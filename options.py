from project_factory import make_node_project, make_python_project

def verifica_linguagem(path_directory,name_project,linguagem):
    if linguagem == "Python":
        return make_python_project(path_directory,name_project)
    elif linguagem == "Node":
        return make_node_project(path_directory,name_project)
    else:
        return "INVALIDO"
        