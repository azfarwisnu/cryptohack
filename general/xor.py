from Crypto.Util.number import *
import binascii


'''
KUNCI1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2^KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2^KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
BENDERA ^ KUNCI1 ^ KUNCI3 ^ KUNCI2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
'''

key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
key2_key1 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
key2_key3 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1

key2 = key2_key1 ^ key1
key3 = key2_key3 ^ key2
combination_key = key1 ^ key2 ^ key3
flag_combine =  0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

flag = flag_combine ^ combination_key
print(long_to_bytes(flag))