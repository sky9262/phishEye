import os
try:
    import colorama
except:    
    print("Some modules are not installed!!\nPlease wait. Installing.......")
    os.system('pip install colorama --quiet')
    os.system('cls' if os.name == 'nt' else 'clear')

from colorama import Fore, Style
import os
import time



def PrintBanner():
    print('''
    {red}██████╗ ██╗  ██╗██╗███████╗██╗  ██╗  ███████╗██╗   ██╗███████╗{reset}
    {yellow}██╔══██╗██║  ██║██║██╔════╝██║  ██║  ██╔════╝╚██╗ ██╔╝██╔════╝{reset}
    {bright}{yellow}██████╔╝███████║██║███████╗███████║  █████╗   ╚████╔╝ █████╗  {reset}
    {green}██╔═══╝ ██╔══██║██║╚════██║██╔══██║  ██╔══╝    ╚██╔╝  ██╔══╝  {reset}
    {blue}██║     ██║  ██║██║███████║██║  ██║  ███████╗   ██║   ███████╗{reset}
    {pink}╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝  ╚══════╝   ╚═╝   ╚══════╝{reset}
    {bright}Version {green}{ver}{white}
    '''.format(ver=1.4, red=Fore.RED, yellow=Fore.YELLOW, green=Fore.GREEN,
    blue=Fore.BLUE, pink=Fore.MAGENTA, white=Fore.WHITE, reset=Style.RESET_ALL, bright=Style.BRIGHT))

    time.sleep(2) 

# PrintBanner()
