# Conexion database with Python
Athor: Edgard Díaz
Date: september 28th 2017

This program connects to a mysql database from python and queries version of mysql.
  conn -> database connection variable receives the following variables as parameters:
  host -> mysql server name.
  user -> default mysql username is root
  passwd -> user password by deafult has no password
  db -> Name of the database to which you will connect.
  cursor -> pointer that is used to query the database.

Requires
  install the pymysql library with the pip command
  - pip install pymysql.
