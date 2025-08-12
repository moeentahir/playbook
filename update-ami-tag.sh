#!/bin/bash
# ----------- CONFIGURATION -----------
REGION="us-east-1"
SEARCH_TAG_KEY="Environment"
SEARCH_TAG_VALUE="Production"
NEW_TAG_KEY="Backup"
NEW_TAG_VALUE="Yes"
# --------------------------------------

echo "Finding AMIs in region $REGION with tag $SEARCH_TAG_KEY=$SEARCH_TAG_VALUE..."

# Get the list of AMI IDs matching the tag
AMI_IDS=$(aws ec2 describe-images \
    --region "$REGION" \
    --owners self \
    --filters "Name=tag:${SEARCH_TAG_KEY},Values=${SEARCH_TAG_VALUE}" \
    --query "Images[*].ImageId" \
    --output text)

if [ -z "$AMI_IDS" ]; then
    echo "No AMIs found with tag ${SEARCH_TAG_KEY}=${SEARCH_TAG_VALUE}."
    exit 0
fi

echo "Found AMIs: $AMI_IDS"
echo "Adding tag $NEW_TAG_KEY=$NEW_TAG_VALUE to each AMI..."

# Loop through AMIs and add the new tag
for AMI_ID in $AMI_IDS; do
    echo "Tagging $AMI_ID..."
    aws ec2 create-tags \
        --region "$REGION" \
        --resources "$AMI_ID" \
        --tags "Key=${NEW_TAG_KEY},Value=${NEW_TAG_VALUE}"
done

echo "Tagging complete!"
