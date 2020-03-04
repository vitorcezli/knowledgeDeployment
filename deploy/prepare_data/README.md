The scripts on this folder prepares the data for training, downloading images
and converting them to JPEG.


## Configuration

1. Go to the subfolders and execute the action on their README;
2. Create an action sequence called *download_convert* and add the actions
created on *download_keyword* and *convert* folders;
3. Create an API called *downloadConvert* and add the sequence with the same
name on it;
4. Substitute the values *COS_API_KEY* and *COS_SERVICE_INSTANCE* on *prepare_data*
code;
5. Substitute the value *API_URL* with the URL of the API that was created;
6. Create an action on IBM Cloud Functions called *prepare_data* and copy the
code on *prepare_data.py* file to it;
7. Configure time limit on 600 seconds and memory on 128 MB.