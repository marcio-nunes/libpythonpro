import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.parametros_de_envio = None
        self.qtd_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Marcio', email='marcio@nunes.com'),
            Usuario(nome='Luciane', email='luciane@oliveira.com')
        ],
        [
            Usuario(nome='Marcio', email='marcio@nunes.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'marcio@nunes.com',
        'Curso Python Pro',
        'confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_emails_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Marcio', email='marcio@nunes.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciane@oliveira.com',
        'Curso Python Pro',
        'confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'luciane@oliveira.com',
        'marcio@nunes.com',
        'Curso Python Pro',
        'confira os módulos fantásticos'
    )