import numpy as np
from tensorflow.python.keras.models import load_model

model = load_model('model_SIBI.h5')

# Hard Encode for the Prediction
classes = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}


def classify(landmarks):
    if not landmarks:
        return ''
    image = []
    # print(landmarks)
    for landmark in landmarks:
        for val in landmark:
            image.append([val])
    image = np.array([image])
    # print(image.shape)

    predictions = model.predict_classes(image)
    for alphabets, values in classes.items():
        if values == predictions[0]:
            return alphabets

    return ''
