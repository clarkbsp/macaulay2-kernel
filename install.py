#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:33:30 2017

@author: clark
"""

import json, os, platform, subprocess, sys

os_name = platform.system()
if os_name == 'Linux' or os_name == 'Linux2': 
    kernel_path = os.path.expanduser('~/.local/share/jupyter/kernels/m2kernel/')
    
elif os_name == 'Darwin':
    kernel_path = os.path.expanduser('~/Library/Jupyter//kernels/m2kernel/')
    
else:
    print('Unsupported platform', os_name)
    sys.exit
    
kernel_json = {
 "argv": ["python3", kernel_path+'m2kernel.py',
          "-f", "{connection_file}"],
 "display_name": "Macaulay2",
 "language": "macaulay2"
}

subprocess.call(['jupyter', 'kernelspec', 'install', '--user', 'm2kernel'])

with open(kernel_path+'kernel.json', 'w') as kernel_file:
    json.dump(kernel_json, kernel_file)
    
kernel_file.close()