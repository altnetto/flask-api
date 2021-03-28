Aqui, irei definir algumas informações acerca do projeto, de tal modo que sirva como um guia também

Para gerar a imagem docker correta, fazer

>> docker run --name pglocal -e "POSTGRES_PASSWORD=admin" -p 5432:5432 -d postgres

As flags do comando fazem o seguinte:

- e: define a variável do ambiente do postgres de senha

- p: define os relacionamentos de comunicação entre portas do sistema (porta local : porta docker)

--name: define o nome do container. Caso isso não seja definido, será gerado um nome aleatório
---------

Para rodar o docker

>> docker start pglocal

---------

Para acessar o ambiente do docker 

>> docker exec -it pglocal bash

---------

Para acessar a shell do banco de dados:

>> psql -U postgres

---------

Para verificar os bancos de dados internos

>> \l

---------

Para criar um banco de dados

>> create database nome_do_banco;

*** Nesse caso, iremos utilizar:

>> create database flask_contacts;

----------

Para conectar ao banco de dados em específico

>> \connect nome_do_banco;

----------

Para detalhar as tabelas (detail)

>> \dt

----------