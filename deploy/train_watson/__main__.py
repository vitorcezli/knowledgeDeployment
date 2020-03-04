import glob
from typing import Dict

import ibm_boto3
from ibm_botocore.client import Config
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import VisualRecognitionV3


cos = ibm_boto3.resource('s3',
    ibm_api_key_id='COS_API_KEY',
    ibm_service_instance_id='COS_SERVICE_INSTANCE',
    ibm_auth_endpoint='https://iam.cloud.ibm.com/identity/token',
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.us-south.cloud-object-storage.appdomain.cloud'
)


visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=IAMAuthenticator('WVR_API_KEY')
)


def _download_training_data(bucket: str) -> None:
    files = cos.Bucket(bucket).objects.all()
    for filename in files:
        file_object = cos.Object(bucket, filename.key).get()
        output_file = open(filename.key, 'wb')
        output_file.write(file_object['Body'].read())
        output_file.close()


def _get_training_data() -> Dict:
    training_data = dict()
    files = glob.glob('*.zip')
    for filename in files:
        keyword = '.'.join(filename.split('.')[:-1])
        training_data[keyword] = open(filename, 'rb')
    return training_data


def _train_watson(classifier: str, training_data: Dict) -> None:
    visual_recognition.create_classifier(
        classifier,
        positive_examples=training_data
    )


def main(args) -> Dict:
    bucket = args.get('bucket')
    _download_training_data(bucket)
    training_data = _get_training_data()
    classifier = '-'.join(bucket.split('-')[1:])
    _train_watson(classifier, training_data)
    return args
