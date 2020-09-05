"""
Note: use json.loads not json.load function after decoding the data
Some time we make mistake by trying to read directly using the file path like in our local machine. which doesn't work.
key point is we need to use boto3 resource function to read data from AWS S3

common error: file/directory not found :- that means we are not able to locate our file in S3 possibly due to incorrect file path or we are not using boto3
                                          if you are using boto3 still getting same error then check the parameter pass like bucket_name and itemname
              should i decode or not: it is not mandatory as json.loads can take care of byte code, this problem you might face reading normal json file also
"""
import json
import boto3

s3 = boto3.resource('s3')

bucketname = 'bucket_name'
itemname = 'folder/sample_json_example.json'
#s3://bucket_name/folder/sample_json_example.json


obj = s3.Object(bucketname, itemname)
body = obj.get()['Body'].read().decode('utf-8') #String output after decoding byte code to utf-8 readable formate
#body = obj.get()['Body'].read()    #Byte code output
json_data = json.loads(body)

print(json_data)
