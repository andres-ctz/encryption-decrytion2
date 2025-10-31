import random
p = input(str("texto: "))
import random
k = [random.randint(0,1) for _ in range(len(p))] 
r = ''.join([chr(ord(c) ^ k[i % len(k)]) for i, c in enumerate(p)])
print("llave: ",k)
print("cifrado: ",r)
