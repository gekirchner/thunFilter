#first try: print contents of a file

def writeFile(contents,file):
    file = open(file,"w") 
    file.write(contents) 
    file.close() 
    return
    
def readFile(file):
    f = open(file,"r") 
    return f.read() 

writeFile("\"hello world\" from a file","testFile.txt")
print('2nd again locally modified for test')
for i in range(10):
    print( ' Counter: ', i )
fileContents=readFile("testFile.txt")
print(fileContents)
