import subprocess
import os
i_pip = 0
while i_pip != 1:
    try:
        import mouse
        i_pip = 1
    except:
        import pip_get.py
import pyautogui
import random
import requests
import json
import os.path
from os import path
import keyboard
import sys
import time
global  start, last, browsers, count, rundex
import os
from pynput.keyboard import Key, Controller
import pyperclip
def fold_exists(x):
    isit = os.path.isdir(x)
    return isit
def vpn_ovpn():
    ovpn_dir = 'C:\Program Files/OpenVPN/config'
    dir_change(ovpn_dir)
    arr = os.listdir(ovpn_dir)  
    num = int(len(arr))
    i = int(0)
    proxies = ''
    ovpn_count = None
    while i < num:
        new = str(arr[i])
        if new[-5:] == ".ovpn":
            txt = reader(str(new))
            if ovpn_count == None:
                ovpn_count = int(-1)
            ovpn_count = ovpn_count + 1
            proxies = proxies +'"'+str(new)+'",'
            i = i + 1
        else:
            i = i + 1
    proxies = proxies[:-1]
    return proxies,ovpn_count
def enterit():
    from keyboard import press
    press('enter')
    #print("enter pressed")
    return
def dir_change(x):
    x = str(x).replace("C:\\",'')
    os.chdir(r"C:\\"+x)
    #print("directory changed to ","C:\\"+x)
    return "C:\\"+x
def string_clean(x):
    x = str(x).replace('(','').replace(')','').replace(' ','').replace("'",'')
    return x
def stringify(x):
    n = 0
    y = str(x).split(',')
    while True:
        try:
            y[n]
            n = n + 1
        except:
            return y, n
def timer(n,i):
    return int(n + i)
def cou(x):
    return float(int((len(str(x)) - len(str(x).replace(',','')))))
def create_globals(x,y):
    x = string_clean(x)
    globals()[str(x)] = y
    #print(x,y)
ordered_headers_list = []
def js_rep(n):
    directory = dir_change(home_fold)
    count_txt = reader("C:/"+home_fold+'counts.txt')
    count = str('{'+count_txt+'}').replace("'",'"')
    count = json.loads(count)
    n = int(n)
    v = rundex[n]
    #print(v)
    count[v] = str(int(count[v])+int(1))
    count = str(count).replace("{",'').replace("}",'')
    write(count,"counts.txt")
    os.chdir(r"C:\\"+config_fold)
    
    return 
def js_clean(txt):
    txt = str(txt).replace("'",'"')
    return txt
def now():
    return float(time.time())
start = now()
last = time.time()
pyautogui.FAILSAFE = False
chrome = "calibrate","chrome","url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
firefox = "calibrate","firefox","url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
brave = "calibrate","brave","url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
opera = "calibrate","opera","url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
edge = "calibrate","edge","url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
safari = "calibrate","safari","url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
chromium = "calibrate","chromium","url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
but_dict = {}
json_but = ''
def get_time(x):
    t = now()
    if x == 1:
        t = float(t)
    elif x == 2:
        t = int(t)
    return t
def mac_spoof():
    new_mac = ''
    mac_count = 0
    while mac_count < 12:
        count = 0
        while count != 2:
            mac_i = random.randint(1,9)
            new_mac = new_mac + str(mac_i)
            mac_count = mac_count + 1
            count = count + 1
        if count == 2:
            new_mac = new_mac + ':'
            count = 0
    if mac_count == int(12):
        new_mac = new_mac[:-1]
        #print(new_mac)
    return new_mac
def mac():
    spoof = mac_spoof()
    os.system('spoof-mac.py set '+spoof+' en0')
def vpns(browser_list):
    fold_exi = fold_exists('C:/Program Files/OpenVPN')
    if fold_exi != True:
        return
    proxies, count = vpn_ovpn()
    if count == None:
        return
    proxies = json.loads('['+proxies+']')
    os.system("taskkill.exe /F /IM openvpn.exe")
    i = random.randint(0,count)
    new = '"C:/Program Files/OpenVPN/bin/openvpn-gui.exe" --connect ' + '"'+ proxies[i] + '"'
    proc = subprocess.check_output( new ,stderr=subprocess.STDOUT,shell=True)
    print("waiting for vpn to activate")
    time.sleep(10)
    enterit()
    return
def create_var(x,y):
    create_globals(x,y)
    return
