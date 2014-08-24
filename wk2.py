from Crypto.Cipher import AES

ct1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
k1 = "140b41b22a29beb4061bda66b6747e14"

ct2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
k2 = "140b41b22a29beb4061bda66b6747e14"

ct3 = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
k3 = "36f18357be4dbd77f050515c73fcf9f2"

ct4 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
k4 = "36f18357be4dbd77f050515c73fcf9f2"


def strxor(a, b):     # xor two strings of different lengths
	if len(a) > len(b):
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
	else:
		return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def add_padding(m):
	l = len(m[-1])
	if(l < 16):
		p = 16 - l
		a = hex(p)[2:]
		a = ("0" + a if len(a) == 1 else a).decode("hex")
		return m[:-1] + ((m[-1] + (a * p)),)
	else:
		assert(l == 16)
		return m + (("10" * 16).decode("hex"),)

def get_frags(m):
	frags = ()
	for i in range(len(m) / 16):
		frags = frags +  (m[:16],)
		m = m[16:]
	if(m):
		frags = frags + (m,)
	return frags

def funcAES_e(key,msg):
	return AES.new(key, AES.MODE_ECB).encrypt(msg)

def funcAES_d(key,msg):
	return AES.new(key, AES.MODE_ECB).decrypt(msg)

def	encript_cbc(key, msg):
	frags = add_padding(get_frags(msg))
	iv = Random.new().read(16)
	x = iv
	ct = ()
	for f in frags:
		c = funcAES_e(key,strxor(f,x))
		ct = ct + (c,)
		x = c
	return iv + "".join(ct)


def	decript_cbc(key, ct):
	assert(not (len(ct) % 16))
	frags = get_frags(ct)
	iv = frags[0]
	frags = frags[1:]
	m = ()
	for f in frags:
		d = strxor(funcAES_d(key,f),iv)
		m = m + (d,)
		iv = f
	return "".join(m)


def decript_ctr(key,ct):
	frags = get_frags(ct)
	iv = frags[0].encode("hex")
	frags = frags[1:]
	ivs = [funcAES_e(key,(hex(int(iv,16)+i)[2:-1]).decode("hex")) for i in range(len(frags))]
	assert(len(frags) == len(ivs))
	m = [strxor(frags[i],ivs[i]) for i in range(len(frags))]
	return "".join(m)

print(decript_cbc(k1.decode("hex"),ct1.decode("hex")))
print(decript_cbc(k2.decode("hex"),ct2.decode("hex")))
print(decript_ctr(k3.decode("hex"),ct3.decode("hex")))
print(decript_ctr(k4.decode("hex"),ct4.decode("hex")))