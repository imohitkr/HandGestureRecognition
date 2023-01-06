import os
from typing import Tuple

from matplotlib import pyplot as plt
from mediapipe_model_maker import gesture_recognizer
from mediapipe_model_maker.python.core.data.classification_dataset import ClassificationDataset


def show_images(dataset_path) -> None:
    """
    Show the images in the dataset contained in the dataset_path
    :param dataset_path: path to the dataset
    :return: None
    """
    num_examples = 5
    print(dataset_path)
    labels = []
    for i in os.listdir(dataset_path):
        if os.path.isdir(os.path.join(dataset_path, i)):
            labels.append(i)
    print(labels)

    for label in labels:
        label_dir = os.path.join(dataset_path, label)
        example_filenames = os.listdir(label_dir)[:num_examples]
        fig, axs = plt.subplots(1, num_examples, figsize=(10, 2))
        for i in range(num_examples):
            axs[i].imshow(plt.imread(os.path.join(label_dir, example_filenames[i])))
            axs[i].get_xaxis().set_visible(False)
            axs[i].get_yaxis().set_visible(False)
        fig.suptitle(f'Showing {num_examples} examples for {label}')

    plt.show()


def prepare_data(dataset_path) -> Tuple[ClassificationDataset, ClassificationDataset, ClassificationDataset]:
    """
    Prepare the dataset. The format of the dataset contained in the dataset_path should have the type
    <path>/<label>/<image>.*  and one of the folders for label should be named `none` as the mediapipe requires that
    :param dataset_path: path to the dataset
    :return: (train_data, validation_data, test_data) : training , validation and test data
    """
    data = gesture_recognizer.Dataset.from_folder(
        dirname=dataset_path,
        hparams=gesture_recognizer.HandDataPreprocessingParams()
    )
    train_data, rest_data = data.split(0.8)
    validation_data, test_data = rest_data.split(0.5)
    return train_data, validation_data, test_data


def train_model(dataset_path, learning_rate=0.001, lr_decay=0.99, dropout_rate=0.02, batch_size=10, epochs=100) -> None:
    """
    This trains a model and saves it as a mediapipe task. The task can be then used directly by the mediapipe vision
    library to run against the video feed.
    :param dataset_path: path to the dataset
    :param learning_rate: learning rate to be used for training
    :param lr_decay: learning rate decay to be used for training
    :param dropout_rate: dropout rate for the model
    :param batch_size: batch size to be used for training
    :param epochs: epochs for which to train the model
    :return: None
    """
    train_data, validation_data, test_data = prepare_data(dataset_path)
    hparams = gesture_recognizer.HParams(learning_rate=learning_rate, lr_decay=lr_decay, export_dir="exported_model",
                                         shuffle=True,
                                         batch_size=batch_size, epochs=epochs)
    model_options = gesture_recognizer.ModelOptions(dropout_rate=dropout_rate)
    options = gesture_recognizer.GestureRecognizerOptions(model_options=model_options, hparams=hparams)
    model = gesture_recognizer.GestureRecognizer.create(
        train_data=train_data,
        validation_data=validation_data,
        options=options
    )

    loss, acc = model.evaluate(test_data, batch_size=1)
    print(f"Test loss:{loss}, Test accuracy:{acc}")
    model.export_model()
    model.export_tflite(export_dir="exported_model")


if __name__ == '__main__':
    """
    Example usage:
    1. download the asl_dataset and rename the 0 folder to 'none' as it is required by mediapipe model maker.
    2. Then run the train_model function with proper path 
    3. It will save the results into the exported_model folder and we can use the final model which is called 
    gesture_recognizer.task.
    """
    dataset_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'asl_dataset'
    )
    # show_images(dataset_path)
    # train_model(dataset_path, epochs=200, batch_size=10)
