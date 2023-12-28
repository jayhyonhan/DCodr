import datetime
from unicodedata import normalize
from os.path import exists
from os import makedirs
def create_output(output, cipher):
    if not(exists("../outputs/")):
        makedirs("../outputs/")
    file_path = ""
    now = datetime.datetime.now()
    file_path = ("../outputs/%s_%s.txt"%(cipher, now.strftime("%Y-%m-%d-%H-%M-%S-%f")))
    file = open(file_path, "w", encoding="utf-8")
    output = normalize('NFKD', output).encode('utf-8', 'ignore')
    file.write(str(output, encoding='utf-8'))
    file.close()

if __name__ == "__main__":
    create_output("test", "test")