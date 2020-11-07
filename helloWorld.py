#first try: print contents of a file

import os
from pathlib import Path

def writeFile(contents,file):
    file = open(file,"w") 
    file.write(contents) 
    file.close() 
    return
    
def readFile(file):
    f = open(file,"r") 
    return f.read() 

writeFile("\"hello world\" from a file","testFile.txt")
print('modified by gitpod for test: testFileOnOtherDir')
for i in range(10):
    print( ' Counter: ', i )
fileContents=readFile("testFile.txt")
print(fileContents)

print('--- Now on other Dir ---')
#dirOfFile = '/workspace/dirOfTestFile'
myHomeDir = str(Path.home())
dirOfFile = myHomeDir + '/dirOfTestFile'
if os.path.exists(dirOfFile):
    print('dir exists: ', dirOfFile)
else:
    print('creating ', dirOfFile)
    os.mkdir(dirOfFile)
writeFile("\"hello world\" from a file on dirOfFile", dirOfFile + "/testFileOnOtherDir.txt")
fileContents=readFile(dirOfFile + "/testFileOnOtherDir.txt")
print(fileContents)
