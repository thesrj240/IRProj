import hashlib
a = 'tamatar'
b = 'tamatar'
hashing1 = hashlib.md5(a)
hash1 = hashing1.digest()
hashing2 = hashlib.md5(b)
hash2 = hashing2.digest()
print(hash1,hash2)