def fold_exists(x):
    isit = os.path.isdir(x)
    return isit
def browser_switch(n,browser_list):
    vpns(browser_list)
    directory = dir_change(home_fold)
    #print(browser_list)
    browser_list = json.loads(browser_list)
    curr_browser = browser_list[n]
    curr_file = 'positions_browsers_'+curr_browser+'.txt'
    txt = reader(curr_file)
    curr_browser_pos_json = json.loads(txt)
    x = "taskbar_browser","etherscan","cmcap","telegram","twitter","website","plus","tab_one","tab_two","exiter","refresh","url","trade"
    x,n = stringify(x)
    y = str(curr_browser),"eth","cmc","tg","tw","site","add","tab_0","tab_1","exiter","refresh","url","trade"
    i = 0
    while i != n:
        taskbar_browser = curr_browser_pos_json[y[i]] 
        g = float(taskbar_browser[0]),float(taskbar_browser[1])
        create_var(x[i],g)
        i = timer(i,1)
    return curr_browser_pos_json, curr_browser
def rando():
    #print("rando")
    timer = 0
    rando_circle = -1
    while rando_circle < 1:
        rando= random.randint(-500, 500)
        U_new = (2700 + rando)
        U_new_two = (900 + rando)
        U_new = U_new, U_new_two
        S_2 = random.uniform(0.4,2.0)
        move(U_new,S_2)
        rando_circle = random.randint(0, 1)
        rando_scroll = random.randint(-2, 1)
        rando_scroll_D_M = random.randint(-1, 1)
        rando_scroll_inv = random.randint(-50, 50)
        if rando_scroll_inv == int(0):
            rando_scroll_inv = int(1)
        if rando_scroll_D_M < 0:
            scro =(rando_scroll * 300)*rando_scroll_inv
        elif rando_scroll_D_M > 0:
            scro =(rando_scroll * 300)/rando_scroll_inv
        elif rando_scroll_D_M == 0:
            scro =(rando_scroll * 300)
        rando_mid_side = random.randint(1600, 2600)
        rando_mid_up = random.randint(900, 1700)
        scro = int(scro)
        pyautogui.scroll(scro, x=rando_mid_side, y=rando_mid_up)
        S = random.randint(0, 8)
        timer = timer + S
        time.sleep(S)
        pyautogui.scroll(10000)
    return
def exists(name,d):
    directory = dir_change(d)
    try:
        json_but = reader(name)
        dir_change(directory)
        return json_but
    except:
        dir_change(directory)
        return "no"
def on_space():
    print('going to exit soon')
    os.chdir('C:\\'+home_fold+'/')
    write("endit",'endit.txt')
    os.chdir(directory)
def read_space():
    os.chdir('C:\\'+home_fold+'/')
    txt = reader('endit.txt')
    os.chdir(directory) 
    return txt
def write(A,name):
    #print("write")
    f = open(name, "w")
    f.write(A)
    f.close()
    return
def reader(name):
    f = open(name,'r')
    txt = f.read()
    f.close()
    return txt
def input_val(txt):
    try:
        x = input(txt)
    except ValueError:
        print('Thats not a number!')
    return int(x)
