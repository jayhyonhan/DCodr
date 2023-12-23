import datetime
def create_output(output, cipher):
    file_path = ""
    now = datetime.datetime.now()
    file_path = ("./outputs/%s_%s.txt"%(cipher, now.strftime("%Y-%m-%d-%H-%M-%S-%f")))
    file = open(file_path, "w")
    file.write(output)
    file.close()

if __name__ == "__main__":
    create_output("test", "test")