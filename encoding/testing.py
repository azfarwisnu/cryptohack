from Crypto.Util.number import *
import codecs
import binascii

b = '0x636f6d706f7365645f6661726d735f6974756e6573'
b = int(b,16)
print(b)

print(long_to_bytes(b).decode("utf-8"))
rot13 = b'ybtvpny_sberire_flabcfvf'.decode("utf-8")
rot13 = codecs.decode(rot13, "rot_13")
print(rot13)

hexval = binascii.unhexlify("706c61696e5f74686f755f75726765")
print(hexval)