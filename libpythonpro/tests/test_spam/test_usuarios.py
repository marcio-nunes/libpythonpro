from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Marcio', email='marcio@nunes.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Marcio', email='marcio@nunes.com'),
        Usuario(nome='Luciane', email='luciane@oliveira.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
