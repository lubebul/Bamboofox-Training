x = int('531F919', 16)
s = []
while x > 0:
    s.append(chr(ord('A')+x%26))
    x /= 26
print s
