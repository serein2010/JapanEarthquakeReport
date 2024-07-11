%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit

for /f "tokens=2 " %c in ('tasklist  /fi "imagename eq get.exe" /nh') do taskkill /f /pid %c
for /f "tokens=2 " %b in ('tasklist  /fi "imagename eq waring.exe" /nh') do taskkill /f /pid %b