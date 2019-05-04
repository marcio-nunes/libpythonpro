# libpythonpro
Usando a lib requests para buscar o avatar do uauário Github.

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