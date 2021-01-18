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

def cadastros():
    usuario_bean = UsuarioBean()
    usuario = Usuario()

#    nome = input("Digite seu nome: ")
#    email = input("Digite seu email: ")
#    cpf = input("Digite seu CPF: ")
#    data_nascimento = input("Digite sua data de nascimento: ")
#    senha = input("Digite uma senha: ")

    usuario.set_nome(input("Digite seu nome: "))
    usuario.set_email(input("Digite seu email: "))
    usuario.set_cpf(input("Digite seu CPF: "))
    usuario.set_data_nascimento(input("Digite sua data de nascimento: "))
    usuario.set_senha(input("Digite uma senha: "))

    usuario_bean.insert(usuario)




