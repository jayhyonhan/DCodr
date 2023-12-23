from sys import argv
from create_output import create_output
def caesar(input_string, allowed_string):
    j = 0
    i = 0
    temp = []
    new = 0
    output_string = ""
    for i in range(len(allowed_string)):
        for j in range(len(input_string)):
            new = allowed_string.find(input_string[j]) + 1
            if len(allowed_string) <= new:
                new = new-len(allowed_string)
            temp = list(input_string)
            temp[j] = allowed_string[new]
            input_string = ""
            for k in temp:
                input_string += str(k)
            output_string += input_string[j]
        output_string += "\n\n"
    create_output(output_string, "caesar")

if __name__ == '__main__':
    caesar(argv[1], argv[2])