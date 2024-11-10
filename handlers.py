from maneger_dir import *

def validate_input(input):
        return input.isalnum()

def save_data(path_projeto, language):
        path_directory = init_create_project()
        print(path_directory)
        # tenho que fazer a area que vai verificar a linguagem e vai direcionar para a parte de fabricar o projeto 
        
def init_create_project():
        path_diretory = get_path_directory()
        check_path(path_diretory)
        go_to(path_diretory)
        return path_diretory
        