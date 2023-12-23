from sys import argv
from create_output import create_output
def binary_to_num(input_string, do_return):
    output_string = ""
    temp = ""
    for i in temp:
        if i != '0' and i != '1':
            print("Not a binary number. Exiting...")
            exit()
    for i in range(len(input_string.split(" "))):
        output_string += str(int(input_string.split(" ")[i], base=2))
        if i != len(input_string.split(" "))-1:
            output_string += " "
    if do_return:
        return output_string
    create_output(output_string, "binary-to-num")
  

if __name__ == '__main__':
    input = ""
    for i in range(1, len(argv)):
        input += argv[i]
        if i != (len(argv)-1):
            input += " "
    binary_to_num(input, False)