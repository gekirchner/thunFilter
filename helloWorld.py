#first try: print contents of a file

#### Imports ####

import os
import tfConfig

#### Functions ####

def userInputNum(textToUser, minAllowed, maxAllowed):
    while True:
        userInput = input(textToUser)
        try:
            inputNum = int(userInput)
            if inputNum >= minAllowed and inputNum <= maxAllowed:
                break
        except ValueError:
            print("This is not a number. Please enter a valid number!")
    return inputNum

def writeFile(contents,file):
    file = open(file,"w") 
    file.write(contents) 
    file.close() 
    return

def appendOnFile(contents, file):
    file = open(file, "a") 
    file.write(contents) 
    file.close() 
    return
  
def readFile(file):
    f = open(file, "r") 
    return f.read() 

def removeFile(file):
    myAnswer = input("Delete file " + file +" ?")
    if myAnswer == "y":
        os.remove(file)
        print(file + " was REMOVED")
    else:
        print(file + " was NOT removed")
        return

#### Main Program ####

print()
print()
print("####### thunFilter running #######")
print()
print("######### Select Task #########")
print("### 1 = Some Tests          ###")
print("### 2 = Handle Filter File  ###")
print("### 3 = Exit                ###")
print("###############################")
print()

userInputNum("My selection: ", 1, 3)

appendOnFile("\"hello world\" from a file\n","testFile.txt")

#loop just for fun
for i in range(10):
    print( ' Counter: ', i, 'id: ', id(i) )
fileContents = readFile("testFile.txt")
print(fileContents)

print('--- Now on other Dir ---')
print('modified by gitpod for test:', tfConfig.fileToBeHandled, 'on Dir:', tfConfig.dirOfFile)
if os.path.exists(tfConfig.dirOfFile):
    print('dir exists: ', tfConfig.dirOfFile)
else:
    print('creating ', tfConfig.dirOfFile)
    os.mkdir(tfConfig.dirOfFile)
appendOnFile("\"hello world\" from a file on tfConfig.dirOfFile\n", tfConfig.fileToBeHandledWithDir)
fileContents = readFile(tfConfig.fileToBeHandledWithDir)
print(fileContents)

print('--- Now write text from console input into file ---')
myInput = input("File entry: ")
appendOnFile(myInput + "\n", tfConfig.fileToBeHandledWithDir)
fileContents = readFile(tfConfig.fileToBeHandledWithDir)
print('contents of file:')
print(fileContents)

print(' --- Now remove optionally file ---')
myInput = input("Remove" + tfConfig.fileToBeHandledWithDir + " ? ")
if myInput == "y":
        removeFile(tfConfig.fileToBeHandledWithDir)
else:
    print(tfConfig.fileToBeHandledWithDir + " was NOT removed")
