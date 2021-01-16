from controller.UsuarioBean import UsuarioBean
from models.entities.Usuario import Usuario
from views.inserir_horas import inserir_horas


def login():
    usuario_bean = UsuarioBean()

    email = input("Digite seu email: ")
    senha = input("Digite a sua senha: ")

    login = usuario_bean.login(email, senha)

    if login:
        inserir_horas()
    else:
        print("Usuário não encontrado, digite novamente.")
        email = input("Digite seu email: ")
        senha = input("Digite a sua senha: ")

        login = usuario_bean.login(email, senha)




