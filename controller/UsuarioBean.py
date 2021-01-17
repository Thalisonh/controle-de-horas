from models.dao.UsuarioDAO import UsuarioDAO
from models.entities import Usuario


class UsuarioBean:
    usuarioDAO = UsuarioDAO()

    def __init__(self):
        self.usuarioDAO

    def insert(self, usuario):
        print(f"Bean {usuario.get_nome()}")
        self.usuarioDAO.insert(usuario)

    def update(self, usuario):
        self.usuarioDAO.update(usuario)

    def login(self, email, senha):
        id_usuario = self.usuarioDAO.login(email, senha)

        id_usuario = id_usuario[0]
        #print(f'{teste[0]} teste')


        return id_usuario[0]

