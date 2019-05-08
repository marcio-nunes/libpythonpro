import requests


def test_conexao_github():
    resp = requests.get('https://api.github.com/users/marcio-nunes')
    assert resp.status_code == 200