def pos():
    directory = dir_change(home_fold)
    json_browse = ''
    all_browse_pos = ''
    browser_list = ''
    browse = 0
    try:
        num_browse = input("how many browsers will you be using?")
        create_globals("num_browse",num_browse)
    except ValueError:
        print("That's not an int!")
    i_temp = int(0)
    haz = ''
    count_brow = int(0)
    while i_temp < int(7):
        exist = exists("positions_browsers_"+browsers[i_temp]+'.txt',home_fold)
        if exist != "no":
            #print("we have ",browsers[i_temp])
            haz = haz + "'"+ browsers[i_temp]+'"'+','
            count_brow = count_brow + 1
            #print(count_brow)
        i_temp = timer(i_temp,1)
        #print(i_temp)
    if count_brow == int(num_browse):
        i_saved = 0
        dir_change(directory)
        arr = os.listdir(directory)  
        num = int(len(arr))
        i = int(0)
        proxies = ''
        saved_count = int(0)
        while i < num:
            new = str(arr[i])
            if "positions_browsers_" in str(new):
                txt = reader(str(new))
                saved_count = saved_count + 1
                i = i + 1
            else:
                i = i + 1
        bypass = input("it looks as if you have "+str(saved_count)+" browsers already saved and calibrated; they are: " + haz[:-1] + ". would you like to bypass the positioning setup? (Y or N)")
        if bypass == "Y" or bypass == "y" or bypass == "yes":
            browser_list = '[' + haz + ']'
            browser_list = browser_list.replace(',]',']')
            browser_list = browser_list.replace("'",'"')
            return but_dict,json_browse,browser_list
    while browse < int(num_browse):
        #print(browser_list)
        try:
            avail_browse = input('which browser would you like to impliment? (1 == chrome,2 == firefox,3 == brave,4 == edge,5 == opera,6 == safari, 7 == chromium)')
            avail_browse = int(avail_browse) - 1
            #print(avail_browse)
            browser_list = browser_list+'"'+browsers[avail_browse]+'"' + ','
            #print("1st",browser_list)
            #print('Thats not a number!')
        except:
            break
        exist = exists("positions_browsers_"+browsers[avail_browse]+'.txt',home_fold)
        but_i = 0
        cal = "N"
        but = "calibrate",browsers[avail_browse],"url","eth","cmc","tg","tw","site","add","trade","refresh","exiter","tab_0","tab_1","more_info"
        talk ="calibrate",browsers[avail_browse],"url","etherscan","coinmarketcap","telegram","twitter","website","add","trade","refresh","exit","tab_1","tab_2","more_info"
        if exist != "no":
            cal = input("looks like the configuration for "+browsers[avail_browse]+" is already saved. did you still want to recalibrate? (Y or N)")
            if cal == "N" or cal == "n" or cal == "no":
                browse = browse + 1
            
        if cal == "Y" or cal == "y" or cal == "yes" or exist == "no":
            #print("position")
            json_browse = ''
            but_i = 0
            try:
                exist = "y"
                while True and but_i < 15:
                    if but_i == 0:
                        exist = "x"
                    elif but_i == 1:
                        print("1) be sure to pin "+  talk[but_i] +" to the taskbar, then open it, maximize the browser; \n input "+pair+"\ninto the url of the first tab and load the site \nnext instruction in 10 seconds")
                        time.sleep(10)
                        print("\n2)alt-tab into the install window with the previous dialog and position it so that you can see all buttons you want to click on the browser behind it\nnext instruction in 10 second")
                        time.sleep(10)
                        ent = "\n3) place the curser on the "+ talk[but_i]+" on the taskbar and press enter"
                    else:
                        if but_i in range(4,8):
                            ent = "if "+ talk[but_i]+" does not exist press x then enter, otherwise press enter"
                        elif talk[but_i] == "url":
                            ent = "place the curser on the "+ talk[but_i]+" bar and press enter"
                        else:
                            ent = "place the curser on the "+ talk[but_i]+" button and press enter"
                    if exist == "x":
                        x,y = None,None
                        if but_i in range(4,8):
                            but_i = 8
                    else:
                        command = input(ent)
                        x,y = pyautogui.position()
                    exist = "y"
                    x = str(str(x).rjust(4))
                    x = x.replace(' ','')
                    y = str(str(y).rjust(4))
                    y = y.replace(' ','')
                    positionStr = x, y
                    but_dict[but[but_i]] = positionStr
                    test = but_dict[but[but_i]]
                    #print(test[0], test[1])
                    #print(but_dict)
                    json_browse = json_browse + ',"'+but[but_i]+'":'+'["'+test[0]+'","'+ test[1]+'"]'
                    json_browse= json_browse.replace('"calibrate":["None","None"],','')
                    #print(json_browse)
                    but_i = but_i + 1
                    #print("but_i",but_i)
                if but_i == 15:
                    json_browse = json_browse.replace(',','', 1)
                    json_browse = json_browse.replace('"calibrate":{"None","None"},','')
                    json_browse = '{' + str(json_browse) + '}'
                    all_browse_pos = all_browse_pos + browsers[avail_browse] + ',\n'
                    write(json_browse,"all_browse_pos")
                    #print("allbrowse",all_browse_pos)
                    write(json_browse,("positions_browsers"+'_'+str(browsers[avail_browse])+'.txt'))
                    print("please exit out of "+browsers[avail_browse]+" and return to this screen \nnext instruction in 10 second")
                    #print(json_browse)
                    browse = browse + 1
            except KeyboardInterrupt:
                print('\n')
            if but_i == 14:
                json_browse = json_browse.replace(',','', 1)
                json_browse = json_browse.replace('"calibrate":{"None","None"},','')
                json_browse = '{' + str(json_browse) + '}'
                all_browse_pos = all_browse_pos + json_browse + ',\n'
                #print("allbrowse",all_browse_pos)
                write(json_browse,"positions_browsers")
                #print(json_browse)
    if browse == int(num_browse):
        #print("avail",avail_browse)
        browser_list = '[' + browser_list + ']'
        browser_list = browser_list.replace(',]',']')
        browser_list = browser_list.replace("'",'"')
        create_globals("browser_list",browser_list)
        directory = dir_change(config_fold)
        return but_dict,json_browse,browser_list
