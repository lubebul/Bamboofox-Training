# Buffer Overflow and x86
some tips about gdb
 * default: ALSR is turned-off!
 * break point at addr: `(gdb) b *0x80486c8`
 * examine stacks: `(gdb) x/40x $ebp`
 * examine frame: `(gdb) info frame`
