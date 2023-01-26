## Converting Keras Model to TF-Lite 

In model training, we saved the model in h5 format in the file 'mobilenet\_v1\_03\_1.000.h5'.  

The code for converting the model to TF-Lite format is found in the notebook Converting\_Keras\_Model\_to\_TF-Lite.ipynb. 

The TF-Lite version is stored in the file 'scene-classifier-model.tflite'.  This version is used in building a containerized service and deploying it to AWS Lambda.

Details of containerization and cloud-deployment are found in [containerize.md](containerize.md) and [deploy\_aws\_lambda.md](deploy\_aws\_lambda.md).

