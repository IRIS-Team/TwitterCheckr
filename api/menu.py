import os
from colorama import Fore, Style

def returnColor(string):
    return f'{Fore.MAGENTA}{string}{Style.RESET_ALL}'

def banner():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    print (f'''  {Fore.WHITE}{Fore.LIGHTBLACK_EX}          {Fore.MAGENTA}z
 {Fore.LIGHTBLACK_EX}  {Fore.MAGENTA}z      {Fore.LIGHTBLACK_EX}   _____ ___ _           _                 
 {Fore.MAGENTA}        {Fore.LIGHTBLACK_EX}   |_   _/ __| |_  ___ __| |___ _ 
 {Fore.MAGENTA}       z{Fore.LIGHTBLACK_EX}     | || (__| ' \/ -_) _| / / '_|
 {Fore.MAGENTA}    ᓚᘏᗢ  {Fore.LIGHTBLACK_EX}    |_| \___|_||_\___\__|_\_\_|  {Fore.LIGHTGREEN_EX}0.1{Fore.WHITE}
{Fore.LIGHTBLACK_EX}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{Fore.LIGHTBLACK_EX}
 ''')

def menu():
    target = input(f'Username: {Fore.MAGENTA}@{Style.RESET_ALL}')
    return target