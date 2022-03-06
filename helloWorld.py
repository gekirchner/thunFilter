#first try: print contents of a file

import os
import tfConfig

def writeFile(contents,file):
    file = open(file,"w") 
    file.write(contents) 
    file.close() 
    return

def appendOnFile(contents,file):
    file = open(file,"a") 
    file.write(contents) 
    file.close() 
    return
  
def readFile(file):
    f = open(file,"r") 
    return f.read() 

def removeFile(file):
    myAnswer = input("Delete file " + file +" ?")
    if myAnswer == "y":
        os.remove(file)
        print(file + " was REMOVED")
    else:
        print(file + " was NOT removed")
        return

appendOnFile("\"hello world\" from a file\n","testFile.txt")
print('modified by gitpod for test: testFileOnOtherDir')
for i in range(10):
    print( ' Counter: ', i )
fileContents=readFile("testFile.txt")
print(fileContents)

print('--- Now on other Dir ---')
if os.path.exists(tfConfig.dirOfFile):
    print('dir exists: ', tfConfig.dirOfFile)
else:
    print('creating ', tfConfig.dirOfFile)
    os.mkdir(tfConfig.dirOfFile)
appendOnFile("\"hello world\" from a file on tfConfig.dirOfFile\n", tfConfig.dirOfFile + "/testFileOnOtherDir.txt")
fileContents=readFile(tfConfig.dirOfFile + "/testFileOnOtherDir.txt")
print(fileContents)

print('--- Now write text from console input into file ---')
myInput = input("File entry: ")
appendOnFile(myInput + "\n", tfConfig.dirOfFile + "/testFileOnOtherDir.txt")
fileContents=readFile(tfConfig.dirOfFile + "/testFileOnOtherDir.txt")
print('contents of file:')
print(fileContents)

print(' --- Now remove optionally file ---')
myInput = input("Remove" + tfConfig.dirOfFile + "/testFileOnOtherDir.txt" + " ? ")
if myInput == "y":
        removeFile(tfConfig.dirOfFile + "/testFileOnOtherDir.txt")
else:
    print(tfConfig.dirOfFile + "/testFileOnOtherDir.txt" + " was NOT removed")
