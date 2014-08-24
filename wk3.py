from Crypto.Hash import SHA256

video = open("6 - 1 - Introduction (11 min).mp4","r+")
def hash(a):
	h = SHA256.new()
	h.update(a)
	return h.hexdigest().decode("hex")

raw = video.read()

def block(a,n): # n = 1,2,3,4... 
	return a[(n-1)*1024:n*1024]

pad = ""
for blk in range(len(raw)//1024+1,0,-1):
	PT = block(raw,blk) + pad
	pad = hash(PT)

print(pad.encode("hex"))

