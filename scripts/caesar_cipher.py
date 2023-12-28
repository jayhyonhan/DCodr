from sys import argv
from create_output import create_output
def caesar(input_string:str, allowed_string:str):
    j = 0
    i = 0
    tempS = ""
    new = 0
    output_string = ""
    for k in range(len(allowed_string)):
        for i in range(len(input_string.split(" "))):
            tempS = input_string.split(" ")[i]
            for j in range(len(tempS)):
                new = allowed_string.find(tempS[j]) + k
                if new > len(allowed_string)-1:
                    new -= len(allowed_string)
                output_string += allowed_string[new]
            output_string += " "
        output_string += "\n\n"

    return output_string

if __name__ == '__main__':
    input = ""
    for i in range(2, len(argv)):
        input += argv[i]
        if i != (len(argv)-1):
            input += " "
    create_output(caesar(input, argv[1]), "caesar")