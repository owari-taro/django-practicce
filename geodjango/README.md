```
#docker 接続
docker exec -it geodjango-db-1 psql -U postgres 

postgres=# create user test;
CREATE ROLE        
postgres=# alter user test password 'test';
ALTER ROLE
postgres=# create database  geo_test encoding UTF8;

postgres=# grant all privileges on database geo_test  to test;
postgres=# \c geo_test 
geo_test=# create extension postgis;CREATE EXTENSION
```