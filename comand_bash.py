import subprocess

def upgrad_linux():
    subprocess.run(f'''sudo apt update -y && sudo apt-get upgrade -y''', shell=True, check=True, executable='/bin/bash')
    
def install_pip():
    subprocess.run(f'''sudo apt install python3-pip''', shell=True, check=True, executable='/bin/bash')
       
def creat_virtual_venv():
    subprocess.run(f'''python3 -m venv .venv''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''source .venv/bin/activate''', shell=True, check=True, executable='/bin/bash')
    subprocess.run(f'''sudo apt install python3-venv''', shell=True, check=True, executable='/bin/bash')
    
def open_vscode(path):
    # ABRE O VS CODE NA PASTA DO PROJETO NOVO CRIADO
    subprocess.run(f'''code {path}''', shell=True, check=True, executable='/bin/bash')
    
