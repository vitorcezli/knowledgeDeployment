This script standardizes the images on Cloud Object Storage, resizing and
converting them to jpeg.


## Configuration

1. Substitute the values *COS_API_KEY* and *COS_SERVICE_INSTANCE* on the code;
2. Create an action on IBM Cloud Functions called *convert* and copy the code on
*convert.py* file to it;
3. Configure time limit on 600 seconds and memory on 256 MB.