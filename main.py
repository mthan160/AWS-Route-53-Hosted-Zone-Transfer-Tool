import json

def transform_route53_records(input_file, output_file):
    # Create new JSON
    output_json = {
        "Comment": "Imported from Route53",
        "Changes": []
    }

    # Load the original data
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Process each record set
    for record_set in data.get('ResourceRecordSets', []):
        # Remove 'ResourceRecords' if the type is not supported for import
        if record_set['Type'] not in ['A', 'AAAA', 'CNAME', 'MX', 'NAPTR', 'PTR', 'SPF', 'SRV', 'TXT']:
            print('Skipping unsupported record type: ' + record_set['Type'])
            continue
            # if 'ResourceRecords' in record_set:
            #     del record_set['ResourceRecords']

        # Remove 'AliasTarget' and 'HealthCheckId' as they are not supported for import
        # if 'AliasTarget' in record_set:
        #     del record_set['AliasTarget']
        # if 'HealthCheckId' in record_set:
        #     del record_set['HealthCheckId']

        output_ResourceRecordSet = {
            "Action": "CREATE",
            "ResourceRecordSet": record_set
        }

        output_json['Changes'].append(output_ResourceRecordSet)

    # Save the transformed data
    with open(output_file, 'w') as file:
        json.dump(output_json, file, indent=4)

# Usage
input_file = '../temp/resource-records.json'
output_file = '../temp/resource-records-transformed.json'
transform_route53_records(input_file, output_file)
