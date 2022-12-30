# cv_for_primitives
Developing a Camera-based Application for Gestural Primitives Recognition (Hand).
# Objective 🎯
The objective of this project is to train and deploy a microservice that detects the current emotion of a user based on facial expression from the webcam inputs.
# Methodology 🃏
The video model predict the emotion in parallel. The final class prediction is a weighted and combined "multimodal" prediction of the two seperate predictions.
# Overview 👓
[Train model video](https://github.com/wintechis/cv_for_primitives/blob/main/src/webapp/process_video.py)

[Webapp](https://github.com/wintechis/cv_for_primitives/blob/main/src/webapp)

[H5 Files](https://github.com/wintechis/cv_for_primitives/blob/main/src/webapp/model_SIBI.h5)
# Training 📉
* CNN as chosen models for video analyzing
*  Video: 📽️
    * Dataset:(https://www.kaggle.com/datasets/ayuraj/asl-dataset)
    
    * Improved by:Flatten, Dropout
# Deployment Tech Stack💻
* Models trained using tensorflow and jupyter notebooks

* real-live graphs shown using highcharts.js and Ajax

* Webapp built with Flask

* Front-end:

     * Flask
     * json
     
* Back-end:

    * Python
    * Keras
    * Numpy
    * CV2
    * mediapipe
# Requirements and installation instructions / Tutorial
* a [Python Installation](https://www.python.org/downloads/) is necessary(atleast V3.7)
* a working webcam and microphone is necessary. The input ports should be detected automatically.
* git clone the repo
* Install the dependencies from requirements.txt (pip install -r requirements.txt)
* run the app.py file and wait until the server is started and ready. This can take up to 2 minutes
* open localhost 127.0.0.1:5000/ on your favorite web browser
* the usage of the application is self-explanatory
         
     

             







