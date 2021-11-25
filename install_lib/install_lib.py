# Author: Hoang Truong

##################################################################
###  a script to automatically upgrade pip and install pygame  ###
##################################################################

import sys
import os
import subprocess


def __install(package: str):
    # install package
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])




def __clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




def install_required_libraries():

    # make sure pip is installed first
    os.system(sys.executable + " " + os.getcwd() + "/install_lib/get_pip.py")
    
    # install pygame and PyQt5
    __install('pygame')
    __install('PyQt5')

    # clear screen and inform that the process is finished
    __clear_screen()
    print("--- FINISHED INSTALLATIONS ---")
