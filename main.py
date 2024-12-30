# # from get_path_directory import get_path_directory
# # from check_path_folder import check_path, go_to, checks_files
# # from user_input import user_input_dir,options,select_project
# from comand_bash import *
# from maneger_dir import *

# # VERIFICA QUAL É O DIRETORIO PADRAO
# project_diretory = get_path_directory()

# # VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
# check_path(project_diretory)

# # VAI PARA DIRETORIO DO PROJETO 
# go_to(project_diretory)

# # SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
# path_full_new_project = user_input_dir(project_diretory)

# # VERIFICA SE EXISTE O DIRETÓRIO PADRÃO CASO NÃO ELE O CRIA
# check_path(path_full_new_project)

# # ENTRA NO DIRETÓRIO
# go_to(path_full_new_project)

# # VERIFICA SE NA RAIZ DO PROJETO EXISTE UM ARQUIVO MAIN
# # CASO NÃO ELE É CRIADO

# #checks_files(path_full_new_project)



# #upgrad_linux()
# selected_project = select_project()

# if selected_project == "Python":
#     install_pip()
#     creat_virtual_venv()
#     user_option = options()
#     if user_option == "SIM":
#         install_tkinter() 
#     else:
#         print("Projeto criado sem Tkinter")
        
# elif selected_project == "Node":
#     change_dir_home()
#     install_node()
#     create_react_project(path_full_new_project)
     
    
# open_vscode(path_full_new_project)

from ui import App

if __name__ == "__main__":
    app = App()
    app.run()