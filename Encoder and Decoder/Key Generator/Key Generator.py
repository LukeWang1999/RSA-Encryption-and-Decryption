import random
import eulerlib
import os.path
P = eulerlib.prime_numbers.primes(100000)
while P[0] < 40000:
    P.pop(0)
p1 = random.choice(P)
P.pop(P.index(p1))
p2 = random.choice(P)
n = p1*p2
P = []
Q = []
Euler = eulerlib.numtheory.lcm(p1-1, p2-1)
A = Euler
while A > 100000:
    A /= 10
P = eulerlib.prime_numbers.primes(int(A))
e = random.choice(P)
MMI = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or MMI(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
f= open("EncryptKey.txt","w+")
f.write('%d\r'%n)
f.write('%d\r'%e)
f.write('%d\r'%int(MMI(e,Euler)))
g = open("C:/path/EncryptKey.txt","w+")
g.write('%d\r'%n)
g.write('%d\r'%e)
f.close()
quit()


