#Slides
 * [Reverse_Engineering](Reverse.pptx)
 * [Some Tips](Some tips.pptx)

## Some Tips
 * Vim + Tmux
  * Tmux：關掉後，下次打開會有一樣的視窗開啟同樣的檔案 => 非常適合跑很久的程式

## Basic Reverse Engineering
 * Memory Layout
  * Big-Endian vs Little-Endian
  * Stack：function參數，return address
  * Heap：malloc, demalloc
 * Representation Convention
  * 取值：`$eax`
  * 取reference address中的值：` ($eax)`
 * Common Structure
  * Loop：不斷檢查條件：符合後變數+1，跳回某段程式碼。不符合跳出
  * Array：(some register)

## Today's Vulnerable
 * [Crack Windows Egg-Level Reversing](EggReverse1)
 * [Crack Linux Still-Egg-Level Reversing](EggReverse2)
