# Python Module ciphersuite
import os
import sys
from binascii import hexlify, unhexlify
import random 


def enc(x, e, n):
    int_x = int.from_bytes(x, "little")
    y = pow(int_x,e,n)
    return hexlify(y.to_bytes(256, 'little'))

def dec(y, d, n):
    int_y = int.from_bytes(unhexlify(y), "little")
    x = pow(int_y,d,n)
    return x.to_bytes(256, 'little')


ciphertext = "3333363431383738353832653735333635353237363965323832636236613366666532636135323362613163333265656633343135663136396135666161363162386336663364386165653930666462363833373964613363336438633962303336326536323439353737613265346138653432366531343838396462313364333963623864396539643438623232623835336637326337646164363035623130643634393634376639333332336361636330373032356461343062393139623461373238646432363962626164333130653862353166353937653338616431363936633763333065616339653265613863333164323936323139346138303130313030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030303030"
e = 65537
n = 359538626972463181545861038157804946723595395788461314546860162315465351611001926265416954644815072042240227759742786715317579537628833244985694861278987734749889467798189216056224155419337614971247810502667407426128061959753492358794507740889756004921248165191531797899658797061840615258162959755571367021109

pRange=2**512;
qRange=2**513;


def isPrime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n!=int(n):
        return False
    n=int(n)
    #Miller-Rabin test for prime
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
        
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
  
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True


def search(n):
    p_start = 2**512
    q_start = 2**513

    if p_start % 2 == 0:  # Make sure we start from an odd number
        p_start += 1
    if q_start % 2 == 0:
        q_start += 1

    for p in range(p_start, 2**513, 2):  # Iterate over odd numbers
        if not isPrime(p):
            continue

        if n % p == 0:  # If p is a divisor of n
            q = n // p
            if q >= q_start and isPrime(q):
                return p, q

    return None, None
    	    	  

p,q = search(n)


d = pow(e, -1, ((p-1)*(q-1)))

flag = dec(unhexlify(ciphertext),d,n)
print(flag)

sys.stdout.flush()