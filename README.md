# DNS Hosted Zone Transfer Tool
This tool is designed to facilitate the transfer of DNS Hosted Zone records from one AWS account to another. It aims to simplify the process of migrating DNS records, making it more efficient and less prone to errors.

## Features
- Transfer all types of DNS records (A, AAAA, CNAME, MX, etc.)
- Support for both public and private hosted zones
- Validation checks to ensure record integrity during transfer
- Detailed logging of the transfer process

## Prerequisites
- AWS CLI installed and configured with access to both source and destination AWS accounts
- Python 3.6 or higher

## Installation
Clone the repository to your local machine:

```bash
git clone git@github.com:mthan160/AWS-Route-53-Hosted-Zone-Transfer-Tool.git
```

Navigate to the project directory and install the required dependencies:

```bash
cd dns-transfer-tool
pip install -r requirements.txt
```

## Usage

```bash
cd scripts
./1-list-resource-record-sets.sh <Hosted Zone ID> <AWS CLI Profile>
```

Replace <Hosted Zone ID>, <AWS CLI Profile> with the appropriate values. The script will output a JSON file containing the DNS records for the specified Hosted Zone.

Once you've confirmed that the records in resource-records-transformed.json are correct, run:

```bash
./2-create-resource-record-sets.sh <Hosted Zone ID> <AWS CLI Profile>
```

To create the records in the new Hosted Zone in the destination AWS account.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## References
- [AWS Route 53 Developer Guide - Migrating DNS Service for an Existing Domain to Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html)

Please note that this tool is not officially supported by AWS and is provided as-is, with no guarantees. Always test thoroughly before using in a production environment.

## Disclaimer
Please note that this tool is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

The user assumes all responsibility for any damages or faults that may occur from using this tool. It is strongly recommended that users review the output of the tool before using it to push DNS records into their Hosted Zones. Always test thoroughly before using in a production environment.