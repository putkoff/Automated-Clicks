import os
def dir_change(x):
    x = str(x).replace('C:\\\\','').replace('C:\\','').replace("C:/",'')
    x = str(x).replace("C:\\",'')
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
def fold_exists(x):
    isit = os.path.isdir(x)
    return isit
exi = fold_exists('C:\Program Files\OpenVPN\config')
if exi == True:
    new_dir = dir_change('C:\Program Files\OpenVPN\config')
    print('make sure you have the open vpn username and password from your VPN service')
    u = input("what is your OVPN ID?")
    p = input("what is your OVPN PASSWORD?")
    directory =  str(os.getcwd()).replace('\\','/')+'/'
    arr = os.listdir(directory)
    num = int(len(arr))
    i = int(0)
    all_names = ''
    while i < num:
        new = str(arr[i])
        if new[-5:] == ".ovpn":
            txt = reader(str(new))
            txt = txt.replace('auth.txt','').replace(' auth.txt','').replace('auth.txt','').replace(' auth.txt','').replace('auth.txt','')
            txt = txt.replace('auth-user-pass','auth-user-pass auth.txt')
            write(new,txt)
            i = i + 1
            print("foundone")
        else:
            i = i + 1
    all_names = all_names+','
    all_names = all_names.replace(',,','')


    n = '\n'

    auth = u + n + p
    write('auth.txt', auth)
    print('done')
else:
    print("please install open_VPN")
