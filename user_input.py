def user_input(directory_home):
    # SOLICITA AO USUÁRIO UM NOME PARA O PROJETO A SER CRIADO
    dir_novo_projeto = input('Digite o nome do Projeto a ser criado: ')

    # VARIÁVEL COM O CAMINHO COMPLETO DO PROJETO A SER CRIADO
    return f'{directory_home}/{dir_novo_projeto}'