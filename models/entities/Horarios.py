class Horarios:
    _hora_entrada = None
    _hora_saida_ao_intervalo = None
    _hora_volta_do_invervalo = None
    _hora_saida = None
    _hora_inicio_extra = None
    _hora_saida_extra = None
    _data = None
    _id_usuario = None

    def __init__(self):
        self._hora_entrada
        self._hora_saida_ao_intervalo
        self._hora_volta_do_invervalo
        self._hora_saida
        self._hora_inicio_extra
        self._hora_saida_extra
        self._data
        self._id_usuario

    def get_hora_entrada(self):
        return self._hora_entrada

    def set_hora_entrada(self, horario):
        self._hora_entrada = horario

    def get_hora_saida_ao_intervalo(self):
        return self._hora_saida_ao_intervalo

    def set_hora_saida_ao_intervalo(self, horario):
        self._hora_saida_ao_intervalo = horario

    def get_hora_volta_do_invervalo(self):
        return self._hora_volta_do_invervalo

    def set_hora_volta_do_invervalo(self, horario):
        self._hora_volta_do_invervalo = horario

    def get_hora_saida(self):
        return self._hora_entrada

    def set_hora_saida(self, horario):
        self._hora_saida = horario

    def get_hora_inicio_extra(self):
        return self._hora_inicio_extra

    def set_hora_inicio_extra(self, horario):
        self._hora_inicio_extra = horario

    def get_hora_saida_extra(self):
        return self._hora_saida_extra

    def set_hora_saida_extra(self, horario):
        self._hora_saida_extra = horario

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def get_id_usuario(self):
        return self._id_usuario

    def set_id_usuario(self, id_usuario):
        self._id_usuario = id_usuario
