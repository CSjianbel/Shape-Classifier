"""
Creates a shape classifier model
"""
# Standard libraries
import os

# 3rd party libraries
import tensorflow as tf
import numpy as np
import cv2 

from sklearn.model_selection import train_test_split

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
    """
    """
    pass


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


