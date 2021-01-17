from controller.HorariosBean import HorariosBean
from models.entities.Horarios import Horarios


def digitar_horarios(id):
    horario = Horarios()
    horarios = HorariosBean()

    data = input("Digite a data referente aos horários? ")
    entrada = input("Digite o horário de entrada: ")
    saida_ao_intervalo = input("Digite o horário de ida ao intervalo: ")
    volta_do_intervalo = input("Digite o horário de volta do intervalo: ")
    saida = input("Digite o horário de saída: ")
    hora_extra = input("Digite o horário de início da hora extra: ")
    saida_hora_extra = input("Digite o horário de saída da hora extra: ")

    horario.set_data(data)
    horario.set_hora_entrada(entrada)
    horario.set_hora_saida_ao_intervalo(saida_ao_intervalo)
    horario.set_hora_volta_do_invervalo(volta_do_intervalo)
    horario.set_hora_saida(saida)
    horario.set_hora_inicio_extra(hora_extra)
    horario.set_hora_saida_extra(saida_hora_extra)
    horario.set_id_usuario(id)

    horarios.insert(horario)

