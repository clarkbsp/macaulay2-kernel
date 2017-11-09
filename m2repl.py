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
            
        #child.send(cmd+'\n')
        child.send('1\n2\n3'+'\n'+'\r\n')
        #i = child.expect(['o\d+','i\d+'])#'\r\n     '])
        #i = child.expect(['i\d+',pexpect.EOF])
        i=0
        while i == 0:
            i = child.expect(['i\d+','\r\n     \r\n     '])

            o = child.before.split('\r\n')[1:-1]
            #print("Before: ", repr(child.before))
            #print("After: ", repr(child.after))
            print('\n'.join(o))