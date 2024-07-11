@echo off

echo  ______   ______     ______     __  __    
echo /\  == \ /\  __ \   /\  ___\   /\ \/ /    
echo \ \  _-/ \ \  __ \  \ \ \____  \ \  _"-.  
echo  \ \_\    \ \_\ \_\  \ \_____\  \ \_\ \_\ 
echo   \/_/     \/_/\/_/   \/_____/   \/_/\/_/ 
echo ____________________________________________
if exist ./core (
    if exist ./core/api (
        if exist ./core/api/get.py (
            echo ./core/api/* checked
        )

    ) else (
        echo Missing file
    )
) else (
    echo Missing file
)

if exist ./core/img (
    if exist ./core/img/top.png (
        if exist ./core/img/api-py.ico (
            if exist ./core/img/main-py.ico (
                if exist ./core/img/warning-py.ico (
                    if exist ./core/img/bg.png (
                        echo ./core/img/* checked
                    ) else (
                        echo Missing file
                    )
                ) else (
                    echo Missing file
                )
            ) else (
                echo Missing file
            )
        ) else (
            echo Missing file
        )
    ) else (
        echo Missing file
    )
) else (
    echo Missing file
)

if exist ./core/sound (
    if exist ./core/sound/warning.wav (
        echo ./core/sound/* checked
    ) else (
        echo Missing file
    )
) else (
    echo Missing file
)

if exist ./warning.py (
    echo ./* checked
) else (
    echo Missing file
)

mkdir packed
if exist ./packed (
    echo [info]make directory "packed" success
) else (
    echo [err]make directory "packed" failed
)
mkdir packed\data
mkdir packed\data\json
mkdir packed\core
xcopy .\core .\packed\core\ /e /y
pip install pyinstaller

pyinstaller -F -w -i .\packed\core\img\api-py.ico .\packed\core\api\get.py
copy .\dist\get.exe .\packed\core\api\
del .\packed\core\api\get.py
rd /s /q build
rd /s /q dist
del .\*.spec

pyinstaller -F -w -i .\packed\core\img\warning-py.ico .\warning.py
copy .\dist\warning.exe .\packed\
rd /s /q build
rd /s /q dist
del .\*.spec

pip install pystray
pip install pillow

pyinstaller -F -w -i .\packed\core\img\main-py.ico .\main.py
copy .\dist\main.exe .\packed\
rd /s /q build
rd /s /q dist
del .\*.spec
