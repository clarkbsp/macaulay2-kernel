#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 18:41:09 2017

@author: clark
"""

from ipykernel.kernelbase import Kernel

import pexpect

child = pexpect.spawnu("M2")

child.expect ('i\d+ :')

print('\n'.join(child.before.split('\r\n')[:-1]))

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
        if not silent:
            #code = '; '.join(code.split('\n'))#breaks for string literals containing \n
            for line in code.split('\n'):
                child.sendline(line)
                child.expect(['i\d+ :', '\r\n     '])
            result = child.before.split('\r\n')[1:-1]
            result = '\n'.join(result)
            
            #result = repr(code)
                   
            stream_content = {'name': 'stdout', 'text': result}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            
        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=M2Kernel)