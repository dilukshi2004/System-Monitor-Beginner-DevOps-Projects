!/usr/bin/env python3

#______DevOps CLI Tool_________________________
# Author : Dilukshi Warangana
# Description : CLI tool to manage AWS resources
#______________________________________________

import argparse
import boto3

# -- AWS Clients --
ec2 = boto3.client('ec2' , region_name='us-east-1')
s3 = boto3.client('s3')
iam = boto3.client('iam')

# -- Functions --

def list_ec2():
        print("\n============================")
        print("            EC2 Instances")
        print("==============================")
        response = ec2.describe_instances()
        instances = response['Reservations']
        if not instances:
                print("No EC@ instances found")
        for reservation in instances:
                for instance in reservation['Instances']:
                        print(f"ID   : {instance['InstanceId']}")
                        print(f"State  : {instance['State']['Name']}")
                        print(f"Type   : {instance['InstanceType']}")
                        print("----------------------------------")

def list_s3():

        print("\n=============================")
        print("           S3 Buckets")
        print("===============================")
        response = s3.list_buckets()
        buckets = response['Buckets']
        if not buckets:
                print("No