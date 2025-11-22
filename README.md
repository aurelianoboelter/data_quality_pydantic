# workshop_02_aovivo

Visite minha documentacao

[![image](/pic/print.png)](https://lvgalvao.github.io/workshop_02_aovivo/)

1. Identificar bibliotecas que serão usadas:
. pyenv
. pydantic
. poetry
. pytest

Exemplo: consulta https://pandera.readthedocs.io/en/stable/ 
. pandera 
versões de python que serão aceitas no projeto
No caso o Pandera precisa do python 3.11, então será usada para iniciar o projeto




2. Configure a versão correta do Python com `pyenv` (versionar o python, multiplas versões de python):

```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Configurar poetry para Python version 3.11.5 e ative o ambiente virtual:
poetry resolver todos os problemas de path do windows

```bash
poetry init
poetry env use 3.11.5
poetry shell

```

4. Instale as dependencias do projeto:

```bash
poetry install --no-root
```
Obs: instala todas as dependências,
mas não instala o projeto atual como pacote.

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
poetry run task test
```

6. Execute o comando para ver a documentação do projeto:

```bash
poetry run task test
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
poetry run python app/etl.py
```


8. Executando mkdocs

```bash
poetry add mkdocs
mkdocs new .
poetry run mkdocs serve

```