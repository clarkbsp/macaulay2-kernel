#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:41:09 2017

@author: clark
"""

from ipykernel.kernelbase import Kernel

import pexpect
import re
import signal

child = pexpect.spawnu("M2")

child.expect ('i\d+ :')

print('\n'.join(child.before.split('\r\n')[:-1]))

#signal.signal(signal.SIGINT,print("interupt_received"))

class M2Kernel(Kernel):
    
    implementation = 'Macaulay2'
    implementation_version = '0.01'
    language = 'Macaulay2'
    language_version = '1.92'
    language_info = {'name': 'Macaulay2', 
                     'mimetype': 'text/plain'}
    banner = "Macaulay2"
    
    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        code = '\n'.join(re.findall('(?:"[^"]*"|.)+', code))#Collapses newlines in code
        if not silent:
            child.send(code+'\n'+'\r\n\r\n') 
            child.expect(['\r\n\s+\r\n\s+\r\n\s+'])
            
            #Output should probably be filtered/formatted
            result = '\n'.join(child.before.split('\r\n')[:-1])
            stream_content = {'name': 'stdout', 'text': result}
            self.send_response(self.iopub_socket, 'stream', stream_content)

            
        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=M2Kernel)