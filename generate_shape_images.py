"""
Generates the dataset of 32x32 images of Shapes
Saves the images in a DATA_DIR
"""

# Standard Libraries
import os
import sys
import shutil
import random
from random import randint

from PIL import Image, ImageDraw


# Image dimension - 32x32
WIDTH, HEIGHT = 32, 32
# Data Directory
DATA_DIR = "Data"

# Colors
WHITE = (255,255,255)


def main():

    # Remove all files in Data Directory
    clear_data_dir(DATA_DIR)
    # Create Subdirectories in DATA_DIR
    setup_data_dir([
        "Circle",
        "Triangle",
        "Square",
        "Rectangle"
    ])

    if len(sys.argv) == 2:
        try:
            N = int(sys.argv[1])
        except ValueError:
            print("Usage: python generate_shape_images.py [int]")
            sys.exit(1)

    # Generate the Images
    try:
       generate(N)
    except NameError:
        generate()

    print("Dataset Complete! :)")


def generate(N=1000):
    """
    Generates the images of shapes
    Dataset will be used to train a neural network model 
    to Classify Shapes
    """
    print("Generating Circle Data...")
    generate_circle(N)

    print("Generating Triangle Data...")
    generate_triangle(N)

    print("Generating Square Data...")
    generate_square(N)

    print("Generating Rectangle Data...")
    generate_rectangle(N)


def generate_circle(n):
    """
    Generates 'n' images of randomly generated circles
    Saves it to a subdirectory within the DATA_DIR
    @param: n: int
    @return: None
    """

    # Padding for filenames
    padding = len(str(n))

    for i in range(n):

        # Generate a random radius
        r = randint(0, WIDTH - 1)
        # Coordinates of the top-left corner of the bounding box
        x, y = randint(0, WIDTH - r - 1), randint(0, HEIGHT - r - 1)

        # Create a new Image
        image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        draw = ImageDraw.Draw(image)

        # Draw the circle with a random outline color
        draw.ellipse([x, y, x + r, y + r], outline=random_color())

        # Filepath of the image
        image_path = os.path.join(os.path.join(DATA_DIR, "Circle"), f"{str(i).zfill(padding)}.png") 
        # Save the image having 'i' as its filename formatted to n's number of digits
        image.save(image_path)
        print(f"Saved image to {image_path}...")


def generate_triangle(n):
    """
    Generates 'n' images of randomly generated triangles
    Saves it to a subdirectory within the DATA_DIR
    @param: n: int
    @return: None
    """

    # Padding for filenames
    padding = len(str(n))

    for i in range(n):

        # Generate random coordinates of the 3 vertices of the triangle
        while True:
            v1 = (randint(0, WIDTH - 1), randint(0, HEIGHT - 1))
            v2 = (randint(0, WIDTH - 1), randint(0, HEIGHT - 1))
            v3 = (randint(0, WIDTH - 1), randint(0, HEIGHT - 1))
            if len(set((v1, v2, v3))) == 3:
                break

        # Create a new Image
        image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        draw = ImageDraw.Draw(image)

        # Draw the triangle with a random outline color
        draw.polygon([v1, v2, v3], outline=random_color())

        # Filepath of the image
        image_path = os.path.join(os.path.join(DATA_DIR, "Triangle"), f"{str(i).zfill(padding)}.png") 
        # Save the image having 'i' as its filename formatted to n's number of digits
        image.save(image_path)
        print(f"Saved image to {image_path}...")


def generate_square(n):
    """
    Generates 'n' images of randomly generated squares
    Saves it to a subdirectory within the DATA_DIR
    @param: n: int
    @return: None
    """

    # Padding for filenames
    padding = len(str(n))

    for i in range(n):
        # Generate a random side length
        side = randint(0, WIDTH - 1)
        # Coordinates of the top-left corner of the square
        x, y = randint(0, WIDTH - side - 1), randint(0, HEIGHT - side - 1)

        # Create a new Image
        image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        draw = ImageDraw.Draw(image)

        # Draw the square with a random outline color
        draw.rectangle([x, y, x + side, y + side], outline=random_color())

        # Filepath of the image
        image_path = os.path.join(os.path.join(DATA_DIR, "Square"), f"{str(i).zfill(padding)}.png") 
        # Save the image having 'i' as its filename formatted to n's number of digits
        image.save(image_path)
        print(f"Saved image to {image_path}...")
  

def generate_rectangle(n):
    """
    Generates 'n' images of randomly generated rectangles
    Saves it to a subdirectory within the DATA_DIR
    @param: n: int
    @return: None
    """

    # Padding for filenames
    padding = len(str(n))

    for i in range(n):
        # Generate 2 random sides that must not be equal to each other
        while True:
            s1, s2 = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
            # if both numbers are unique 
            # and their absolute difference is at least 5; break the loop
            if s1 != s2 and abs(s1 - s2) > 4:
                break

        # Coordinates of top-left corner of the square
        x, y = randint(0, WIDTH - s1 - 1), randint(0, HEIGHT - s2 - 1)

        # Create a new Image
        image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
        draw = ImageDraw.Draw(image)

        # Draw the rectangle with a random outline color
        draw.rectangle([x, y, x + s1, y + s2], outline=random_color())

        # Filepath of the image
        image_path = os.path.join(os.path.join(DATA_DIR, "Rectangle"), f"{str(i).zfill(padding)}.png") 
        # Save the image having 'i' as its filename formatted to n's number of digits
        image.save(image_path)
        print(f"Saved image to {image_path}...")
    

def clear_data_dir(directory):
    """
    Removes all contents of directory
    @param: directory(path): str
    @return: None
    """
    # Remove contents of data_directory and directory itself
    shutil.rmtree(directory)
    # Recreate the directory
    os.mkdir(directory)


def random_color(max=230):
    """
    Returns a randomly generated tuple of RGB values
    @param: max: int
    @return: tuple: (R, G, B)
    """
    return (
        randint(0,max),
        randint(0,max),
        randint(0,max)
    )


def setup_data_dir(directories):
    """
    Setups the DATA_DIR by creating the directories for each shape
    @param: list: [str]
    @return: None
    """
    for directory in directories:
        os.mkdir(os.path.join(DATA_DIR, directory))


if __name__ == "__main__":
    # Run the main function
    main()
