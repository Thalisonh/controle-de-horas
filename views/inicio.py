from controller.UsuarioBean import UsuarioBean
from models.entities.Usuario import Usuario


def main():
    usuario = Usuario()
    usuario_bean = UsuarioBean()

    usuario.set_nome("Thalison Henrique Morais Silva")
    usuario.set_email("thalison_henrique@hotmail.com")
    usuario.set_cpf("41455310867")
    usuario.set_data_nascimento("30/08/1996")
    usuario.set_senha("37246310")

    usuario_bean.update(usuario)

main()
