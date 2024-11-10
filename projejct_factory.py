from comand_bash import *

def make_python_project():
    user_option = input("Quer instar o tkinter ? ")
    install_pip()
    creat_virtual_venv()
    if user_option == "SIM" or user_option == "sim" or user_option == "S" or user_option == "s":
        install_tkinter() 
    else:
        print("Projeto criado sem Tkinter")
    
def make_node_project():
    path_full_new_project = "a"
    change_dir_home()
    install_node()
    create_react_project()