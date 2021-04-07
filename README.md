# Shape-Classifier

Machine Learning Model that accurately classifies shapes such as circles, triangles, squares and rectangles.

## Clone

```bash
git clone "https://github.com/CSjianbel/Shape-Classifier.git"
```

## Project Overview

1. Generate the Data
   - Generate `n` random images of shapes
2. Create and train a Convolutional Neural Network
   - Load in the dataset
   - Feed into the CNN
   - Make Tweaks on CNN model to improve accuracy/performance
3. Python Application that utilizes the shape classifier model
   - 3 Modes:
     1. User provides image to be classified
     2. GUI application that let's the user draw shapes and the model classifies the drawing
     3. Webcam, the user can turn on their camera and show hand-drawn shapes to the camera for the model to classify

## Setup

```bash
pip install -r requirements.txt
```

## Generate Images Data

```bash
python generate_shape_images.py
```

## Train and Save a CNN model

```bash
python shape_classifier_model.py

python shape_classifier_model.py [model.h5]
```

## Use the CNN model

Default model will be in ~Models/shape_classifier_model.h5~.

```bash
python shape_classifier.py

python shape_classifier.py --webcam

python shape_classifier.py [path to image]

python shape_classifer.py -m [path to model]
```

## Supported Shapes

- Circles
- Triangles
- Squares
- Rectangles

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License

[MIT](https://choosealicense.com/licenses/mit/)

_A Project by Jiankarlo A. Belarmino_
