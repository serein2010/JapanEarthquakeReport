import os
import sys
sys.path.append("..")
dir=os.getcwd()
print(dir)
dir=os.path.abspath(os.path.join(os.path.dirname('waring.exe'),os.path.pardir))
print(dir)
