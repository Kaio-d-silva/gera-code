from maneger_dir import *
from options import verifica_linguagem

def validate_input(input):
        return input.isalnum()

def save_data(name_project, language, path_directory, libs):
        # path_directory = init_create_project()
        init_create_project(path_directory)
        return verifica_linguagem(path_directory,name_project,language, libs)
        
def init_create_project(path_directory):
        # path_diretory = get_path_directory()
        check_path(path_directory)
        go_to(path_directory)
        # return path_diretory
        