# Sphinx documentation template

- [Arquivo README em português](docs/README_PT.md)

Template of Sphinx documentation for Python projects. Check the documentation generated [here]().

# Quality

To run the template quality measures, it is needed to install its development requirements. To install then, run
```
virtualenv .venv
source .venv/bin/activate
pip install -r requirements/dev.txt
```
or
```
poetry install --no-root
poetry shell
```

The quality measures of the template are reproduced by the continuos integration (CI) pipeline of the project. CI configuration in `.github/workflows/ci.yml` file.

## Linter

To run Python linter, run
```
prospector .
```

Python linter configuration in `.prospector.yaml` file.

## Code formatters

To check Python code imports format, run
```
isort --check --diff .
```

To format Python code imports, run
```
isort .
```

To check Python code format, run
```
black --check --diff .
```

To format Python code, run
```
black .
```

isort and black configuration in `pyproject.toml` file.

To check all repository's files format, run
```
ec -verbose
```

File format configuration in `.editorconfig` file.

## Security vulnerability scanners

To check common security issues in Python code, run
```
bandit --recursive scripts
```

To check known security vulnerabilities in Python dependencies, run
```
safety check --file requirements/dev.txt --full-report
```

## Documentation

To check Python documentation generation, run
```
sphinx-apidoc -M -P -o docs/modules example
sphinx-build -W -T -v -n docs public
```

To generate Python documentation, run
```
sphinx-apidoc -M -P -o docs/modules example
sphinx-build -v -n docs public
```

Sphinx configuration in `docs/index.rst` file.

# License

This repository is licensed under the terms of [MIT License](LICENSE).
