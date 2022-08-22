# Anotações


## Iniciar um projeto

#### Criação de um ambiente virtual:

**`python3 -m venv nome-env`**

#### Ativar o ambiente:

**`env/Scripts/activate`**

## Criação da aplicação

Para criar aplicação é preciso ir até o repositório que eu quero criar.

#### Criação do projeto:

**`djando-admin startprojetect nome_projeto`**

# Apps:


**`django-admin startapp nome_app`**


## No Pycharm

### Configuração do projeto:

1. **Ir até Project Interprete**: Para configurar o interpretador do Python;
1. **Show All..**: Para mostrar todos os interpretadores do Python;
1. Escolhe o interpretador e clica em **'ok'**.

### Manage:

1. Clicar em **'manage'**;
1. Edite Configurations;
1. Parameters: `runserver` ;
1. Clicar em **'apply'**;
1. Clicar em **'ok'**.

# Criação Tabelas:

No terminal do Pycharm!!

#### Cria as tabelas:

**`python manage.py migrate`**

#### Criação de admin

Após criar as tabelas é necessário criar o usuário admin, para poder acessar as
tabelas e os usuários.

**`python manage.py createsuperuser --username nome_usuario`**


# Migrar Tabelas:

Após ter criado um modelo de tabela, dentro do arquivo models.py, é preciso migrar
essa tabela para o banco de dados, fazer com que a class criada vire uma tabela no banco.

Antes de iniciar o comando é preciso instalar ele no arquivo **settings.py**, na
parte de **INSTALLED_APPS**, ai só adicionar lá o **nome da aplicação**.


Ai no terminal rodar o comando:

**`python manage.py makemigrations nome_app`** 

Gerar o SQL para migração:

**`python manage.py sqlmigrate nome_applicacao numero`**

O número após o nome da aplicação é do arquivo quando ele é gerado, é muito importante
colocar ele, para reconhecer qual tabela vai ser migrada.

Agora sim, para implementar no banco de dados:

**`python manage.py migrate nome_applicacao numero`**
