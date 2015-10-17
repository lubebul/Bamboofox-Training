# Crack Windows Egg-Level Reversing
Given
 * [windows executable](ConsoleApplication2.exe)
 * [analysis tool](https://drive.google.com/open?id=0B84AHWN3DG-gVWhBMkN6RTRoZUk)

# Analysis
用IDAPro打開後，分析程式碼
 * 要你輸入字串 str
 * 檢查str[i] 是大寫英文字母
 * `x = (x + str[i] - 'A')*26`
 * 目標：`x == 0x531F919`

# Solve
算`0x531F919`的26進制，然後在用大寫字母表示出來
 * [solve.py](solve.py)
