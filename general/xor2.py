from Crypto.Util.number import *
import binascii
import string

data = binascii.unhexlify("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
flag = ""

for a in range(256):
	for b in data:
		xor  =  chr(a ^ b)
		flag += xor
	if "crypto" in flag:
		print(flag)
		break
