import os
from api.colors import colors
from colorama import Fore, Style

def returnColor(string):
    return f'{colors.main}{string}{Style.RESET_ALL}'

def banner():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

    print (f'''  {Fore.WHITE}{colors.darktext}          {colors.main}z
 {colors.darktext}  {colors.main}z      {colors.darktext}   _____ ___ _           _                 
 {colors.main}        {colors.darktext}   |_   _/ __| |_  ___ __| |___ _ 
 {colors.main}       z{colors.darktext}     | || (__| ' \/ -_) _| / / '_|
 {colors.main}    ᓚᘏᗢ  {colors.darktext}    |_| \___|_||_\___\__|_\_\_|  {colors.sencondary}0.1{Fore.WHITE}
{colors.darktext}▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬{colors.darktext}
 ''')

def menu():
    target = input(f'Username: {returnColor("@")}')
    return target