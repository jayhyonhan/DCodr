from sys import argv
from create_output import create_output
def num_to_text(input_string,do_return):
    output_string = ""
    temp = ""
    for i in temp:
        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
            print("Not a denary(base 10) number. Exiting...")
            exit()
    for i in range(len(input_string.split(" "))):
        output_string += str(chr(int(input_string.split(" ")[i])))
    if do_return:
        return output_string
    create_output(output_string, "num-to-text")
  

if __name__ == '__main__':
    input = ""
    for i in range(1, len(argv)):
        input += argv[i]
        if i != (len(argv)-1):
            input += " "
    num_to_text(input, False)