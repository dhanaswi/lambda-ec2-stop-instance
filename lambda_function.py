import boto3

# AWS region where the EC2 instance is running
REGION = "us-east-1"

# Replace this with your EC2 Instance ID
INSTANCE_ID = "i-000b64fbb6fe987b1"

def lambda_handler(event, context):
    ec2 = boto3.client("ec2", region_name=REGION)
    ec2.stop_instances(InstanceIds=[INSTANCE_ID])

    return {
        "statusCode": 200,
        "body": "EC2 instance stopped successfully"
    }
