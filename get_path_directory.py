import os 
from pathlib import Path

def get_path_directory(folder:str='Projetos'):
    # BUSCAR NOME DA PASTA DE USUÁRIO
    diretorio_home = Path.home()
    # ENTRAR NA PASTA DE USUÁRIO
    os.chdir(diretorio_home)
    #print(diretorio_home)
    # VARIAVÉL PARA DIRETÓRIO PADRÃO DOS PROJETOS
    return f'{diretorio_home}/{folder}'