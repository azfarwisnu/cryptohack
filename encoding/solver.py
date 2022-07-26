from pwn import * # pip install pwntools
import json
import base64
import binascii
from Crypto.Util.number import *
import codecs

#remote
r = remote('socket.cryptohack.org', 13377)

#json konvert skraaa
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

#loop soal
for x in range(100):
	received = json_recv()
	print(f"ini soal {received}")
	tipe = received["type"]
	enc = received["encoded"]
	encint = 0
	dec = ""
	tampungdec = []

	if tipe == "base64":
		dec = base64.b64decode(enc).decode("utf-8")
	elif tipe == "hex":
		dec = binascii.unhexlify(enc).decode("utf-8")
	elif tipe == "rot13":
		dec = codecs.decode(enc, "rot_13")
	elif tipe == "bigint":
		encint = int(enc,16)
		dec = long_to_bytes(encint).decode("utf-8")
	elif tipe == "utf-8":
		tampungdec = enc
		for data in enc:
			dec += chr(data)
	else:
		print("ngablue bang")

	to_send = {
    "decoded": dec
	}

	print(to_send)
	json_send(to_send)

r.interactive()






