import subprocess
import random
import os
import shutil
def get_path(x):
    og_dir = os.getcwd()
    og_dir = og_dir.replace('\\','/')
    x = x.replace('\\','/')
    dir_change(x)
    new_dir = os.getcwd()
    new_dir = new_dir.replace('\\','/')
    dir_change(og_dir)
    return new_dir
def dir_change(x):
    x = str(x).replace('C:\\\\','').replace('C:\\','').replace("C:/",'')
    print(x)
    x = str(x).replace("C:\\",'')
    print(x)
    os.chdir(r"C:/"+x)
    return "C:/"+x
def reader(x):
    f = open(x, "r")
    txt = f.read()
    return txt
def write(x, txt):
    f = open(x, "w")
    f.write(str(txt))
    f.close()
    return
def exists(name,d):
    directory = dir_change(d)
    try:
        json_but = reader(name)
        return json_but
    except:
        return "no"
def fold_exists(x):
    isit = os.path.isdir(x)
    return isit
def create_dir(name,d):
    directory = name
    path = os.path.join(d, directory)
    os.mkdir(path)
    path = path.replace('\\','/')
    return path
def cmd_line(txt):
    os.system('cmd /k "'+txt+'"')
home_dir = os.getcwd()
clicks_fold = home_dir + '/clicks'
fold_exi = fold_exists(clicks_fold)
if fold_exi != True:
    clicks_fold = create_dir("clicks",home_dir)



print(clicks_fold)
prog_fold = home_dir
prog_fold = get_path(prog_fold)
print(prog_fold)
open_inst = 'OpenVPN-2.5.3-I601-amd64.msi'
pyth_one = 'C:\Program Files\Python39\Scripts'
pyth_two = os.environ['USERPROFILE'] + '\AppData\Local\Programs\Python\Python39\Scripts'
cd_pyth = pyth_one
fold_exi = fold_exists(pyth_one)
if fold_exi != True:
    cd_pyth = pyth_two
change_scripts = 'cd '+cd_pyth+' && pip install mouse && pip install pyautogui && pip install keyboard && pip install requests && pip install pynput && pip install pyperclip && exit'
cmd_line(change_scripts)
print(change_scripts)
cmd_line('exit')
