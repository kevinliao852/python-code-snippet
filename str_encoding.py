"""
bytes decoding & string encoding 
"""

a = bytes('你', 'big5')

print(bin(a[0]))
print(a)

s = a.decode('big5')
print(s)

c = b.encode('big5')
print(c)
