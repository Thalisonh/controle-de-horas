from models.dao.HorariosDAO import HorariosDAO


class HorariosBean:
    horarios_dao = HorariosDAO()

    def __init__(self):
        self.horarios_dao

    def insert(self, horario):
        self.horarios_dao.insert(horario)

    def insert_base(self, horario):
        self.horarios_dao.insert_base(horario)

    def update(self, horario):
        pass

    def remove(self, horario):
        pass

    def prepare_to_insert(self, horarios):
        pass


