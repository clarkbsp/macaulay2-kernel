#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:13:44 2017

@author: clark
"""

import pexpect
import sys

print('Macaulay2 Python REPL')

child = pexpect.spawnu("M2")


child.expect ('i\d+ :') #wait for next input prompt
o = child.before.split('\r\n')[:-1] 

print('\n'.join(o))

while True:
    cmd = input(child.after + ' ')
    cmd = cmd.strip()
    if cmd != '':
        if cmd == 'quit' or cmd == 'exit':
            sys.exit()
            
        child.sendline(cmd)
        
        child.expect(['i\d+ :', '\r\n     '])
        
        o = child.before.split('\r\n')[1:-1]
        
        print('\n'.join(o))