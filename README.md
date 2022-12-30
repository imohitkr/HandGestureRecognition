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
     * Ajax
     * Bootstrap
* Back-end:

    * Python
    * Keras
    * Numpy
    * CV2
    * Pyaudio
    * Librosa
         
     

             







