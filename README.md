# EngenhariaSoftware
Repositório pessoal referente a minha parte (Backend) desenvolvimento pessoal 

#Docker: https://docs.docker.com/desktop/setup/install/windows-install/

#Postgre: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads 
(Baixar versao Windos ou mudar o .yml)\

*add o nas variavel de ambiente:
C:\Program Files\PostgreSQL\17\bin

Restaurar o backu.sql para o banco 

psql -U postgres -d bd -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

caso nao exista:

psql -U postgres -c "CREATE DATABASE bd;"


psql -U postgres -d bd -f backup.sql




*Linux{
(settings.py)

'HOST': os.environ.get('DJANGO_DB_HOST', 'localhost'),  

(docker-compose.yml)

environment:
      - DJANGO_DB_HOST=SEU_IP_DA_MAQUINA_HOST # Ex: 192.168.1.100 (o IP do seu Linux)
      
}


