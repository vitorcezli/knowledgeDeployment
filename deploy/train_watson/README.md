This script is responsible for getting images from Cloud Object Storage and send
them to Watson Visual Recognition for training and deployment of a model.


## Configuration

1. Substitute the values *COS_API_KEY*, *COS_SERVICE_INSTANCE* and *WVR_API_KEY*
on the code;
2. Create an action following Docker [guideline][1]. Name this action *train*;
3. Configure time limit on 600 seconds and memory on 128 MB.

[1]: https://cloud.ibm.com/docs/openwhisk?topic=cloud-functions-prep#prep_python_virtenv