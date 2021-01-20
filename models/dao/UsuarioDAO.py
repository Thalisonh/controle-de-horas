from models.dao.Conexao import Conexao
from datetime import datetime


class UsuarioDAO(Conexao):

    def insert(self, usuario):
        data_atual = datetime.now()
        cursor = Conexao.conecta(self)
        query = f"INSERT INTO usuarios(idusuarios, nome, email, cpf, data_nascimento, senha, ativo, data_criacao) VALUES (0, '{usuario.get_nome()}', '{usuario.get_email()}', '{usuario.get_cpf()}', '{usuario.get_data_nascimento()}', '{usuario.get_senha()}', 1, '{data_atual}') "
        cursor.execute(query)
        print(query)
        Conexao.desconecta(self)

    def find(self, usuario):
        cursor = Conexao.conecta(self)

        query = f"SELECT * FROM usuarios"

        Conexao.desconecta(self)

    def update(self, usuario):
        cursor = Conexao.conecta(self)

        query = f"UPDATE usuarios SET CPF = '{usuario.get_cpf()}' WHERE email = '{usuario.get_email()}'"
        cursor.execute(query)
        print(query)
        Conexao.desconecta(self)

    def login(self, email, senha):
        cursor = Conexao.conecta(self)
        resultado = False

        query = f"SELECT idusuarios FROM usuarios WHERE email = '{email}'  AND senha = '{senha}'"
        try:
            cursor.execute(query)
            resultado = cursor.fetchall()
            print(resultado)
        except:
            print("falha")
        Conexao.desconecta(self)

        return resultado


