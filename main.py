from pathlib import Path
import os
import subprocess
from get_path_directory import get_path_directory
from check_path_folder import check_path, go_to, checks_files
from user_input import user_input
from comand_bash import *

# VERIFICA QUAL É O DIRETORIO PADRAO
project_diretory = get_path_directory()

# VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
check_path(project_diretory)

# SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
path_full_new_project = user_input(project_diretory)

# VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
check_path(path_full_new_project)
# ENTRA NO DIRETÓRIO
go_to(path_full_new_project)

# VERIFICA SE NA RAIZ DO PROJETO EXISTE UM ARQUIVO MAIN
# CASO NÃO ELE É CRIADO
checks_files(path_full_new_project)


upgrad_linux()
install_pip()
creat_virtual_venv()
open_vscode(path_full_new_project)
