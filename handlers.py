from maneger_dir import *
from options import verifica_linguagem

def validate_input(input):
        return input.isalnum()

def save_data(name_project, language):
        path_directory = init_create_project()
        return verifica_linguagem(path_directory,name_project,language)
        
        
        
def init_create_project():
        path_diretory = get_path_directory()
        check_path(path_diretory)
        go_to(path_diretory)
        return path_diretory
        