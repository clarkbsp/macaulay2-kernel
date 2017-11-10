#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:33:30 2017

@author: clark
"""

import json, os, subprocess

subprocess.call(['jupyter', 'kernelspec', 'install', '--user', 'm2kernel'])

kernel_path = os.path.expanduser('~/.local/share/jupyter/kernels/m2kernel/')
kernel_json = {
 "argv": ["python3", kernel_path+'m2kernel.py',
          "-f", "{connection_file}"],
 "display_name": "Macaulay2",
 "language": "macaulay2"
}

with open(kernel_path+'kernel.json', 'w') as kernel_file:
    json.dump(kernel_json, kernel_file)
    
kernel_file.close()