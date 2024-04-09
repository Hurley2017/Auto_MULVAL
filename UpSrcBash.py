import os
import sys
from time import sleep
from getpass import getuser

#update the bashrc to force system to work with existing installed mulval package.
def ConfigMulval():
    CURRENT_LOCATION = os.getcwd()
    MULVALROOT = CURRENT_LOCATION + "/mulval"
    ADDPATH = ":"+MULVALROOT + "/bin:" + MULVALROOT + "/utils:/usr/local/bin/xsb-5.0.0/bin"
    os.chdir('/home/' + getuser()) 
    os.system('echo "export MULVALROOT=' + CURRENT_LOCATION + '/mulval" >> .bashrc')
    os.system('echo "export PATH=$PATH'+ADDPATH+'" >> .bashrc')
    os.chdir(MULVALROOT)
    os.system('make')
    print('Check')

ConfigMulval()