def refference(last,refreshes):
    T = time.time()
    ref = time.time() - last
    if ref > refreshes:
        #print("refresh over ",refreshes)
        return int(1)
    else: 
        #print("refresh  under ",refreshes)
        return int(0)
def click(P):
    #print("click")
    pyautogui.click(P[0], P[1])
def move(P,D):
    #print("move")
    pyautogui.moveTo(P[0], P[1], duration = D)
    return
def D_go(P):
    #print("go")
    S = random.uniform(0.4,2.0)
    T = random.randint(1, 2)
    A = random.randint(1, 59)
    A = A*2
    D = S
    S_2 = random.uniform(0.4,2.0)
    if T == 1:
        U = P[0] + A
        U_two = P[1] - A
    elif T == 2:
        U = P[0] - A
        U_two = P[1] + A
    near = U, U_two
    move(near,S_2)
    pyautogui.scroll(10000)
    pyperclip.copy(str(pair))
    move(P, D)
    click(P)
    pyautogui.hotkey('ctrl', 'v')
    enterit()
    return 
def go(P):
    S = random.uniform(0.4,2.0)
    R = random.randint(0,1)
    if R == 0:
        rando()
    T = random.randint(1, 2)
    A = random.randint(1, 59)
    A = A*2
    D = S
    S_2 = random.uniform(0.4,2.0)
    if T == 1:
        U = P[0] + A
        U_two = P[1] - A
    elif T == 2:
        U = P[0] - A
        U_two = P[1] + A
    near = U, U_two
    move(near,S_2)
    move(P, D)
    #print("clicking ",P)
    click(P)
    if P == tab_one:
        ref = refference(last,refreshes)
        if ref == 1:
            js_rep(int(0))
            go(refresh)
    return
def go_norand(P):
    #print("go")
    S = random.uniform(0.4,2.0)
    T = random.randint(1, 2)
    A = random.randint(1, 59)
    A = A*2
    D = S
    S_2 = random.uniform(0.4,2.0)
    if T == 1:
        U = P[0] + A
        U_two = P[1] - A
    elif T == 2:
        U = P[0] - A
        U_two = P[1] + A
    near = U, U_two
    move(near,S_2)
    pyautogui.scroll(10000)
    move(P, D)
    click(P)
    if P == tab_one:
        ref = refference(last,refreshes)
        if ref == 1:
            js_rep(int(0))
            go(refresh)
    return 
