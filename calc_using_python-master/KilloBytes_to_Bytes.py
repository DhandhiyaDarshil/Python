# Function to calculates the bits 
def Bits(kilobytes) :

	# calculates Bits - 1 kilobytes(s) = 8192 bits 
	Bits = kilobytes * 8192
	return Bits

# Function to calculates the bytes 
def Bytes(kilobytes) :

	# calculates Bytes - 1 KB = 1024 bytes 
	Bytes = kilobytes * 1024
	return Bytes

# Driver code
if __name__ == "__main__" :

	kilobytes = 1

	print(kilobytes, "Kilobytes =", 
	Bytes(kilobytes) , "Bytes and", 
	Bits(kilobytes), "Bits")