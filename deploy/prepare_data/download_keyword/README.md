This script is responsible for downloading images from Google based on a
keyword and zip and send these images to Cloud Object Storage.


## Configuration

1. Substitute the values *COS_API_KEY* and *COS_SERVICE_INSTANCE* on the code;
2. Create an action following Docker [guideline][1]. Name this action *download_keyword*;
3. Configure time limit on 600 seconds and memory on 128 MB.

[1]: https://cloud.ibm.com/docs/openwhisk?topic=cloud-functions-prep#prep_python_virtenv