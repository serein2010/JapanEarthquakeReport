import subprocess
import os
import pystray
from PIL import Image

dir=os.getcwd()
print(dir)
# 用于存储两个子进程对象
processes = []
statu='none'#初始化
default='exit'
def run_exe(exe_path):
    process = subprocess.Popen(exe_path)
    processes.append(process)



# 两个 exe 文件的路径
exe_path1 = dir+"\\core\\api\\get.exe"
exe_path2 = "warning.exe"

# 运行两个 exe 文件
run_exe(exe_path1)
run_exe(exe_path2)

print(processes)
# 创建系统托盘图标
def on_quit():
    print("Quitting")
    os.system(dir+"/core/kill/kill.bat")



image = Image.open("core/img/bg.png")           # 打开 ICO 图像文件并创建一个 Image 对象
menu = (pystray.MenuItem(text='Exit', action=on_quit),) # 创建菜单项元组
icon = pystray.Icon("JEQR", image, "Japan Earthquake Report", menu)            # 创建 PyStray Icon 对象，并传入关键参数

# 显示图标
icon.run()                              # 启动托盘图标目录
