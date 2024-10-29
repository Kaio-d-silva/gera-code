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

