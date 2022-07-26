import binascii
from Crypto.Util.number import *
import base64

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
ords2 = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for x in ords:
	print(chr(int(x) ^ 0x32), end="")

print("\n")

for a in ords2:
	print(chr(a), end="")

print("\n")

data = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(binascii.unhexlify(data))
print(bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))

data2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
data2 = binascii.unhexlify(data2)
data2 = base64.b64encode(data2)
print(data2.split())

data3 = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
print(long_to_bytes(data3))

label = "label"
new_data = ""
for a in label:
	a = (ord(a) ^ 13)
	print(chr(a), end="")
