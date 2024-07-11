%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
for /f "tokens=2 " %a in ('tasklist  /fi "imagename eq get.exe" /nh') do taskkill /f /pid %a
for /f "tokens=2 " %a in ('tasklist  /fi "imagename eq warning.exe" /nh') do taskkill /f /pid %a