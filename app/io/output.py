def print_text(text):
    """
    This function is used for printing out text to console.
    """
    print(text)


def write_file_builtin(filename, text):
    """
    This function is used for writing to a file using built-in Python features.
    """
    with open(filename, 'w') as file:
        file.write(text)

def write_file_pandas(filename, dataframe):
    """
    This function is used for writing to a CSV file using pandas library.
    """
    dataframe.to_csv(filename, index=False)
