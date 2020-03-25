"""
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

######################################################################################################
	Este programa se conecta a una base de datos mysql desde python y consulta de version del mysql.


		conn --> variable de conexion  a la base de datos recibe como parametro las siguientes variables: 
		host --> nombre del servidor mysql.
		user --> nombre de usuario mysql por default es root
		passwd --> contraseña del usuario por deafult no tiene contraseña
		db --> Nombre de la base de datos a la que te conectaras.
		cursor --> puntero que se usa para realizar consultas a la base de datos.
	
	Requerido
		instalar la biblioteca  pymysql con el comando pip
			-- pip install pymysql.

"""


import pymysql	#library required for connection to the database.  

#Configuration of the connection variable.
conn = pymysql.connect(
	
	host = "localhost", #server
	user = "root",		#user
	passwd = "",		#user password
	db = "mysql")		#database name

cursor = conn.cursor()  #connection pointer to the database.

cursor.execute("SELECT VERSION()") #executes the query to the database.

#print query result
for row in cursor:
	print(row)

cursor.close() #close the pointer to the database.
conn.close()   #close the connection to the database.