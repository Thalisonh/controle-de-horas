from models.dao.Conexao import Conexao
from datetime import datetime


class UsuarioDAO(Conexao):

    def insert(self, usuario):
        data_atual = datetime.now()
        cursor = Conexao.conecta(self)
        query = f"INSERT INTO usuario(idusuario, nome, email, data_nascimento, senha, data_criacao) VALUES (0, '{usuario.get_nome()}', '{usuario.get_email()}', '{usuario.get_data_nascimento()}', '{usuario.get_senha()}', '{data_atual}') "
        cursor.execute(query)
        print(query)
        Conexao.desconecta(self)

    def busca(self, usuario):
        cursor = Conexao.conecta(self)

        query = f"SELECT * FROM usuario"

        Conexao.desconecta(self)

    def update(self, usuario):
        cursor = Conexao.conecta(self)

        query = f"UPDATE usuario SET CPF = '{usuario.get_cpf()}' WHERE email = '{usuario.get_email()}'"
        cursor.execute(query)
        print(query)
        Conexao.desconecta(self)


