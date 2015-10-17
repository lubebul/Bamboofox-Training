# Crack Linux Still-Egg-Level Reversing
Given [an executable](eggReverse2), want you to crack it.

## Analysis
```
$ objdump -d eggReverse2
...
080484fd <check_permission>:
 80484fd:	55                   	push   %ebp
 80484fe:	89 e5                	mov    %esp,%ebp
 8048500:	53                   	push   %ebx
 8048501:	83 ec 64             	sub    $0x64,%esp
 8048504:	8b 45 08             	mov    0x8(%ebp),%eax
 8048507:	89 45 a4             	mov    %eax,-0x5c(%ebp) // -> a1 = 0x80486d0
 804850a:	8b 45 0c             	mov    0xc(%ebp),%eax
 804850d:	89 45 a0             	mov    %eax,-0x60(%ebp) // -> a2 = 0x80486ca
 8048510:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
 8048516:	89 45 f4             	mov    %eax,-0xc(%ebp)
 8048519:	31 c0                	xor    %eax,%eax
 804851b:	8d 45 b8             	lea    -0x48(%ebp),%eax
 804851e:	89 44 24 04          	mov    %eax,0x4(%esp)
 8048522:	c7 04 24 b0 86 04 08 	movl   $0x80486b0,(%esp)
 8048529:	e8 92 fe ff ff       	call   80483c0 <scanf@plt>
 804852e:	8d 45 b8             	lea    -0x48(%ebp),%eax // str
 8048531:	89 44 24 04          	mov    %eax,0x4(%esp)
 8048535:	c7 04 24 b5 86 04 08 	movl   $0x80486b5,(%esp)
 804853c:	e8 4f fe ff ff       	call   8048390 <printf@plt>
 8048541:	8b 45 a0             	mov    -0x60(%ebp),%eax
 8048544:	89 04 24             	mov    %eax,(%esp)
 8048547:	e8 94 fe ff ff       	call   80483e0 <strlen@plt>
 804854c:	89 45 b0             	mov    %eax,-0x50(%ebp) // -> len(a2)
 804854f:	8b 45 a4             	mov    -0x5c(%ebp),%eax
 8048552:	89 04 24             	mov    %eax,(%esp)
 8048555:	e8 86 fe ff ff       	call   80483e0 <strlen@plt>
 804855a:	89 45 b4             	mov    %eax,-0x4c(%ebp) // -> len(a1)
 804855d:	c7 45 ac 00 00 00 00 	movl   $0x0,i
 8048564:	eb 3c                	jmp    80485a2 <check_permission+0xa5>
 8048566:	8b 55 ac             	mov    i,%edx
 8048569:	8b 45 a4             	mov    -0x5c(%ebp),%eax
 804856c:	01 d0                	add    %edx,%eax // -> a1 + i
 804856e:	0f b6 08             	movzbl (%eax),%ecx // -> a1[i]
 8048571:	8b 45 ac             	mov    i,%eax
 8048574:	99                   	cltd
 8048575:	f7 7d b0             	idivl  -0x50(%ebp)
 8048578:	89 d0                	mov    %edx,%eax // -> r = i%len(a2)
 804857a:	89 c2                	mov    %eax,%edx
 804857c:	8b 45 a0             	mov    -0x60(%ebp),%eax
 804857f:	01 d0                	add    %edx,%eax // -> a2+r
 8048581:	0f b6 00             	movzbl (%eax),%eax // -> a2[r]
 8048584:	31 c8                	xor    %ecx,%eax
 8048586:	89 c2                	mov    %eax,%edx // -> a2[r]^a1[i]
 8048588:	8d 4d b8             	lea    -0x48(%ebp),%ecx
 804858b:	8b 45 ac             	mov    i,%eax
 804858e:	01 c8                	add    %ecx,%eax
 8048590:	0f b6 00             	movzbl (%eax),%eax // -> st[i]
 8048593:	38 c2                	cmp    %al,%dl
 8048595:	74 07                	je     804859e <check_permission+0xa1>
 8048597:	b8 00 00 00 00       	mov    $0x0,%eax
 804859c:	eb 11                	jmp    80485af <check_permission+0xb2>
 804859e:	83 45 ac 01          	addl   $0x1,i
 80485a2:	8b 45 ac             	mov    i,%eax
 80485a5:	3b 45 b4             	cmp    -0x4c(%ebp),%eax // if i < len(a1)
 80485a8:	7c bc                	jl     8048566 <check_permission+0x69>
 80485aa:	b8 01 00 00 00       	mov    $0x1,%eax
 80485af:	8b 5d f4             	mov    -0xc(%ebp),%ebx
 80485b2:	65 33 1d 14 00 00 00 	xor    %gs:0x14,%ebx
 80485b9:	74 05                	je     80485c0 <check_permission+0xc3>
 80485bb:	e8 e0 fd ff ff       	call   80483a0 <__stack_chk_fail@plt>
 80485c0:	83 c4 64             	add    $0x64,%esp
 80485c3:	5b                   	pop    %ebx
 80485c4:	5d                   	pop    %ebp
 80485c5:	c3                   	ret

080485c6 <main>:
 80485c6:	55                   	push   %ebp
 80485c7:	89 e5                	mov    %esp,%ebp
 80485c9:	83 e4 f0             	and    $0xfffffff0,%esp
 80485cc:	83 ec 20             	sub    $0x20,%esp
 80485cf:	c7 44 24 18 ca 86 04 	movl   $0x80486ca,0x18(%esp)
 80485d6:	08
 80485d7:	c7 44 24 1c d0 86 04 	movl   $0x80486d0,0x1c(%esp)
 80485de:	08
 80485df:	8b 44 24 18          	mov    0x18(%esp),%eax
 80485e3:	89 44 24 04          	mov    %eax,0x4(%esp)
 80485e7:	8b 44 24 1c          	mov    0x1c(%esp),%eax
 80485eb:	89 04 24             	mov    %eax,(%esp)
 80485ee:	e8 0a ff ff ff       	call   80484fd <check_permission>
 80485f3:	83 f8 01             	cmp    $0x1,%eax
 80485f6:	75 0e                	jne    8048606 <main+0x40>
 80485f8:	c7 04 24 f3 86 04 08 	movl   $0x80486f3,(%esp)
 80485ff:	e8 ac fd ff ff       	call   80483b0 <puts@plt>
 8048604:	eb 0c                	jmp    8048612 <main+0x4c>
 8048606:	c7 04 24 0d 87 04 08 	movl   $0x804870d,(%esp)
 804860d:	e8 9e fd ff ff       	call   80483b0 <puts@plt>
 8048612:	c9                   	leave
 8048613:	c3                   	ret

```
 * main：位在`0x80486d0`, `0x80486ca`的兩字串是 `check_permission`的參數 A1, A2
 * check_permission
  * 讀入一個字串：str
  * 分別算A1, A2的長度
  * 計算 `x = A1[i] ^ A2[i % len(A2)]``
  * 目標：`str[i] == x`, for all i

## Solve
正確的字串就是 `A1[i] ^ A2[i % len(A2)]`, for i = 0 to len(A1)
 * 用gdb 找出 A1, A2
 ```
 (gdb) b *0x8048593
 (gdb) x 0x80486d0
 (gdb) x 0x80486d4
 ... until find '\0'
 (gdb) x 0x80486ca
 (gdb) x 0x80486ce
 ... until find '\0'
 ```
 * 寫[python script](solve.py) 解決
