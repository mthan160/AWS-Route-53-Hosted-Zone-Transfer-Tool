#!/bin/bash

aws route53 change-resource-record-sets --hosted-zone-id $1 --change-batch file://../temp/resource-records-transformed.json --profile ${2:-"default"}