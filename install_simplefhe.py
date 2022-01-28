#!usr/bin/python3
import os

# Installation SEAL Python
os.system('sudo apt-get install git build-essential cmake python3 python3-dev python3-pip')
os.system('git clone https://github.com/Huelse/SEAL-Python.git')
os.chdir('SEAL-Python')
os.system('pip3 install -r requirements.txt')
os.system('git submodule update --init --recursive')
os.chdir('SEAL')
os.system('cmake -S . -B build -DSEAL_USE_MSGSL=OFF -DSEAL_USE_ZLIB=OFF -DSEAL_USE_ZSTD=OFF')
os.system('cmake --build build')
os.chdir('..')
os.system('mv scenario.py SEAL-Python/')
os.system('python3 setup.py build_ext -i')
os.system('pip3 install simplefhe')
