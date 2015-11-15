# Buffer Overflow and x86
Slides
 * [Buffer Overflow](Buffer overflow and format string.pdf)
 * [x86](x86.pdf)

## How Buffer Overflow Happens?
 * use unsafe functions
 * copy data without boundary check

## Dangerous Functions
unsafe -> safe
 * gets -> fgets
 * sprintf -> snprintf
 * strcpy -> strncpy
 * strcat -> strncat
 * scanf -> don't use `%s` format

## Copy Data Without Boundary check
 * size rely on user input
  * Today's Vulnerable: [Magic](Magic)
 * off-by-one
```c
char buf[15];
memset(buf, 0, sizeof(buf));
strncat(buf, s, sizeof(buf)); // should be sizeof(buf)-1
```
 * integer overflow

## Control `eip` Strategy
 * shellcode
 * return to libc
 * return-oriented programming

## Stack Protector

### Stack Canary
How does it work?
 * protects stack by modifying function prologue and epilogue
 * after prologue: add 4 bytes random value(canary)
 * before epilogue: xor canary with original value

### Bypass Canary
 * leak canary
  * canaries are fixed after load
  * leak it and overwrite with correct value
 * skip canary

## Some gdb Tips
[GDB cheat sheet](GDB Cheat Sheet.pdf)
 * default: stack canary is turned-off!
 * break point at addr: `(gdb) b *0x80486c8`
 * examine stacks: `(gdb) x/40x $ebp`
 * examine frame: `(gdb) info frame`

## Today's Vulnerable
 * [Magic](Magic)
 * [ROP](ROP)
