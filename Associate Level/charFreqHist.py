from os import strerror

fileName = input("Enter the file name: ")
fileOpen = False
fileContentFreq = {}

while fileOpen == False:
    try:
        file = open("C:\\Users\\User\\Documents\\GitHub\\Python-Learning\\Associate Level\\"+fileName,'rt')
        fileOpen = True
    except Exception as e:
        print(f"Failed: {strerror(e.errno)}")
        fileName = input("Enter the file name: ")

line = file.readline()
while line != '':
    for n in line.lower().strip(): 
        if n not in fileContentFreq:
            fileContentFreq[n] = 1
        else:
            fileContentFreq.update({n:fileContentFreq[n]+1})
    line = file.readline()

for i in fileContentFreq:
    print(f"{i} -> {fileContentFreq[i]}")
print(fileContentFreq)