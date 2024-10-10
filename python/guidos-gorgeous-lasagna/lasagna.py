"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return int(EXPECTED_BAKE_TIME - elapsed_bake_time)


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Preparation time in minutes

    :param number_of_layers: int - each layer takes 2 minutes to prep.
    :return: int - total prep time.

    A function that takes the number of layers and calculates how long prepping them takes in minutes.
    """

    return int(number_of_layers * 2)


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed bake time.

    :param number_of_layers: int - each layer takes 2 minutes to prep.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed bake time (in minutes) derived from preparation_time_in_minutes and bake_time_remaining.

    Function that takes the actual minutes the lasagna has been in the oven and the number of layers we prep as
    an argument and returns how many minutes the lasagna takes to make
    based on the preparation_time_in_minutes and bake_time_remaining.
    """

    return preparation_time_in_minutes(number_of_layers=number_of_layers) + elapsed_bake_time  
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining.)
