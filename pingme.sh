#!/bin/bash

[ -z "$IFTTT_TOKEN" ] && { echo "IFTTT_TOKEN is not set" ; exit 1; }

URL="https://maker.ifttt.com/trigger/tfl_webhook/with/key/$IFTTT_TOKEN"

PAYLOAD="{\"value1\": \"$1\"}"

curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD" \
  "$URL"

