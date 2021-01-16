import mysql.connector


class Conexao:
    def __init__(self):
        self._conexao = mysql.connector.connect(
            user='root',
            password='password',
            host='localhost',
            database='banco_de_hora_python',
        )

    def conecta(self):
        try:
            cursor = self._conexao.cursor()
            print("Conectado")
        except:
            print("Erro na conexão")

        return cursor

    def desconecta(self):
        print("Desconectado")
        self._conexao.commit()
        self._conexao.cursor().close()
        self._conexao.close()
