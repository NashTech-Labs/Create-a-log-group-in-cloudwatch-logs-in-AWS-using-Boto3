import json
import boto3

REGION = input("Enter the AWS REGION Name: ")

log_client = boto3.client('logs', region_name=REGION)
# these are the valid values are: [1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, 2192, 2557, 2922, 3288, 3653] for retention period
retention_period_in_days = 7

#This configration will use for Backend Log Group.

group_name = input("Enter the name for  backend group: ")
res = log_client.create_log_group(
    logGroupName=group_name,
    tags={
        'Type': 'Back_end',
        'Frequency': '10 seconds',
        'Environment': 'Prod',
        'RetentionPeriod': str(retention_period_in_days)
    }
)

print(json.dumps(res, indent=4))

response = log_client.put_retention_policy(
          logGroupName=group_name,
          retentionInDays=retention_period_in_days
)

print(json.dumps(response, indent=4))

#This configration will use for Frontend Log Group.

log_grp = input("Enter the name for  Front group: ")
response = log_client.create_log_group(
    logGroupName=log_grp,
    tags={
        'Type': 'Front_end',
        'Frequency': '10 seconds',
        'Environment': 'Prod',
        'RetentionPeriod': str(retention_period_in_days)
    }
)

res = log_client.put_retention_policy(
          logGroupName=log_grp,
          retentionInDays=retention_period_in_days
)

print(json.dumps(res, indent=4))

