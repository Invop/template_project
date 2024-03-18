from app.io import input, output
import pandas as pd

def main():
    input_result1 = input.input_text()
    output.print_text(input_result1)
    txt_file = "data/test.txt"
    input_result2 = input.read_file_builtin(txt_file)
    output.print_text(input_result2)
    csv_file = "data/test.csv"
    input_result3 = input.read_file_pandas(csv_file)
    output.print_text(input_result3)

    output.write_file_builtin("data/output1.txt", input_result1)
    output.write_file_builtin("data/output2.txt", input_result2)

    data = pd.DataFrame({
        'Column1': ['Item1', 'Item2', 'Item3'],
        'Column2': ['Item4', 'Item5', 'Item6']
    })
    output.write_file_pandas('data/output3.csv', data)


if __name__ == "__main__":
    main()
