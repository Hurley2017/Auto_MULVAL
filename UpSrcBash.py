import os
import sys
from time import sleep
from getpass import getuser

#GLOBALS
CURRENT_LOCATION = os.getcwd()
MULVALROOT = CURRENT_LOCATION + "/mulval"
ADDPATH = ":"+MULVALROOT + "/bin:" + MULVALROOT + "/utils:/usr/local/bin/xsb-5.0.0/bin"

def FixXSBinstall():
    os.system('sudo tar -zxvf Resources/XSB-5.0.tar.gz -C /usr/local/bin')
    os.system('sudo mv /usr/local/bin/XSB /usr/local/bin/xsb-5.0.0')
    os.chdir('/usr/local/bin/xsb-5.0.0/build')
    os.system('sudo ./configure -prefix=/usr/local/bin')
    os.system('sudo ./makexsb')
    os.chdir(CURRENT_LOCATION)


def PerformSystemUpdate():
    os.system('sudo apt update && sudo apt upgrade -y')

def Install_Packages():
    os.system('sudo apt install -y build-essential default-jdk flex bison graphviz texlive-font-utils xutils-dev git')


def ConfigMulval():
    CURRENT_LOCATION = os.getcwd()
    MULVALROOT = CURRENT_LOCATION + "/mulval"
    ADDPATH = ":"+MULVALROOT + "/bin:" + MULVALROOT + "/utils:/usr/local/bin/xsb-5.0.0/bin"
    os.chdir('/home/' + getuser()) 
    os.system('echo "export MULVALROOT=' + CURRENT_LOCATION + '/mulval" >> .bashrc')
    os.system('echo "export PATH=$PATH'+ADDPATH+'" >> .bashrc')
    os.chdir(MULVALROOT)
    os.system('make')
    

if __name__ == "__main__":
    FixXSBinstall()
    PerformSystemUpdate()
    Install_Packages()
    ConfigMulval()
    print("Mulval has been installed successfully")