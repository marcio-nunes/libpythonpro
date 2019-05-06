import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario

@pytest.mark.parametrize(
    'usuarios',
    [
        Usuario(nome='Marcio', email='marcio@nunes.com'),
        Usuario(nome='Luciane', email='luciane@oliveira.com')
    ],
    [
        Usuario(nome='Marcio', email='marcio@nunes.com')
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
        enviador = Enviador()
        enviador_de_spam = EnviadorDeSpam(sessao, enviador)
        enviador_de_spam.enviar_emails(
            'marcio@nunes.com',
            'Curso Python Pro',
            'confira os módulos fantásticos'
        )
    assert len(usuarios) == enviador.qtde_email_enviados
