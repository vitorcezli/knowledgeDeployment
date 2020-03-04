import random
import string
import threading
import time

import ibm_boto3
import requests
from ibm_botocore.client import Config


def create_bucket(bucket_name):
    cos = ibm_boto3.resource('s3',
        ibm_api_key_id='COS_API_KEY',
        ibm_service_instance_id='COS_SERVICE_INSTANCE',
        ibm_auth_endpoint='https://iam.cloud.ibm.com/identity/token',
        config=Config(signature_version='oauth'),
        endpoint_url='https://s3.us-south.cloud-object-storage.appdomain.cloud'
    )
    cos.create_bucket(Bucket=bucket_name)


def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def post_data(bucket_name, keyword):
    data = {'bucket': bucket_name, 'keyword': keyword}
    requests.post('API_URL', json=data)


def main(dict):
    random_prefix = random_string(32)
    bucket_name = f"{random_prefix}-{dict['classifier']}"
    create_bucket(bucket_name)
    for keyword in dict['keywords']:
        threading.Thread(target=post_data, args=(bucket_name, keyword,)).start()
    time.sleep(300)  # Wait for the data to be downloaded and converted.
    return {'bucket': bucket_name}
