import random

dat = b'\x7fELF\x01\x01\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x01\x00\x00\x00\x91\x80\x04\x084\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004\x00 \x00\x02\x00(\x00\x00\x00\x00\x00\x01\x00\x00\x00t\x00\x00\x00t\x80\x04\x08t\x80\x04\x08G\x00\x00\x00G\x00\x00\x00\x07\x00\x00\x00\x00\x10\x00\x00\x01\x00\x00\x00\xbb\x00\x00\x00\xbb\x90\x04\x08\xbb\x90\x04\x080\x00\x00\x000\x00\x00\x00\x06\x00\x00\x00\x00\x10\x00\x00\x89\xc8\x808\x00t\x03@\xeb\xf8\x89\xc2)\xca\xb8\x04\x00\x00\x00\xbb\x01\x00\x00\x00\x89\xc9\xcd\x80\xc3\xb9\xbb\x90\x04\x08\xe8\xd9\xff\xff\xff\xbb\x00\x00\x00\x00\xb8\x01\x00\x00\x00\xcd\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Can you find the flag?\n\x00easyctf{abcdef__123456}\x00'

def gen_flag(length):
	x = ''
	for i in range(0,length):
		x += random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQSTUVWXYZ0123456789'))
	return x

output = bytearray(dat[:0xdb]) 
flag = gen_flag(14)
output.extend(flag.encode('utf-8'))
output.extend(dat[0xdb+14:])

print(output)
#o = open(flag, 'wb')
#o.write(output)
#o.close()
