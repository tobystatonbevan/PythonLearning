import os

def find(path, dir):
    try:
        os.chdir(path)
    except:
        os.chdir("\\")
    
    currentDir = os.getcwd()

    for i in os.listdir(currentDir):
        if i == dir:
            print(currentDir+"\\"+i)
        find(currentDir+"\\"+i,dir)

find("Associate Level\\tree","python")