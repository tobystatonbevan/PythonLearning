class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    def __init__(self,line,message="Bad line."):
        self.line = line
        self.message = message
        super().__init__(self.message)


class FileEmpty(StudentsDataException):
    def __init__(self,file,message="File exists but is empty"):
        self.file = file
        self.message = message
        super().__init__(self.message)

from os import strerror

fileOpen = False
fileName = input("Enter file name: ")

while fileOpen == False:
    try:
        file = open("C:\\Users\\User\\Documents\\GitHub\\Python-Learning\\Associate Level\\"+fileName,'rt')
        fileOpen = True
    except Exception as e:
        print(f"Failed: {strerror(e.errno)}")
        fileName = input("Enter file name: ")
    
line = file.readline()
sanitisedLine = []
try:
    if line == "":
        raise FileEmpty(file)
except FileEmpty as fe:
    print(f"Failed: {fe.message}")

while line != "":
    try: 
        sanitisedLine.append([i for i in line.strip().split(" ") if i != ""])
        line = file.readline()
    except:
        raise BadLine(line)

finalResults = {}

for i in sanitisedLine:
    name = i[0]+" "+i[1]
    try:
        grade = float(i[2])
    except ValueError:
        raise BadLine(line)
    if name not in finalResults:
        finalResults[name] = grade
    else:
        finalResults.update({name:finalResults[name]+grade})

for i in finalResults:
    print(f"{i} {finalResults.get(i)}")