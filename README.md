Dependencies:
    Requires python3, M2, jupyter, pexpect
    
    jupyter/pexpect can be installed through pip3/conda
    
Automatic Installation:
    If you're using Linux, run 'python3 install.py' from the project root folder
    
Backup Manual Installation:
    run 'jupyter kernelspec install --user m2kernel' from the project root directory
    run 'jupyter notebook' from a directory containing m2kernel.py
    (Either the m2kernel folder in the project directory or 
    ~/.local/share/jupyter/kernels/m2kernel/ on Linux)