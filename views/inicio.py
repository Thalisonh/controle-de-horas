from controller.UsuarioBean import UsuarioBean
from models.entities.Usuario import Usuario
from views.input_usuario import login, cadastros


def main():
    usuario = Usuario()
    usuario_bean = UsuarioBean()

    usuario.set_nome("Thalison Henrique Morais Silva")
    usuario.set_email("thalison_henrique@hotmail.com")
    usuario.set_cpf("41455310867")
    usuario.set_data_nascimento("30/08/1996")
    usuario.set_senha("37246310")

    usuario_bean.insert(usuario)

def inicio():
    print("=====Controle de Horários=====")
    print()
    print("===== 1 - Login =====")
    print("===== 2 - Cadastro =====")
    print("===== 0 - Sair =====")

    escolha = int(input("Digite uma opção: "))

    if escolha == 0:
        pass
    elif escolha == 1:
        login()
    elif escolha == 2:
        cadastro()
    else:
        escolha = input("Opção inválida digite uma nova opção: ")

def cadastro():
    print("=====Controle de Horários=====")
    print("=====      CADASTROS     =====")
    print("==============================")
#    print("=====   1 - Confirmar    =====")
#    print("=====     2 - Voltar     =====")
#    print("=====    3 - Corrigir    =====")
    cadastros()


inicio()
