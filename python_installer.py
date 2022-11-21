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
prog_fold = home_dir+'/programs'
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
#change_scripts = 'cd ' + prog_fold+ ' && '+ open_inst + ' && exit'
#print(change_scripts)
#cmd_line(change_scripts)
#cmd_line('exit')
proc = subprocess.check_output( change_scripts ,stderr=subprocess.STDOUT,shell=True)
fol = 'C:/Program Files/OpenVPN/config'
fold_exi = fold_exists(fol)
if fold_exi == True:
    ovpn_dir = 'C:\Program Files/OpenVPN/config'
    exist = exists('auth.txt',ovpn_dir)
    if exist == "no":
        writer('auth.txt','')
    dir_change(ovpn_dir)
    arr = os.listdir(ovpn_dir)
    num = int(len(arr))
    i = int(0)
    proxies = ''
    ovpn_count = int(-1)
    while i < num:
        new = str(arr[i])
        if new[-5:] == ".ovpn":
            print(i)
            txt = reader(str(new))
            txt = txt.replace('auth.txt','').replace(' auth.txt','').replace('auth.txt','').replace(' auth.txt','').replace('auth.txt','')
            txt = txt.replace('auth-user-pass','auth-user-pass auth.txt')

            write(new,txt)
            ovpn_count = ovpn_count + 1
            proxies = proxies +'"'+str(new)+'",'
            i = i + 1
            print("foundone")
        else:
            i = i + 1
    proxies = proxies[:-1]
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
click_copy = home_fold + '\clicks\clicks.py'
txt = reader(click_copy)
print(txt)
write(desktop+"\new_clicker\clicks.py",txt)

print('ending')
