from typing import Dict

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import VisualRecognitionV3


visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=IAMAuthenticator('WVR_API_KEY')
)


def main(args: Dict) -> Dict:
    classifiers = visual_recognition.list_classifiers(verbose=True).get_result()
    classifiers_info = [{'classifier_id': classifier['classifier_id'],
                         'name': classifier['name'],
                         'status': classifier['status']}
                         for classifier in classifiers['classifiers']]
    return {'info': classifiers_info}
