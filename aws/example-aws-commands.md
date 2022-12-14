# Example aws commands

## Launch an instance (with a tag for the name)

aws ec2 run-instances --image-id ami-0beb6fc68811e5682  --instance-type t2.small --key-name AMSkey --subnet-id subnet-0a9f06e2e3deb6551 --associate-public-ip-address --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=InstanceName}]'

## Terminate an instance

aws ec2 terminate-instances --instance-ids i-00d73c8a67222b75c

## Stop an instance

aws ec2 stop-instances --instance-ids i-051f84930d02d744d

## Create a keypair

aws ec2 create-key-pair --key-name cli-key

## Delete a keypair

aws ec2 delete-key-pair --key-name cli-key