def run(XX):
    initial == int(1)
    ti = get_time(1)
    last = ti
    curr = 0
    #print("run")
    P = XX[1],XX[0]
    go(P) 
    D = random.uniform(float(0.4),float(2.0))
    W = random.randint(0,7)
    while int(W) < int(8):
        curr = get_time(1) - ti
        endit = read_space()
        if endit == "endit":
            sys.exit("Error message")
            exit()
        #print(curr,browser_times,refreshes)
        if W == 0 :
            ref = refference(last,refreshes)
            #print("ref",ref)
            if ref == int(1):
                ran = random.randint(1, 3)
                if ran == 3:
                    #print("going to click input url to ",rundex[W], '@ ',refresh)
                    go_norand(tab_one)
                    D_go(url)
                    js_rep(int(0))
                    last = get_time(1)
                else:
                    #print("going to click ",rundex[W], '@ ',refresh)
                    go(refresh)
                    js_rep(int(0))
                    last = get_time(1)
        if W == 1:
            #print("etherscan")
            #print("going to click ",rundex[W], '@ ',etherscan)
            go(etherscan)
            
            js_rep(W)
            go(tab_one)
        if W == 2:
            #print("coinmarketcap")
            #print("going to click ",rundex[W], '@ ',cmcap)
            go(cmcap)
            js_rep(W)
            go(tab_one)
        if W == 3:
            #print("telegram")
            #print("going to click ",rundex[W], '@ ',telegram)
            go(telegram)
            js_rep(W)
            go(tab_one)
        if W == 4:
            #print("twitter")
            #print("going to click ",rundex[W], '@ ',twitter)
            go(twitter)
            js_rep(W)
            go(tab_one)
        if W == 5:
            #print("website")
            #print("going to click ",rundex[W], '@ ',website)
            go(website)
            js_rep(W)
            go(tab_one)
        if W == 6:
            #print("trade")
            #print("going to click ",rundex[W], '@ ',trade)
            go(trade)
            js_rep(W)
            go(tab_one)
        if W == 7 and int(curr) > int(browser_times):
            #print("exiting browser", curr," is greater than ", browser_times)
            js_rep(W)
            go(exiter)
            n = random.randint(0,(int(num_browse)-1))
            #print(browser_list)
            curr_browser_pos_json, curr_browser = browser_switch(n,browser_list)
            D = 0.4 
            #print("taskbargoogle",taskbar_browser)
            move(taskbar_browser,D)
            click(taskbar_browser)
            go_norand(tab_one)
            D_go(url)
            run(taskbar_browser)
        
        current = (float(time.time()) - float(start))/float(60)
        directory = dir_change(home_fold)
        count = reader("C:/"+home_fold+'counts.txt')
        os.chdir(r"C:\\"+config_fold)
        print("over ",current," minutes there have been ",count)
        W = random.randint(0,7)
        endit = read_space()
        
        #print("rando == ", W)
        rando()
    while W == int(9):
        sys.exit("Error message")
        exit()

global count, exiting, initial, pair, home_fold, config_fold, directory, done, proxies
directory =  str(os.getcwd()).replace('\\','/')+'/'
home_fold = directory.replace("C:/",'')
create_globals("home_fold",home_fold)
config_fold = "Program Files/OpenVPN/config"
browsers = "chrome","firefox","brave","edge","opera","safari","chromium"
create_globals("browsers",browsers)
directory = dir_change(home_fold)
write('','C:\\'+home_fold+'/endit.txt')
ex_pair = exists('pair.txt',directory)
if ex_pair != "no":
    pair_prev = reader('pair.txt')
    pair_ans = input('is '+ pair_prev +' still the desired pair??(Y or N)')
    if pair_ans == "N":
        pair = input("please input the dextools pair youd like to trend.(the entire link please)")
        write(pair,'pair.txt')
    else:
        pair = pair_prev
else:
    pair = input("please input the dextools pair youd like to trend.(the entire link please)")
    write(pair,'pair.txt')
initial = 0
exiting = int(3304),int(23)
count = '"refresh":"0","etherscan":"0","cmc":"0","twitter":"0","telegram":"0","website":"0","trade":"0","vpn_switch":"0"'
write(count,"C:/"+home_fold+'/counts.txt')
rundex = "refresh","etherscan","cmc","telegram","twitter","website","trade","vpn_switch"
directory = dir_change(config_fold)
keyboard.add_hotkey('space', on_space)
but_dict,json_browse,browser_list = pos()
D = 1
X = 0
refreshes = input_val("how often would you like to refresh(seconds, 0 for random)?")
if refreshes == int(0):
    refreshes = random.randint(int(35),int(100))
browser_times = input_val("how often would you like to switch browsers(seconds, 0 for default(5 min))?")
if browser_times == int(0):
    browser_times = int(300)
#print(refreshes,browser_times)
browsers = input("please reopen all browsers:\n"+browser_list+"\nmake sure each is maximized and exit each after doing so; then return to this screen and press enter")
print('in order to stop the script, press space bar and it will kill the script shortly')
time_var = "refreshes","browser_times"
time_input = refreshes,browser_times
i = 0
while i < 2:
    create_globals(time_var[i],time_input[i])
    i = timer(i,1)
while X == 0:
    print("starting")
    if initial == int(1):
        go(exiter)
    #print("select browser")
    n = random.randint(0,(int(num_browse)-1))
    #print(browser_list)
    curr_browser_pos_json, curr_browser = browser_switch(n,browser_list)
    #print("starting")
    D = 0.4 
    #print("taskbargoogle",taskbar_browser)
    move(taskbar_browser,D)
    click(taskbar_browser)
    go_norand(tab_one)
    D_go(url)
    run(taskbar_browser)
exit()

