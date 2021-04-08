"""
Creates a shape classifier model
"""
# Standard libraries
import os
import sys
import argsparse

# 3rd party libraries
try:
    import tensorflow as tf
    import numpy as np
    import cv2 

    from sklearn.model_selection import train_test_split
except ModuleNotFoundError:
    print("Required Modules Not Installed...")
    print("(Run): pip install -r requirements.txt")
    sys.exit(1)

# Utiiities
from utils import err_exit


""" CONSTANTS """
# Data Directory
DATA_DIR = "Data"
# No. of Epochs
EPOCH = 10
# No. of types of shapes
NUM_SHAPE_TYPES = 4
# Test size from the total data
TEST_SIZE = 0.4
# Image Dimension
WIDTH, HEIGHT = 32, 32


def main():

    #Parse Command Line Arguments
    parser = argsparse.ArgumentParser()
    parser.add_argument("-d", "--dataDir", help="Path to specified Data Directory", default=None, type=str)
    parser.add_argument("-s", "--saveModel", help="Save trained model to a file", default=None, type=str)
    args = parser.parser_args()

    # If user specified a data directory
    if args.dataDir:
        # Check if it is a invalid directory
        if not os.path.isdir(args.dataDir) or len(os.listdir(args.dataDir)) != NUM_SHAPE_TYPES:
            err_exit("Invalid Data Directory provided...", 2)
        else: 
            DATA_DIR = args.dataDir if args.dataDir else DATA_DIR

    # Load the images 
    images, labels = load_data(DATA_DIR)

    # Split the training data into traingin and testing sets
    labels = tf.keras.util.to_categorical(labels)
    x_train, y_train, x_test, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled convolutional neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate convolutional neural network accuracy/performance
    model.evaluate(x_test, y_test, verbose=2)

    # Save model
    if args.saveModel:
        model.save(args.saveModel)
        print(f"Model saved on {args.saveModel}...")


def load_data(data_dir):
    """
    Load in the images in data_dir as an numpy array
    Inside data_dir are subdirectories where each shape has its own directory
    Inside the subdirectories are the images as .png files
    The name of the subdirectory will serve as the label for the image
    @param: data_dir(path): str
    @return: tuple([np.array], str)
    """
    # Holds the images data as np.arrays
    # and it's resepective label
    images, labels = [], []

    for subdirectory in os.listdir(data_dir):
        for file in os.listdir(os.path.join(data_dir, subdirectory)):
            # Read in the image
            image = cv2.imread(os.path.join(os.path.join(data_dir, subdirectory), file))
            # Add it to the images and labels lists
            images.append(image)
            labels.append(subdirectory)

    return (images, labels)


def get_model():
    """
    """
    # Describe the Convolutional Neural Network
    model = tf.keras.Sequential([

        # Convolutions

        # Pooling

        # Flatten units
        tf.keras.layers.Flatten(),

        # Input Layer

        # Avoid overfitting

        # Output layer - NUM_SHAPE_TYPES units
        tf.keras.layers.Dense(NUM_SHAPE_TYPES, activation="softmax")
    ])

    # Train the model
    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    # Run the main function
    main()


