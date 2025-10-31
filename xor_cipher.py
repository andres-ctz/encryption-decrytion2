import random
p = input(str("texto: "))
k = [random.randint(0,1) for _ in range(len(p))] 
r = ''.join([chr(ord(c) ^ k[i % len(k)]) for i, c in enumerate(p)])
d = ''.join([chr(ord(c) ^ k[i % len(k)]) for i, c in enumerate(r)])
print("llave: ",k,"\ncifrado:",r,"\ndecifrado:",d)

