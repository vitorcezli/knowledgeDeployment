from typing import Dict

import ibm_boto3
from ibm_botocore.client import Config


cos = ibm_boto3.resource('s3',
    ibm_api_key_id='COS_API_KEY',
    ibm_service_instance_id='COS_SERVICE_INSTANCE',
    ibm_auth_endpoint='https://iam.cloud.ibm.com/identity/token',
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.us-south.cloud-object-storage.appdomain.cloud'
)


def _delete_items_bucket(bucket: str) -> None:
    items = cos.Bucket(bucket).objects.all()
    for item in items:
        cos.Object(bucket, item.key).delete()


def _delete_bucket(bucket: str) -> None:
    cos.Bucket(bucket).delete()


def main(args) -> Dict:
    bucket = args.get('bucket')
    _delete_items_bucket(bucket)
    _delete_bucket(bucket)
    return {'status': 200}
