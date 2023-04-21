#CH9 PE3
#part1 : create the cipher pickle files

import random
import pickle
import pprint

list_a = [chr(i) for i in range(33,127)]
list_b = list_a[:]
random.shuffle(list_b)

encrypt_dt = dict(zip(list_a,list_b))
decrypt_dt = dict(zip(list_b,list_a))

print("Encryption Table")
pprint.pprint(encrypt_dt)

print("Decryption Table")
pprint.pprint(decrypt_dt)


outfile = open('encrypt.dat','wb')
pickle.dump(encrypt_dt,outfile)
outfile.close()

outfile = open('decrypt.dat','wb')
pickle.dump(decrypt_dt,outfile)
outfile.close()
