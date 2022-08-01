import boto3
import json

AWS_REGION = input("Enter the AWS_REGION Name")

client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 5

#This configration will use for Backend Log Group.

log_group = input("Enter the name for  backend group")
response = client.create_log_group(
    logGroupName=log_group,
    tags={
        'Type': 'Back end',
        'Frequency': '30 seconds',
        'Environment': 'Production',
        'RetentionPeriod': str(retention_period_in_days)
    }
)

print(json.dumps(response, indent=4))

response = client.put_retention_policy(
          logGroupName=log_group,
          retentionInDays=retention_period_in_days
)

print(json.dumps(response, indent=4))

#This configration will use for Frontend Log Group.

log_group = input("Enter the name for  Front group")
response = client.create_log_group(
    logGroupName=log_group,
    tags={
        'Type': 'Front end',
        'Frequency': '30 seconds',
        'Environment': 'Production',
        'RetentionPeriod': str(retention_period_in_days)
    }
)

response = client.put_retention_policy(
          logGroupName=log_group,
          retentionInDays=retention_period_in_days
)