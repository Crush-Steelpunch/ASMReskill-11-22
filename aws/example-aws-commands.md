# Example aws commands

## Launch an instance (with a tag for the name)

`aws ec2 run-instances --image-id ami-0beb6fc68811e5682  --instance-type t2.small --key-name AMSkey --subnet-id subnet-0a9f06e2e3deb6551 --associate-public-ip-address --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=InstanceName}]'`

## Filter and query example
`aws ec2 describe-instances --filter 'Name=instance-id,Values=i-09214b775c7a27c49' --query Reservations[].Instances[].PublicIpAddress --output text`

## Terminate an instance

`aws ec2 terminate-instances --instance-ids i-00d73c8a67222b75c`

## Stop an instance

`aws ec2 stop-instances --instance-ids i-051f84930d02d744d`

## Create a keypair

`aws ec2 create-key-pair --key-name cli-key`

## Delete a keypair

`aws ec2 delete-key-pair --key-name cli-key`

## S3

`aws s3 cp  Jenkinsfile s3://a3fcc7e7-378e-4ce2-9409-cc5d844db128-clibucket`
`aws s3api get-bucket-policy --bucket s3://a3fcc7e7-378e-4ce2-9409-cc5d844db128-leon`

## VPC

` aws ec2 create-vpc --cidr-block 10.1.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=cli-vpc}]'`
 output: cli-vpc vpc-00116c6f76c8935b1

## Display VPC and CIDR only

`aws ec2 describe-vpcs --query "Vpcs[].[CidrBlockAssociationSet[].CidrBlock],Tags[?Key=='Name'].Value]" --output text`

## Create a subnet

`aws ec2 create-subnet --vpc-id vpc-00116c6f76c8935b1 --cidr-block 10.1.0.0/24 --availability-zone eu-west-2a --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=cli-subnet-a}]'`

## Internet gateway

`aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=cli-internet-gateway}]'`

output: cli-internet-gateway igw-0958eff3610f121a1

## Attach an internet gateway to a vpc

`aws ec2 attach-internet-gateway --vpc-id vpc-00116c6f76c8935b1  --internet-gateway-id igw-0958eff3610f121a1  --region eu-west-2`

## Describe internet Gateways

`aws ec2 describe-internet-gateways`

## Route Tables
`aws ec2 describe-route-tables`

`aws ec2 create-route  --destination-cidr-block 0.0.0.0/0 --route-table-id rtb-0d02b91a3fc9b9c91 --gateway-id igw-0958eff3610f121a1`

## Security Groups

### Create web group

`aws ec2 create-security-group --description "webseccli" --group-name "webseccli" --vpc-id vpc-00116c6f76c8935b1`

### Create Web Group Rules

`aws ec2 authorize-security-group-ingress --group-id sg-02d5e868b37052b93 --port 80 --protocol tcp --cidr 0.0.0.0/0`
`aws ec2 authorize-security-group-ingress --group-id sg-02d5e868b37052b93 --port 22 --protocol tcp --cidr 0.0.0.0/0`

### Create db group

`aws ec2 create-security-group --description "dbseccli" --group-name "dbseccli" --vpc-id vpc-00116c6f76c8935b1`

### Create db Group Rules

`aws ec2 authorize-security-group-ingress --group-id sg-0383fb9dfacfa147b --port 22 --protocol tcp --cidr 0.0.0.0/0`
`aws ec2 authorize-security-group-ingress --group-id sg-0383fb9dfacfa147b --port 22 --protocol tcp --source-group webseccli`

### Modify security groups on a running instance

`aws ec2 modify-instance-attribute --groups <group-ids> --instance-id <instance-id>`

## RDS

`aws rds create-db-instance --db-instance-identifier database-cli --allocated-storage 20  --db-instance-class db.t3.micro --engine mysql --master-username admin --master-user-password password123`

`aws rds describe-db-instances --db-instance-identifier  database-cli`

`aws rds delete-db-instance --db-instance-identifier data`