# Modelo de documentação do Sphinx

- [README file in English](../README.md)

Modelo de documentação do Sphinx para projetos Python. Confira a documentação gerada [aqui](https://mateusoliveira43.github.io/sphinx-documentation-template/).

# Qualidade

Para rodar as métricas de qualidade do modelo, é necessário instalar seus requisitos de desenvolvimento. Para instalá-los, execute
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
```
ou
```
poetry install --no-root
poetry shell
```

As métricas de qualidade do modelo são reproduzidas pelas etapas de integração contínua do projeto. Configurações das etapas de integração contínua descritas no arquivo `.github/workflows/ci.yml`.

## Linter

Para rodar o linter de código Python, execute
```
prospector .
```

Configurações do linter de Python descritas no arquivo `.prospector.yaml`.

## Formatadores de código

Para checar o formato das importações no código Python, execute
```
isort --check --diff .
```

Para formatar as importações no código Python, execute
```
isort .
```

Para checar o formato do código Python, execute
```
black --check --diff .
```

Para formatar o código Python, execute
```
black .
```

Configurações do isort e black descritas no arquivo `pyproject.toml`.

Para checar o formato de todos os arquivos do repositório, execute
```
ec -verbose
```

Configurações do formato dos arquivos descritas no arquivo `.editorconfig`.

## Varredura de vulnerabilidades de segurança
Check the documentation generated [here]().
Para checar problemas de segurança comuns no código Python, execute
```
bandit --recursive scripts
```

Para checar vulnerabilidades de segurança conhecidas nas dependências Python, execute
```
safety check --file requirements/dev.txt --full-report
```

## Documentação

Para checar a geração de documentação do código Python, execute
```
sphinx-apidoc -M -P -o docs/modules example
sphinx-build -W -T -v -n docs public
```

Para gerar a documentação do código Python, execute
```
sphinx-apidoc -M -P -o docs/modules example
sphinx-build -v -n docs public
```

Configuração do Sphinx no arquivo `docs/index.rst`.

# Licença

Esse repositório é licenciado sob os termos da [Licença MIT](../LICENSE).
