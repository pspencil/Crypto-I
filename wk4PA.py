import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='
base = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
                  # Print response code
            if e.code == 404:
                print "We got: %d" % e.code 
                return True # good padding
            return False # bad padding

def frags(m):
    l = []
    while m:
        l.append(m[:32])
        m = m[32:]
    assert len(l[-1]) == 32
    return l
def generate_padding(bytes):
    pad = ""
    for x in range(bytes):
        pad += chr(bytes)
    return pad


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return a[:-len(b)] + "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[-len(b):], b)])
    else:
        return b[:-len(a)] + "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[-len(a):])])

possible = [ord(' ')]+range(ord('a'),ord('z')+1)+range(ord('A'),ord('Z')+1)
if __name__ == "__main__":
    try:
        po = PaddingOracle()
        message = ""
        global decoded
        l = [x.decode("hex") for x in frags(base)]
        for blk in range(3):
            decoded = ""
            for bytes in range(16):
                if blk == 0 and bytes <9:
                    decoded = '\x09'+decoded
                    continue
                for attempt in possible:
                    message_byte = chr(attempt)
                    decoded_new = message_byte + decoded
                    new_l = [x for x in l[:4-blk]]
                    new_l[-2] = strxor(strxor(new_l[-2],decoded_new),generate_padding(bytes+1))
                    ct = "".join(new_l)
                    if po.query(ct.encode("hex")):

                        decoded = message_byte+decoded
                        break
                else:
                    print "Error"
                print decoded
            message = decoded + message
        print message
    except KeyboardInterrupt:
        pass



















