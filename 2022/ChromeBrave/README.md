
Open new tab in Brave through powershell (does not work on cmd line)
```
start-process "brave.exe" "https://www.nserc-crsng.gc.ca/Students-Etudiants/PG-CS/CGSM-BESCM_eng.asp",'--profile-directory="Default"'
```

https://developer.chrome.com/docs/extensions/

right click = context menu
https://developer.chrome.com/docs/extensions/reference/contextMenus/

Goal: open a link in brave with as few clicks as possible

Approach: open link in Brave through context menu in Chrome

or, work one level higher: use some system level stuff (eg sth like automator for Mac?)
