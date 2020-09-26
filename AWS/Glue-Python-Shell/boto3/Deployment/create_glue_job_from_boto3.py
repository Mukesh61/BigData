"""
Couple of thing we need to keep in mind while creating new glue jobs from awscli and boto3 from window machine.
Install awscli using "pip install awscli"
then pip install boto3
then configure your account using "aws configure" pass secret key and id
and you are all set to use cli from your desktop.
MaxCapacity=0.0625 for pythonshell job

"""

import boto3
client = boto3.client('glue')
response = client.create_job(
    Name='python-redshift-test1',
    Description='for testing',
    Role='AWSGlueServiceRole-Glueuser',
    ExecutionProperty={
        'MaxConcurrentRuns': 2
    },
    Command={
        'Name': 'pythonshell',
        'ScriptLocation': 's3://bucket_name/Refined/read_json_from_s3.py',
        'PythonVersion': '3'
    },
    DefaultArguments={
        '--extra-py-files': "s3://bucket_name/Output/lib/cffi-1.14.3-2-cp36-cp36m-manylinux1_x86_64.whl"+","+"s3://bucket_name/Output/lib/cryptography-3.1-2-cp35-abi3-manylinux2010_x86_64.whl"+","+"s3://bucket_name/Output/lib/pycparser-2.20-2-py2.py3-none-any.whl",
        'extra_key':'new_value'
    },

    Connections={
        'Connections': [
            'dev_etl_recon',
            'redshift-test',
        ]
    },
    Timeout=123,
    MaxCapacity=0.0625,
    Tags={
        'pub-dev': '12356'
    },
    NotificationProperty={
        'NotifyDelayAfter': 123
    }
)

print(response)
