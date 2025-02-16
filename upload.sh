#!/usr/bin/bash
DESTINATION_ADDRESS=$1
DESTINATION_USER=zen
rsync -v -e ssh ../basic_robot/ {$DESTINATION_USER}@{$DESTINATION_ADDRESS}:/home/{$DESTINATION_USER}/workspace/