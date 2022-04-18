#!/bin/bash

ROOT_DIR="$HOME/tfl"

stdout=$(python3 "$ROOT_DIR/tfl.py")
exit_code=$?

if [ $exit_code -ne 0 ]; then
  echo "Pinging..."

  stdout_escaped=${stdout//$'\n'/\\n}
  source /home/stefan/.secrets
  "$ROOT_DIR/pingme.sh" "$stdout_escaped"

  echo "Pinged"
fi

