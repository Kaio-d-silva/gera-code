import os 
from pathlib import Path

# Diretorio padrão dos projetos
def get_path_directory(folder:str='Projetos'):
    # BUSCAR NOME DA PASTA DE USUÁRIO
    diretorio_home = Path.home()
    # ENTRAR NA PASTA DE USUÁRIO
    os.chdir(diretorio_home)
    # VARIAVÉL PARA DIRETÓRIO PADRÃO DOS PROJETOS
    return f'{diretorio_home}/{folder}'


def check_path(directory):
    # VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
    if os.path.exists(directory) == False:
        os.mkdir(directory)

def go_to(directory):
    # ENTRA NO DIRETÓRIO PADRÃO
    os.chdir(directory)
    
def checks_files(full_path):
    # VERIFICA SE NA RAIZ DO PROJETO EXISTE UM ARQUIVO MAIN
    # CASO NÃO ELE É CRIADO
    if os.path.isfile(f'{full_path}/main.py') == False:
        os.mknod('main.py')

    # EXIBE O CAMINHO COMPLET DO NOVO PROJETO CRIADO
    print(f'{full_path}/main.py')
       
    
# IMPORTAÇÕES DO USUARIO

def user_input_dir(directory_home):
    # SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
    dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')
    
    # VARIÁVEL COM O CAMINHO COMPLETO DO PROJETO A SER CRIADO
    return f'{directory_home}/{dir_novo_projeto}'



def options():
    print(20 * "-")
    option = input(str('Quer instalar o tkinter ?\nSIM\nNÃO\n'))
    print(20 * "-")
    return option
    

def select_project():
    exit = False
    while exit == False:
        print(20*"-")
        project = input("Quer um projeto Python ou node ?\nPara Python escreva ' P ' para Node ' N ' \n")
        print(20*"-")
        if project == "P":
            user_project = "Python"
            exit = True
        elif project == "N":
            user_project = "Node"
            exit = True
        
    return user_project

