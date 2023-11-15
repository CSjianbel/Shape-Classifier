# Standard Libraries
import os
import sys
import shutil
import math
import random


def vector_subtraction(p1, p2):
    """
    Returns the difference between 2 vectors
    p1 and p2 are vectors in 2d space
    @param: tuple: (int,int), tuple: (int,int) 
    @return: tuple(int, int)
    """
    return (
        p1[0] - p2[0],
        p1[1] - p2[1]
    )


def pythagorean(v):
    """
    Pythagorean Theorem: c = sqrt(a^2 + b^2)
    'v' is a vector in 2d space
    @param: tuple: (int,int)
    @return: float
    """
    return math.sqrt(
        v[0] ** 2 + v[1] ** 2
    )


def vector_difference(p1, p2):
    """
    Wrapper for pythagorean and vector_subtraction functions
    Returns the magnitude of the difference of p1 and p2 vectors.
    p1 and p2 are vectors in 2d space
    @param: tuple: (int,int), tuple: (int,int)
    @return: float
    """
    return pythagorean(vector_subtraction(p1, p2))


def verify_vertices(v1, v2, v3):
    """
    Verifies if the vertices are all distinct from each other 
    and their differences are all greater than 10.0
    v1, v2 and v3 are vectors in 2d space
    @param: tuple: (int,int), tuple: (int,int), tuple(int,int)
    @return: Boolean
    """
    return (
        len(set((v1, v2, v3))) == 3 
        and vector_difference(v1, v2) > 10.0
        and vector_difference(v2, v3) > 10.0
        and vector_difference(v1, v3) > 10.0
    )


def clear_data_dir(directory):
    """
    Removes all contents of directory
    @param: directory(path): str
    @return: None
    """
    # Remove contents of data_directory and directory itself
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    # Recreate the directory
    os.mkdir(directory)


def setup_data_dir(data_dir, directories):
    """
    Setups the DATA_DIR by creating the directories for each shape
    @param: str(path), list: [str]
    @return: None
    """
    for directory in directories:
        os.mkdir(os.path.join(data_dir, directory))


def random_color(max=230):
    """
    Returns a randomly generated tuple of RGB values
    @param: max: int
    @return: tuple: (R, G, B)
    """
    return (
        random.randint(0, max),
        random.randint(0, max),
        random.randint(0, max)
    )


def err_exit(msg="", code=404):
    """
    Prints an error message and exits the program
    @param: msg: str, code: int
    @return: None
    """
    print(msg)
    sys.exit(code)