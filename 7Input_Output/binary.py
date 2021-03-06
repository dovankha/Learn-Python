# with open(r'binary.txt', 'bw') as bin_file:
#     bin_file.write(bytes(range(17)))

# with open(r'binary.txt', 'br') as binFile:
#     for b in binFile:
#         print(b)

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 02 2D C0 1E

with open(r'binary2.txt', 'bw') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'big'))
    bin_file.write(x.to_bytes(4, 'little'))

# with open(r'binary2.txt', 'br') as bin_file:
#     e = int.from_bytes(bin_file(2), 'big')
#     f = int.from_bytes(bin_file(2), 'big')
#     g = int.from_bytes(bin_file(2), 'big')
#     h = int.from_bytes(bin_file(2), 'big')
#     i = int.from_bytes(bin_file(2), 'big')