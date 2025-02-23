from bash.comand_bash import *
from handlers.maneger_dir import go_to, check_path, check_file

def make_python_project(path_directory,name_project, libs):
    path_full_new_project = f"{path_directory}/{name_project}"
    check_path(path_full_new_project)
    go_to(path_full_new_project)
    print(path_full_new_project)
    check_file(path_full_new_project)
    # user_option = input("Quer instalar o tkinter ? ")
    user_option = libs
    venv_name = creat_virtual_venv()
    path_venv = f"{path_full_new_project}/{venv_name}"
    print(path_venv)
    install_pip(path_venv)
    if user_option: #== "SIM" or user_option == "sim" or user_option == "S" or user_option == "s":
        # print("!!!! INSTALANDO COM TKINTER !!!!")
        print("!!! INSTALANDO COM PYSIDE")
        # install_tkinter()
        install_Pyside(path_venv) 
    else:
        print("Projeto criado sem Tkinter")
    return path_full_new_project
    
def make_node_project(path_directory,name_project, libs):
    path_full_new_project = f"{path_directory}/{name_project}"
    change_dir_home()
    install_node()
    go_to(path_directory)
    create_react_project(name_project)
    return path_full_new_project
    
    