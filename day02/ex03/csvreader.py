#context manager
class CsvReader():
    def __init__(self, name, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.name = name
        self.file = name
        self.lenght = 0
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file =  open(self.name, "r") #Test if it finds the file
            return self
        except:
            print("File not found")
            exit()

    def file_lenght(self):
        i = 1
        line = ""
        while line != "":
            line = self.file.readline()
            print(line)
            i += 1
        self.lenght = i

    def getdata(self):
        data = ""
        i = 0
        self.file_lenght()
        for line in self.file:
            if i >= self.skip_top:
                data += line + "\n"
            i += 1
        return data

    def getheader(self):
        if self.header == False:
            return None
        else:
            return self.file.readline()

    def __exit__(self, type, value, traceback):
        self.file.close()

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(data)
        print(header)
