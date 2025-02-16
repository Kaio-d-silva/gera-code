from create_projects.project_factory import make_node_project, make_python_project

def verifica_linguagem(path_directory,name_project,linguagem, libs):
    if linguagem == "Python":
        return make_python_project(path_directory,name_project, libs)
    elif linguagem == "Node":
        return make_node_project(path_directory,name_project, libs)
    else:
        return "INVALIDO"
        