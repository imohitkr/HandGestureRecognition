# Table of Contents

* [model-maker](#model-maker)
  * [show\_images](#model-maker.show_images)
  * [prepare\_data](#model-maker.prepare_data)
  * [train\_model](#model-maker.train_model)

<a id="model-maker"></a>

# model-maker

<a id="model-maker.show_images"></a>

#### show\_images

```python
def show_images(dataset_path) -> None
```

Show the images in the dataset contained in the dataset_path

**Arguments**:

- `dataset_path`: path to the dataset

**Returns**:

None

<a id="model-maker.prepare_data"></a>

#### prepare\_data

```python
def prepare_data(
    dataset_path
) -> Tuple[ClassificationDataset, ClassificationDataset,
           ClassificationDataset]
```

Prepare the dataset. The format of the dataset contained in the dataset_path should have the type

<path>/<label>/<image>.*  and one of the folders for label should be named 'none' as the mediapipe requires that

**Arguments**:

- `dataset_path`: path to the dataset

**Returns**:

(train_data, validation_data, test_data) : training , validation and test data

<a id="model-maker.train_model"></a>

#### train\_model

```python
def train_model(dataset_path,
                learning_rate=0.001,
                lr_decay=0.99,
                dropout_rate=0.02,
                batch_size=10,
                epochs=100) -> None
```

This trains a model and saves it as a mediapipe task. The task can be then used directly by the mediapipe vision

library to run against the video feed.

**Arguments**:

- `dataset_path`: path to the dataset
- `learning_rate`: learning rate to be used for training
- `lr_decay`: learning rate decay to be used for training
- `dropout_rate`: dropout rate for the model
- `batch_size`: batch size to be used for training
- `epochs`: epochs for which to train the model

**Returns**:

None

