This script is responsible for sending the received base64 image to Watson Visual
Recognition for classification.


## Configuration

1. Substitute the value *WVR_API_KEY* on the code;
2. Create an action following Docker [guideline][1]. Name this action *classify*;
3. Configure time limit on 60 seconds and memory on 128 MB.

[1]: https://cloud.ibm.com/docs/openwhisk?topic=cloud-functions-prep#prep_python_virtenv