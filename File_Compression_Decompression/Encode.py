

def convertFile(fname,huffmanCodes) :
    data = open(fname, "r")
    data=data.read()
    encodedData = ""
    for i in data :
        encodedData  = encodedData+huffmanCodes[i]
    return encodedData

def padFile(data) :
    extra = 8 - len(data)%8
    for i in range(extra) :
        data = data + "0"
    padding  = "{0:08b}".format(extra)
    data = padding + data
    return data

def convertToBits(data) :
    byteArray = bytearray()
    while(data != "") :
        byteArray.append(int(data[:8],2))
        data = data[8:]
    return byteArray

def encode(huffmanCodes,fname) :
    encodedData = convertFile(fname,huffmanCodes)
    encodedData = padFile(encodedData)
    byteArray = convertToBits(encodedData)
    encodedFile = open(fname+".bv","wb+")
    huffmanCodes = str(huffmanCodes).encode()
    encodedFile.write(huffmanCodes)
    encodedFile.write("\n".encode())
    encodedFile.write(bytes(byteArray))
    encodedFile.close()
