[![Build Status](https://travis-ci.com/ffabiorj/desafio_vendas.svg?branch=master)](https://travis-ci.com/ffabiorj/voluntario_app)

[![codecov](https://codecov.io/gh/ffabiorj/desafio_vendas/branch/master/graph/badge.svg)](https://codecov.io/gh/ffabiorj/voluntario_app)

# Api de voluntários

Criação de uma api de voluntários

## Tools

- Django
- Django Rest FrameWork
- Postgres
- Docker

## Há duas maneiras de roda o projeto localmente:

### Sem docker.

1. Clone o repositório.
2. Entre na pasta.
3. Crie uma um ambiente de desenvolvimento com python 3.8.
4. Ative o ambiente.
5. Instale as dependências.
6. Crie um arquivo .env
7. Rode as migrações
8. Rode o projeto
9. Acesse o link

```
- git clone git@github.com:ffabiorj/voluntario_app.git
- cd voluntario_app
- python3 -m venv .venv
- source .venv/bin/activate
- pip install -r requirements-dev.txt
- python contrib/env_gen.py
- python manage.py migrate
- python manage.py runserver
- http://127.0.0.1:8000/api/v1/acao/
```

### Com Docker e Docker Compose

1. Crie um arquivo .env
2. Crie um build do docker
3. Roda o docker Compose

```
- python contrib/env_gen.py
- docker-compose build
- docker-compose up
```

## Endpoints da api

- http://127.0.0.1:8000/api/v1/voluntario/ # Retorna todas voluntario ou cria uma.
- http://127.0.0.1:8000/api/v1/voluntario/id/ # Retorna, delete o update um voluntário.
- http://127.0.0.1:8000/api/v1/acao/ # Retorna todas ações ou cria uma.
- http://127.0.0.1:8000/api/v1/acao/id/ # Retorna, delete o update uma acao.

### Rodar os testes

```
pytest
```

### Links para as ferramentas utilizadas

[Django](https://docs.djangoproject.com/)

[Django Rest Framework](https://www.django-rest-framework.org/)

[Codecov](https://codecov.io/)

[Travis](https://travis-ci.com/)

[Postgres](https://www.postgresql.org/)

[Docker](https://www.docker.com/)
