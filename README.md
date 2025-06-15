# EngenhariaSoftware
Repositório pessoal referente a minha parte (Backend) desenvolvimento pessoal 

#Docker: https://docs.docker.com/desktop/setup/install/windows-install/

#Postgre: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads 
(Baixar versao Windos ou mudar o .yml)\

*add o nas variavel de ambiente:
C:\Program Files\PostgreSQL\17\bin

Restaurar o backu.sql para o banco 

psql -U postgres -d bd -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

caso nao exista

psql -U postgres -c "CREATE DATABASE bd;"

caso nao exista:

psql -U postgres -c "CREATE DATABASE bd;"


psql -U postgres -d bd -f backup.sql


