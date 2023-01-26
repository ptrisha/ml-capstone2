# Scene Classification with MobileNet

## Project Overview
In this project, we train a CNN (Convolutional Neural Network) image classifier for that is able to distinguish 3 types of natural scenery: coast, forest, and mountain. We apply transfer learning, basing the classifier on MobileNet [1] which has been shown to efficiently trade off between latency and accuracy.  Our aim is to develop a lightweight yet performant model which would be useful in mobile and embedded applications.

Scene classification is a challenging problem in computer vision.  In addition to recognizing objects in an image, the classifier has to understand the layout of the objects and the contextual content. Despite these challenges, it is an active area of research, because there are many real-world applications such as image retrieval, robotics, self-driving cars and disaster detection.




## Dataset
We extract the 3 classes of images from the static images database of SUN 09 Dataset [2].  The dataset is available for download [sun09.tar](http://groups.csail.mit.edu/vision/Hcontext/data/sun09.tar) (5.2GB).  More information about the dataset is available on the [project webpage](http://people.csail.mit.edu/myungjin/HContext.html).  The dataset was developed for leveraging the contextual information in images.

We extracted a total of 1158 images from the SUN 09 Dataset.  The images are organized into 3 subfolders according to their classification.  The folder is zipped and available as data\_sun09.zip in the [data\_prep\_eda](data_prep_eda/) folder of this repo.  Also found in the folder is the data.zip file which contains the same files as data\_sun09.zip, except that the files have been organized into train/validation/test subfolders in preparation for model training.  The code for data preparation is found in the Data_Preparation.ipynb notebook in the same folder.

## EDA
Please refer to the EDA.ipynb notebook in the [data\_prep\_eda](data_prep_eda/) folder for an analysis of the image dataset.

## Model Training
We first trained the Xception model and found the results to be excellent, and then proceeded to train with MobileNet for comparison.  Generally, our MobileNet models performed only slightly worse.  We also tuned the learning rate and applied data augmentation with transformations: vertical flip, horizontal and vertical translation, zoom-in/out).  Eventually, our best model with data augmentation was for learning rate=0.01 achieving validation accuracy of 100% at epoch 3.

The model training notebooks and data resources are found in the [train\_model](train\_model/) folder of this repo.

Model training was run on [Saturn Cloud](https://saturncloud.io/).

### Exporting training notebook to script
The logic for model training has been exported to a separate Python script model\_training.py in the [train\_model](train\_model/) folder.

## Dependency and Environment Management

This project has been run in a Conda environment.  The conda env file is environment.yml in the root folder of this repo.

To set up the local environment for this project:  

- Open a terminal in the working directory.
- To create the conda environment from the file:
    ```
    conda env create -f environment.yml
    ```
- To activate the environment:
    ```
    conda activate sc_env
    ```
    
To set up the environment for running the model training notebooks in Saturn Cloud and create a Jupyter notebook with Tensorflow and GPU:

1. Click "New Resource from a Template"
2. Select "TensorFlow (Python)"
3. Type a name in the "Name" slot.
4. Click "Edit" button on the top right corner.
5. Scroll down to "Environment" section and click on the "Pip" tab.
6. Type "scipy" under Pip.
7. Check the box for "This is a requirements.txt"
8. Scroll down to the bottom and click "Save" to save settings.
9. Click "Overview" tab and the "Start" button to start the Jupyter workspace.
10. When it has started, expand on "Jupyter Lab" and click "Jupyter Notebook".

It is not necessary to set up SSH connection as shown in the course video.  Simply use the Upload function in the cloud notebooks to upload the model training notebooks and zipped data files.  To unzip the data file, create a Terminal in the cloud notebook and unzip the data in command line.  Also, the training script model\_train.py can be uploaded and run in a Terminal.
    
    


## Containerization

The saved model (in h5 format) is converted to TF-Lite version.  The model is deployed to AWS Lambda in a docker container.

Instructions for building and running the container are found in [containerize.md](containerize\_deploy/containerize.md) in the [containerize\_deploy](containerize\_deploy/) folder.  Other resources for containerization have also been placed in the folder.

## Cloud Deployment

Details of deployment of the service as an AWS Lambda function and testing it are described in [deploy\_aws\_lambda.md](containerize\_deploy/deploy\_aws\_lambda.md) in the [containerize\_deploy](containerize\_deploy/) folder.  


## References
1.  [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861)
2.  [Exploiting Hierarchical Context on a Large Database of Object Categories](http://people.csail.mit.edu/myungjin/HContext.html)

