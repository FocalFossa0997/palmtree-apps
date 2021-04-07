import os
import time

print("Welcome to the palmtree-test setup application!")
print("This should setup palmtree-test and run it automatically!")
print("Now installing needed dependencies for palmtree-test")
time.sleep(1)
print("Now installing zenity")
os.system("sudo apt-get install zenity")
os.system("wget https://raw.githubusercontent.com/FocalFossa0997/palmtree-apps/main/apps/palmtree-test/test.txt")
os.system("zenity --title='palmtree-test (test.txt)' --text-info --filename='test.txt'")
os.system("rm test.txt")
