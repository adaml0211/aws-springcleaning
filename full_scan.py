#! /usr/bin/env python3
from sys import exit

try:
    import config
except ModuleNotFoundError:
    print("Please create a 'config.py' before running this tool")
    exit(1)

import crayons
import helper
import timeit
from datetime import datetime

from modules import (
    ami,
    ec2_snapshots,
    ec2,
    rds_snapshots,
    securitygroups,
    volumes,
    lambdafunctions,
    cloudwatch,
    cloudformation,
    s3,
)

print("Starting full account scan for these Regions: {}".format(",".join(config.REGIONS)))
account_id = helper.get_account_id()
print("Account: {}".format(account_id))
start_date = datetime.now().strftime("%Y-%m-%d_%H:%M")
print("Start date: {}".format(datetime.now()))

start = timeit.default_timer()

print(crayons.yellow("Scanning AMIs"))
ami.scan()

print(crayons.yellow("Scanning EC2 instances"))
ec2.scan()

print(crayons.yellow("Scanning EC2 volumes"))
volumes.scan()

print(crayons.yellow("Scanning EC2 snapshots"))
ec2_snapshots.scan()

print(crayons.yellow("Scanning RDS snapshots"))
rds_snapshots.scan()

print(crayons.yellow("Scanning security groups"))
securitygroups.scan()

print(crayons.yellow("Scanning CloudWatch loggroups"))
cloudwatch.scan()

print(crayons.yellow("Scanning Lambda functions"))
lambdafunctions.scan()

print(crayons.yellow("Scanning CloudFormation"))
cloudformation.scan()

print(crayons.yellow("Scanning S3"))
s3.scan()

stop = timeit.default_timer()
runtime = int(stop - start)
print("Scan finished after {} seconds".format(crayons.yellow(runtime)))
