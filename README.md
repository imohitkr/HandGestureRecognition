## Computer Vision for Gesture Primitives (cv_for_primitives)
Microservice to be used for training and recognition of hand gestures
### Objective 🎯
The objective of this project is to provide tools to train hand gesture recognition. A microservice has also been created
that detects the American Sign Language gestures and also detects the user palm orientation.

### Methodology 🃏
1. Take input from the camera
2. Run the model on the input frame
3. Classify the palm orientation and gesture recognition

### Overview 👓
The code is present within the [src/](src) directory. 
It contains two folders [model](src/model) and [webapp](src/webapp). 
model folder provides code to train a gesture recognition model. 
webapp folder provides us with a already trained model and corresponding web GUI. 

### Running 💻

_These steps are tested on Mac OS and currently mediapipe vision model import is not supported on Windows._

1. Clone the repository

```bash
$ git clone https://github.com/wintechis/cv_for_primitives.git
```
2. Navigate to cloned repository and run the following command to install the dependencies. 

```bash
# install python 3.9 
$ pip install -r requirements.txt
```
3. Move to the [webapp](src/webapp) directory and run the following command to start the web GUI. 
```bash
$ cd src/webapp
$ python app.py
```
4. This should start the web server at `127.0.0.1:5000`. 

This GIF also demonstrates steps 3 and 4.

![](blob/how-to-run.gif)

When the web GUI starts you can navigate to the Video Gesture Recognizer to start playing. 
![](blob/gesture-recognizer.gif)

### FAQ 💡
* If video recognition doesn't work: make sure the camera is not blocked by some other application (e.g. Videocalling in Zoom or Teams).
### License
This project is licensed under the MIT License. See LICENSE for more details
         
     

             







