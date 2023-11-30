#!/bin/bash

aws route53 list-resource-record-sets --hosted-zone-id $1 --profile ${2:-"default"} > ../temp/resource-records.json
python3 ../main.py 