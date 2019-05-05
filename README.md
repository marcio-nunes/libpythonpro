# libpythonpro
[![Build Status](https://travis-ci.org/marcio-nunes/libpythonpro.svg?branch=master)](https://travis-ci.org/marcio-nunes/libpythonpro)
[![Updates](https://pyup.io/repos/github/marcio-nunes/libpythonpro/shield.svg)](https://pyup.io/repos/github/marcio-nunes/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/marcio-nunes/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/marcio-nunes/libpythonpro/)


Usando a lib requests para buscar o avatar do uauário Github.
https://api.github.com/users/usuario
```bash
pip install requests
```
Se o ambiente virtual já existe, então
```bash
pip freeze > requirements.txt
```
Senão
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Utilizando libs somente no ambiente de desenvolvimento.
```bash
pip install flake8
pip freeze > requirements-dev.txt
```
Retirar as libs que já fazem parte do requirements.txt e acrescentar a importação do mesmo.
```
-r requirements.txt
```
Criar o arquivo de configuração .flake8 na raiz do projeto para excluir a pasta .venv e outras cofigurações.
```
[flake8]
max-line-length = 120
exclude=.venv
```
Para conferir o código.
```bash
flake8
```

# Travis - Integração Contínua
Automatizar tarefas usando o Travis com a conta do Github.
- Criar o arquivo de configuração .travis.yml na raiz do projeto.
    - a opção -q (quiet) oculta as instalações de dependências no log do Travis.
```
language: python
dist: xenial
sudo: true
python:
  - 3.7.2
install:
  - pip install -q -r requirements-dev.txt
script:
  - flake8
```
- Adicionar repositório (public) ao https://travis-ci.org/ ou https://travis-ci.com/ caso seja privado.

##Upgrade das dependências
Como saber caso haja um novo release de alguma lib usada no projeto?

Usar o https://pyup.io para automatizar as verificações de atualizações das dependências.

Emulando upgrade:
1. alterar requirements.txt com uma versão mais antiga da lib
2. desinstalar requests
```bash
pip uninstall requests
```
3. instalar uma versão anterior da lib
```bash
pip install requests==2.18.3
```
4. adicionar o Repo ao Pyup
    - adicionar o distintivo ao Readme
