from Crypto.Cipher import AES

def funcAES_e(key,msg):
	return AES.new(key, AES.MODE_ECB).encrypt(msg)

def funcAES_d(key,msg):
	return AES.new(key, AES.MODE_ECB).decrypt(msg)

def padding(key):
	while len(key) % 16 != 0:
		key += '\x00'
	return key
mode = raw_input("Do you want to encrypt or decrypt? ")
if mode.lower() == "e":
	pt = raw_input("What to encrypt and key? space delimited ")
	key = pt.split(' ')[1]
	pt = pt.split(' ')[0]
	print funcAES_e(padding(key),padding(pt)).encode("hex")
if mode.lower() == 'd':
	ct = raw_input("What to decrypt and key? space delimited ")
	key = ct.split(' ')[1]
	ct = ct.split(' ')[0].decode('hex')
	print funcAES_d(padding(key),ct)