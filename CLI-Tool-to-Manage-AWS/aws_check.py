#!/usr/bin/env python3
import boto3

#Connect to AWS

ec2 = boto3.client('ec2' , region_name='us-east-1')
s3 = boto3.client('s3')

#List ec2 instances
print("=== EC2 Instances ===")
response = ec2.describe_instances()
for reservation in response['Reservations']:
        for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']} | State: {instance['State']['Name']}")

#List S3 buckets
print ("\n== S3 buckets ===")
response  = s3.list_buckets()
for bucket in response['Buckets']:
        print(f"Bucket: {bucket['Name']}")











