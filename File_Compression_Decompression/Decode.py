import ast


frequencyTable = None
data = ""
bitString=""
extractedData=""

def readFile(fileName) :
    fileDiscriptor = open(fileName, "rb")
    frequencyTable=fileDiscriptor.readline().decode().rstrip()
    frequencyTable = ast.literal_eval(frequencyTable)
    data = fileDiscriptor.readline()
    return data

def removePadding() :
    padding = -int(bitString[:8],2)
    bitString = bitString[8:padding]

def extractDataAsBits() :
    for character in data :
        characterAsBit = bin(character)[2:].rjust(8,'0')
        bitString = bitString + characterAsBit
	
def writeData(fileName) :
    fileName = fileName.split('.')
    fileName = fileName[0]+"_new."+fileName[1]
    fd = open(fileName,"w+")
    fd.write(extractedData)

def decodeBitString() :
    code = ''
    for bit in bitString :
        code=code+bit	
        for key, value in frequencyTable.items():
            if code == value :
                extractedData = extractedData + key
                code = ""
                break

def decode(fname) :
    readFile(fname)
    extractDataAsBits()
    removePadding()
    decodeBitString()	
    writeData(fname)
