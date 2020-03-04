from ibm_watson import VisualRecognitionV3
import base64
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=IAMAuthenticator('WVR_API_KEY')
)


def main(args):
    decoded_string_image = args['image'].encode('utf-8')
    # Decode base64 image.
    decoded = base64.b64decode(decoded_string_image)
    classes = visual_recognition.classify(
        images_file=decoded,
        images_filename='image.jpg',
        threshold=0.5,
        classifier_ids=args['classifier']).get_result()
    # Return the result of classification.
    results = classes['images'][0]['classifiers'][0]['classes']
    result = ('', 0)
    for r in results:
        if r['score'] > result[1]:
            result = (r['class'], r['score'])
    return {'result': result[0] if result[0] else 'invalid'}
