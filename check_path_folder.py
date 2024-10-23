import os



def check_path(directory):
    # print(directory)
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
        
