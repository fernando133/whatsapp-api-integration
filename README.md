# Instruções

## Premissa

Estar com Docker e Docker Compose instalados na máquina.

Na raiz utilziar o comando: ```docker-compose up --build -d```

## Migrates

```docker-compose exec api ./manage.py makemigrations```\
```docker-compose exec api ./manage.py migrate```

### Superuser
```docker-compose exec api ./manage.py createsuperuser```

### Acesso
```http://localhost:8000```\
```http://localhost:8000/admin```

# Verificação de Código

### Instalar
```apt-get install pre-commit```

Dentro do diretótio executar:
```pre-commit install```

### Rodar hooks de pre-commit em todos os arquivos
```pre-commit run --all-files```\

# Informações Úteis

### Comandos úteis para docker
https://www.codenotary.com/blog/extremely-useful-docker-commands/

### Processo gitflow
https://medium.com/trainingcenter/utilizando-o-fluxo-git-flow-e63d5e0d5e04
