import Frequency
from MinHeap import MinHeap
from Huffman import Huffman
import Encode
import Decode
import sys,time

def main() :
	while(1) :
		print("1.Compress\n2.Decompress\n3.Exit")
		choice = int(input("Enter Choice :"))
		if choice == 1 :
			fileName = input("Enter file Name: ")
			print("Encoding : ", fileName)
			frequencyTable = Frequency.frequencyTable(fileName)
			print(frequencyTable)
			huffmanObject = Huffman(frequencyTable)
			huffmanCodes = huffmanObject.huffman()
			Encode.encode(huffmanCodes, fileName)
		
			print("File Encoded as:"+fileName+".bv\n\n")

		elif choice == 2 :
			fileName = input("Enter file Name: ")
			print("decoding : ", fileName)
			Decode.decode(fileName)
			print("\nDecoded as "+fileName+"_new.txt")

		elif choice == 3 :
			print("Bye\n")
			return
		else :
			print("Invalid Choice\n")
				

if __name__ == "__main__" :
	st = time.time()
	main()
	print(time.time()-st)
