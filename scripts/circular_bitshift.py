from sys import argv
from create_output import create_output
from binary_to_number import binary_to_num
from binary_to_text import binary_to_text
def circular_bitshift(input_string: str, output_type):
    output_string = ""
    output_string2 = str(output_string)
    tempS = ""
    for i in range(len(input_string)):
        if input_string[i] != " ": # remove all spaces
            tempS += input_string[i]
    input_string = tempS
    for i in input_string:
        if i != '0' and i != '1':
            print("Not a binary number. Exiting...")
            exit()
    tempS = ""
    tempL = []
    for block in range(2, 33):
        if len(input_string)%block == 0:
            for offset in range(1, block):
                output_string += "block %d, offset %d:  "%(block, block-offset)
                # Splitting the input into chunks
                for i in range(1, len(input_string)+1):
                    if i%block == 0:
                        tempL.append(input_string[i-block:i])
                # Offset magic
                for i in range(len(tempL)):
                    tempS = tempL[i][0:offset]
                    tempL[i] = tempL[i][offset:block]
                    tempL[i] += tempS
                    tempS = ""
                for i in range(len(tempL)):
                    output_string += tempL[i]
                    output_string2 += tempL[i]
                    if i != len(tempL)-1:
                        output_string += " "
                        output_string2 += " "
                output_string += "\n\n"
                output_string2 += "\n"
                tempL = []
    output_string = output_string.rstrip()
    output_string2 = output_string2.rstrip()
    if output_type == "binary":
        create_output(output_string, "circular_bitshift_binary")
    if output_type == "text":
        tempS = ""
        tempL = output_string2.split("\n")
        for i in range(len(tempL)): tempL[i] = binary_to_text(tempL[i])
        print(tempL)
        output_string2 = "" # reset output_string2
        for i in range(len(tempL)): # loop through tempL
             # basically add the "block %d, offset %d:  " part to output_string2
             output_string2 += output_string.split("\n\n")[i].split("  ")[0] + "  " + tempL[i] + "\n\n"
        create_output(output_string2, "circular_bitshift_text") # create an output file
    if output_type == "number":
        tempS = ""
        tempL = []
        for i in range(len(output_string2.split("\n"))):
            tempS = str(output_string2.split("\n")[i])
            tempL.append(binary_to_num(tempS))
        output_string2 = ""
        for i in range(len(tempL)):
             output_string2 += output_string.split("\n\n")[i].split("  ")[0] + "  " + tempL[i] + "\n\n"
        create_output(output_string2, "circular_bitshift_num")

if __name__ == '__main__':
    input = ""
    for i in range(2, len(argv)):
        input += argv[i]
        if i != (len(argv)-1):
            input += " "
    circular_bitshift(input, argv[1])