from controller.UsuarioBean import UsuarioBean
from models.entities.Usuario import Usuario
from views.menu_escolha_horarios import menu_escolha_horarios


def login():
    usuario_bean = UsuarioBean()

    email = input("Digite seu email: ")
    senha = input("Digite a sua senha: ")

    login = usuario_bean.login(email, senha)

    if login:
        menu_escolha_horarios(login)
    else:
        print("Usuário não encontrado, digite novamente.")
        email = input("Digite seu email: ")
        senha = input("Digite a sua senha: ")

        login = usuario_bean.login(email, senha)




