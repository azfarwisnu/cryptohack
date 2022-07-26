p = 26513
q = 32321

#p * u + q * v = gcd(p,q)

def extended_gcd(a,b):
	if a==0:
		return b,0,1
	else:
		gcd, x,y = extended_gcd(b%a,a)
		return gcd, y-(b//a)*x,x

print(extended_gcd(p,q))

print(min(11%6, 8146798528947%17))