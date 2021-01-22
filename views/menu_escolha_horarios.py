from controller.HorariosBean import HorariosBean
from controller.UsuarioBean import UsuarioBean
from views.digitar_horarios import digitar_horarios, digitar_horarios_base


def menu_escolha_horarios(id):
    horario_bean = HorariosBean()

    print("===== Inserir horários =====")
    print("===== 1 - Digitar horários =====")
    print("===== 2 - Inserir Horarios Base =====")
    print("===== 0 - Voltar =====")

    escolha = int(input("Digite a sua opção: "))

    while escolha:
        if escolha == 1:
            digitar_horarios(id)
            menu_escolha_horarios(id)
            escolha = int(input("Digite a sua opção: "))
        elif escolha == 2:
            digitar_horarios_base(id)
            menu_escolha_horarios(id)
            escolha = int(input("Digite a sua opção: "))
        elif escolha == 0:
            break
        else:
            print("Opção inválida, escolha uma opção válida.")
            escolha = int(input("Digite a sua opção: "))
