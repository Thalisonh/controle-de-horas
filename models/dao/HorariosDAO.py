from models.dao.Conexao import Conexao


class HorariosDAO(Conexao):

    def insert(self, horarios):
        cursor = Conexao.conecta(self)

        query = f"INSERT INTO horarios VALUES (0, {horarios.get_id_usuario()}, '{horarios.get_hora_entrada()}', '{horarios.get_hora_saida_ao_intervalo()}', '{horarios.get_hora_volta_do_invervalo()}', '{horarios.get_hora_saida()}', '{horarios.get_hora_inicio_extra()}', '{horarios.get_hora_saida_extra()}', '{horarios.get_data()}')"
        cursor.execute(query)
        #cursor.fetchall()
        Conexao.desconecta(self)

    def update(self):
        pass

    def find(self):
        pass


