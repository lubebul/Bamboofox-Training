# Magic
 * 解題：`nc 140.113.209.24 10000`
 * binary file: [magic](magic)

## Description
關鍵代碼：
```
void do_magic(char *buf,int n) {
        int i;
        srand(time(NULL));
        for (i = 0; i < n; i++)
                buf[i] ^= rand()%256;
}
void magic() {
        char magic_str[60];
        scanf("%s", magic_str);
        do_magic(magic_str, strlen(magic_str));
        printf("%s", magic_str);
}
```

## Solve
看代碼：
 1. `magic()` 有 `buffer overflow` 問題
 2. 但 `do_magic()` 讓直接overwrite `RET address` 的攻擊無效
 3. `strlen` 回傳型態是`int` => 可以做 `integer overflow`!

所以，解題思路：
 * overflow `strlen(magic_str)` 使得回傳的長度為 0 => `do_magic()` 防禦無效
 * 可以執行overwrite `RET address`攻擊
  * 放入`ececve(/bin/sh)` 的shellcode
