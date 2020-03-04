import glob
import os
import shutil

from PIL import Image
import ibm_boto3
from ibm_botocore.client import Config


cos = ibm_boto3.resource("s3",
    ibm_api_key_id="COS_API_KEY",
    ibm_service_instance_id="COS_SERVICE_INSTANCE",
    ibm_auth_endpoint="https://iam.cloud.ibm.com/identity/token",
    config=Config(signature_version="oauth"),
    endpoint_url="https://s3.us-south.cloud-object-storage.appdomain.cloud"
)


def _folder_from_filename(filename: str) -> str:
    return filename.split('.')[0]


def _load_file(bucket: str, filename: str) -> None:
    folder = _folder_from_filename(filename)
    images = glob.glob(f'{folder}/*')
    file_content = cos.Object(bucket, filename).get()
    output_file = open(filename, 'wb')
    output_file.write(file_content['Body'].read())
    output_file.close()


def _extract_files(filename: str) -> None:
    folder = _folder_from_filename(filename)
    shutil.unpack_archive(filename, folder, 'zip')
    os.remove(filename)


def _convert_files(filename: str) -> None:
    folder = _folder_from_filename(filename)
    images = glob.glob(f'{folder}/*')
    for index, image_path in enumerate(images):
        resized_path = f'{folder}/image{index}.jpg'
        try:
            image = Image.open(image_path)
            resized = image.resize((224, 224), Image.ANTIALIAS)
            resized.save(resized_path)
        except OSError:
            # Some images have invalid format. If they are created
            # they must be removed.
            if os.path.exists(resized_path):
                os.remove(resized_path)
        os.remove(image_path)


def _create_zip_with_converted_files(filename: str) -> None:
    folder = _folder_from_filename(filename)
    shutil.make_archive(folder, 'zip', folder) 


def _delete_folder(filename: str) -> None:
    folder = _folder_from_filename(filename)
    shutil.rmtree(folder)


def _delete_zip_file(filename: str) -> None:
    os.remove(filename)


def _delete_file_on_bucket(bucket: str, filename: str) -> None:
    cos.Object(bucket, filename).delete()


def _upload_converted_file_on_bucket(bucket: str, filename: str) -> None:
    file_content = open(filename, 'rb').read()
    cos.Object(bucket, filename).put(Body=file_content)


def main(args):
    bucket = args.get('bucket')
    filename = args.get('filename')
    _load_file(bucket, filename)
    _extract_files(filename)
    _convert_files(filename)
    _create_zip_with_converted_files(filename)
    _delete_file_on_bucket(bucket, filename)
    _upload_converted_file_on_bucket(bucket, filename)
    _delete_folder(filename)
    _delete_zip_file(filename)
    return {'status': 200}

