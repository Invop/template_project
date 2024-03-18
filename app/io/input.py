import pandas as pd


def input_text():
    """
    This function is used for inputting text from console.
    """
    text = input("Please enter some text: ")
    return text


def read_file_builtin(filename):
    """
    This function is used for reading from file using built-in Python features.
    """
    with open(filename, 'r') as file:
        data = file.read()
    return data


def read_file_pandas(filename):
    """
    This function is used for reading from a CSV file using pandas library.
    """
    data = pd.read_csv(filename)
    return data
