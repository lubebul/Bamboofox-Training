# a1, a2 = 0x5c($esp), 0x60($esp) = 0x80486d0, 0x80486ca
a1 = [int('0x010e1221', 16), int('0x0c251c0c', 16),
      int('0x022e081b', 16), int('0x280c140d', 16),
      int('0x2a041d0a', 16), int('0x2b0c2010', 16),
      int('0x10071d02', 16), int('0x59061e0c', 16),
      int('0x59000e4a', 16)]
a2 = [int('0x63637363', 16), int('0x1221000', 16)]

# 0x5c, 0x4c -> len(A2), len(A1)
A1, A2 = [], []
for i in range(len(a1)):
    for j in range(4):
        x = (a1[i] >> (8*j)) & 0xff
        if x != 0:
            A1.append(x)
        else:
            break
for i in range(len(a2)):
    for j in range(4):
        x = (a2[i] >> (8*j)) & 0xff
        if x != 0:
            A2.append(x)
        else:
            break
print ''.join([chr(A1[i] ^ A2[i % len(A2)]) for i in range(len(A1))])
