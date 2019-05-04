# libpythonpro
[![Build Status](https://travis-ci.com/marcio-nunes/libpythonpro.svg?token=Sz9oyCVW8oMiJ5wFzrrY&branch=master)](https://travis-ci.com/marcio-nunes/libpythonpro)

Usando a lib requests para buscar o avatar do uauário Github.
https://api.github.com/users/marcio-nunes
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

#Travis - Integração Contínua
Automatizar tarefas usando o Travis com a conta do Github.
- Criar o arquivo de configuração .travis.yml na raiz do projeto.
    - a opção -q (quiet) oculta as instalações de dependências do log do Travis.
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
- Adicionar repositório ao https://travis-ci.org/ se o repositório for público ou https://travis-ci.com/ caso seja privado.

##Upgrade das dependências
Como saber caso haja um novo release de alguma lib usada no projeto?

Emulando upgrade:
- alterar requirements.txt com uma versão mais antiga da lib
- desinstalar requests
```bash
pip uninstall requests
```
- instalar uma versão anterior da lib
```bash
pip install requests==2.18.3
```