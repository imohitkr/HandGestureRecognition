# Table of Contents

* [hand\_recognize](#hand_recognize)
  * [hand\_feature\_extract](#hand_recognize.hand_feature_extract)
* [app](#app)
  * [index](#app.index)
  * [video\_feed](#app.video_feed)
  * [about](#app.about)
  * [asl](#app.asl)
  * [video](#app.video)
  * [live\_data\_video](#app.live_data_video)
* [process\_video](#process_video)
  * [frame\_process](#process_video.frame_process)

<a id="hand_recognize"></a>

# hand\_recognize

<a id="hand_recognize.hand_feature_extract"></a>

#### hand\_feature\_extract

```python
def hand_feature_extract(frame, timestamp)
```

Extract hand features from the given frame.

**Arguments**:

- `frame`: the frame to extract hand features from.
- `timestamp`: the timestamp of the frame.

**Returns**:

(frame, landmarks, gestures, palm_orientation) : modified frame, hand landmarks, gestures, palm_orientation

<a id="app"></a>

# app

<a id="app.index"></a>

#### index

```python
@app.route('/')
def index()
```

Return the home page

<a id="app.video_feed"></a>

#### video\_feed

```python
@app.route('/video_feed')
def video_feed()
```

Return the video feed

<a id="app.about"></a>

#### about

```python
@app.route('/about')
def about()
```

Return the about page

<a id="app.asl"></a>

#### asl

```python
@app.route('/asl')
def asl()
```

Return the asl page

<a id="app.video"></a>

#### video

```python
@app.route('/video')
def video()
```

Return the video page

<a id="app.live_data_video"></a>

#### live\_data\_video

```python
@app.route('/live-data_video')
def live_data_video()
```

echo video predictions as JSON

<a id="process_video"></a>

# process\_video

<a id="process_video.frame_process"></a>

#### frame\_process

```python
def frame_process()
```

This function is used to read frames from the camera and run the gesture recognition model on them.

**Returns**:

frame bytes from camera augmented by gesture recognition model

