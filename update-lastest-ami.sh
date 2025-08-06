#!/bin/bash

set -euo pipefail

YAML_PATH="jenkins.yaml"  # Update this path as needed
TAG_KEY="Type"            # The AMI tag key used to filter
REGION="us-east-1"        # Change to your desired region

# Map Jenkins EC2 template label -> AMI tag value
declare -A TEMPLATE_AMI_MAP=(
  ["ubuntu-agent"]="ubuntu"
  ["windows-agent"]="windows"
  ["arm64-agent"]="arm"
)

# Function to get latest AMI by tag
get_latest_ami() {
  local tag_value=$1
  aws ec2 describe-images \
    --region "$REGION" \
    --owners self \
    --filters "Name=tag:${TAG_KEY},Values=${tag_value}" "Name=state,Values=available" \
    --query "Images[*].[ImageId,CreationDate]" \
    --output text | \
    sort -k2 -r | \
    head -n1 | \
    awk '{print $1}'
}

echo "🔍 Fetching latest AMIs..."

# Build a label-to-AMI-ID map
declare -A AMI_ID_MAP
for label in "${!TEMPLATE_AMI_MAP[@]}"; do
  tag_value="${TEMPLATE_AMI_MAP[$label]}"
  ami_id=$(get_latest_ami "$tag_value")
  if [[ -z "$ami_id" ]]; then
    echo "❌ No AMI found for tag ${TAG_KEY}=${tag_value}"
    exit 1
  fi
  echo "✅ $label → $ami_id (tag: $tag_value)"
  AMI_ID_MAP["$label"]=$ami_id
done

echo "✍️ Updating YAML with new AMIs..."

# Update each EC2 template's AMI using yq
for label in "${!AMI_ID_MAP[@]}"; do
  ami="${AMI_ID_MAP[$label]}"
  echo "🔁 Updating label '$label' to AMI '$ami'"

  yq -i "
    (.jenkins.clouds[]?.amazonEC2.templates[] | select(.labelString == \"$label\") ).ami = \"$ami\"
  " "$YAML_PATH"
done

echo "✅ YAML update complete: $YAML_PATH"
