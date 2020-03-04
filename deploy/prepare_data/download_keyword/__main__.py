import os

import ibm_boto3
from ibm_botocore.client import Config, ClientError

import glob
import os
import zipfile

from google_images_download import google_images_download


def _download_images(keyword):
    # *downloaded* variable is used to verify if some images were crawled,
    # because sometimes **google_images_download** doesn't download any image.
    downloaded = 0
    while downloaded == 0:
        response = google_images_download.googleimagesdownload()
        arguments = {'keywords': keyword,
                     'output_directory': '.',
                     'limit': 100}
        downloaded = len(response.download(arguments)[0][keyword])


def _zip_content(keyword):
    zip_file = zipfile.ZipFile(f'{keyword}.zip', 'w')
    for image in glob.glob(f'{keyword}/*'):
        zip_file.write(image, os.path.basename(image))
    zip_file.close()


def _crawl(keyword):
    _download_images(keyword)
    _zip_content(keyword)


cos = ibm_boto3.resource("s3",
    ibm_api_key_id="COS_API_KEY",
    ibm_service_instance_id="COS_SERVICE_INSTANCE",
    ibm_auth_endpoint="https://iam.cloud.ibm.com/identity/token",
    config=Config(signature_version="oauth"),
    endpoint_url="https://s3.us-south.cloud-object-storage.appdomain.cloud"
)


def main(args):
    bucket = args.get('bucket')
    keyword = args.get('keyword')
    _crawl(keyword)
    file_name = f'{keyword}.zip'
    file_content = open(file_name, 'rb').read()
    cos.Object(bucket, file_name).put(Body=file_content)
    return {'status': 200}

