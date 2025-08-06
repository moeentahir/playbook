#!/bin/bash

set -euo pipefail

YAML_PATH="jenkins.yaml"  # Path to your Jenkins CASC YAML
TAG_KEY="Type"
REGION="us-east-1"

# Define mappings: anchor name, tag value
ANCHOR_NAMES=("ami_ubuntu" "ami_windows" "ami_arm64")
AMI_TAG_VALUES=("ubuntu" "windows" "arm")

# Function to get the latest AMI ID for a given tag
get_latest_ami() {
  local tag_value="$1"
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

# Build new AMI ID list
AMI_IDS=()
for ((i = 0; i < ${#AMI_TAG_VALUES[@]}; i++)); do
  tag="${AMI_TAG_VALUES[$i]}"
  ami_id=$(get_latest_ami "$tag")
  if [[ -z "$ami_id" ]]; then
    echo "❌ No AMI found for tag: $tag"
    exit 1
  fi
  echo "✅ ${ANCHOR_NAMES[$i]} → $ami_id (tag: $tag)"
  AMI_IDS+=("$ami_id")
done

echo "✍️ Updating AMI anchors in YAML..."

# Replace the lines with anchor definitions
for ((i = 0; i < ${#ANCHOR_NAMES[@]}; i++)); do
  anchor="${ANCHOR_NAMES[$i]}"
  new_ami="${AMI_IDS[$i]}"

  # Use sed to replace the line like: ami_id: &ami_ubuntu "ami-xxxx"
  sed -i '' -E "s/(^.*&${anchor}.*)\"ami-[a-zA-Z0-9]+\"/\1\"${new_ami}\"/" "$YAML_PATH"

  echo "🔁 Updated &${anchor} to ${new_ami}"
done

echo "✅ Finished updating anchors in $YAML_PATH"
