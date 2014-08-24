import numbthy
hashtable = dict()
p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
G = numbthy.powmod(g,2**20,p)

print "after"
g_inverse = 1
def inverse(a,n):
	t = 0
	r = n
	newt = 1
	newr = a
	while newr != 0:
		quotient = r // newr
		t,newt = newt , t - quotient * newt
		r,newr = newr, r - quotient * newr
	if r > 1:
		print "a not invertible"
	if t < 0:
		t = t + n
	return t
if __name__ == "__main__":
	g_inverse = inverse(g,p)
	var = h
	print "q"
	for x1 in xrange(1,2**20+1):
		var *= g_inverse
		var = var%p
		hashtable[var] = x1
	print len(hashtable)
	result = 1
	for x2 in xrange(1,2**20+1):

		result *= G
		result %= p
		if result in hashtable:
			a = hashtable[result]
			print a + x2 * 2**20
			print a,x2
			break

	else:
		print "None found"
