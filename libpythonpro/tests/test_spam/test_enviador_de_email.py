import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_cria_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com', 'marcio@nunes.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'luciane@oliveira.com',  # destinatario
        'Cursos Python Pro',  # assunto
        'Primeira turma aberta.'  # corpo do email
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'marcio.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'luciane@oliveira.com',  # destinatario
            'Cursos Python Pro',  # assunto
            'Primeira turma aberta.'  # corpo do email
        )