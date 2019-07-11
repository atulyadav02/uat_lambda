import json 
import boto3

s3 = boto3.resource('s3')

def handler(event, context):

 bucketlist = []

 for bucket in s3.buckets.all():
  bucketlist.append(bucket.name)
#hello I am updating this code for a purpose

 return {
  "statusCode": 200,
  "body": bucketlist
 }
