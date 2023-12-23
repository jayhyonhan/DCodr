#Requires binary-to-number.py AND number-to-text.py
from sys import argv
from create_output import create_output
from binary_to_number import binary_to_num
from number_to_text import num_to_text
def binary_to_text(input_string):
    create_output(num_to_text(input_string=binary_to_num(input_string=input_string, do_return=True), do_return=True), "binary-to-text")
  

if __name__ == '__main__':
    input = ""
    for i in range(1, len(argv)):
        input += argv[i]
        if i != (len(argv)-1):
            input += " "
    binary_to_text(input)