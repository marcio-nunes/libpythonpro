import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    # Setup - função geradora
    conexao_obj = Conexao()
    yield conexao_obj  # retorna o valor a ser injetado nos testes
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
