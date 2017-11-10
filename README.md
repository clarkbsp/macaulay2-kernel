#Installation

###Dependencies:
    *Requires python3, M2, jupyter, pexpect
    *Jupyter/pexpect can be installed through pip3/conda
    
###Automatic Installation
    *Linux/Mac(untested)
    *Run `python3 install.py` from the project root folder
    
###Backup Manual Installation
    *Run `jupyter kernelspec install --user m2kernel` from the project root directory
    *Run `jupyter notebook` from a directory containing `m2kernel.py` (The m2kernel folder or~/.local/share/jupyter/kernels/m2kernel/ on Linux)