#!/bin/bash
set -o allexport; source .env; set +o allexport

download_datetime=$(date '+%Y%m%d%H%M%S');

TMPFILE=$(mktemp "/tmp/county-list-$download_datetime.json.XXXXXXX")
LATEST_FILE=json/county-list-latest.json

printf "\n\n"

# Make json directory if it doesn't exist
[ -d json ] || mkdir json

python scrape_county_list.py
python combine_weekly_versions.py > $TMPFILE

# Test that this is a seemingly valid file
FIRST_COUNTY="$(cat $TMPFILE | jq 'keys[0]')"
if [ $FIRST_COUNTY == '"Aitkin"' ]; then
  echo "Seems to be JSON in expected format. Checking for changes from last version."

  if cmp --silent $TMPFILE $LATEST_FILE; then
     echo "File unchanged. No upload will be attempted."
  else
     echo "Changes found. Updating latest file..."
     cp $TMPFILE $LATEST_FILE

     # Push "latest" to s3
     gzip -vc $LATEST_FILE | aws s3 cp - s3://$S3_URL/$LATEST_FILE \
     --profile $AWS_PROFILE_NAME \
     --acl public-read \
     --content-type=application/json \
     --content-encoding gzip

     # Push timestamped to s3
     gzip -vc $LATEST_FILE | aws s3 cp - "s3://$S3_URL/county-list-$download_datetime.json" \
     --profile $AWS_PROFILE_NAME \
     --acl public-read \
     --content-type=application/json \
     --content-encoding gzip

     # Make local timestamped file for new changed version
     cp $TMPFILE "json/county-list-$download_datetime.json"
  fi

   # Check response headers
   RESPONSE_CODE=$(curl -s -o /dev/null -w "%{http_code}" $S3_URL/$LATEST_FILE)
   if [ $RESPONSE_CODE == '200' ]; then
     echo "Successfully test-retrieved 'latest' file from S3."
   else
     echo "***** WARNING WARNING WARNING: No 'latest' file could be retrieved from S3. Response code $RESPONSE_CODE *****"
   fi

   # curl -I $S3_URL/$LATEST_FILE

   # Get first entry of uploaded json
   FIRST_COUNTY="$(cat $TMPFILE | jq 'keys[0]')"
   if [ $FIRST_COUNTY == '"Aitkin"' ]; then
     echo "$FIRST_COUNTY"
   else
     echo "***** WARNING WARNING WARNING: Test-retrieved 'latest' file does not seem to be parseable JSON in expected format. *****"
   fi
else
  echo "***** WARNING WARNING WARNING: The newest file doesn't seem to be what we'd expect from elex JSON. Taking no further action. *****"
fi
printf "\n\n"
