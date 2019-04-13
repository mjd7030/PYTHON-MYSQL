import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="password",
	database="TESTDB"
	) 

# TO MOVE CURSOR INSIDE DATABSE WITH PYTHON 
mycursor= mydb.cursor()

#TO CREATE DATABASE
mycursor.execute("CREATE DATABASE TESTDB")

# TO SEE ALL DATABASE 
mycursor.execute("SHOW DATABASES")
for i in mycursor:
	print(i)

# TO CREATE TABLE
mycursor.execute("CREATE TABLE users(name VARCHAR(255),email VARCHAR(255),age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
mycursor.execute("SHOW TABlES")
for i in mycursor:
	print(i[0])

# TO INSERT VALUES

sqlstuff = "INSERT INTO users(name,email,age) VALUES(%s,%s,%s)"
record1=("Maulik","asda@fadf.com",21)
mycursor.execute(sqlstuff,record1)
mydb.commit()

# FOR MULTIPLE RECORDS
sqlstuff = "INSERT INTO users(name,email,age) VALUES (%s,%s,%s)"
records = [("Vaibhav","adsfsda@fadf.com",19),
	("JMD","jmd@gmail.com",54),
	("KJD","KJD@gail.com",48),]

mycursor.executemany(sqlstuff,records)
mydb.commit()
mycursor.execute("SELECT * FROM users")
result = mycursor.fetchall()
print("NAME\t\tEMAIL ID\t\t\tAGE\tID")
for i in result:
	print(i[0]) #for only names 
	print(i)
	print("--------------------------")
	rint("%s\t\t" %i[0]+"%s\t\t\t" %i[1] +"%s\t" %i[2]+"%s" %i[3])
	

mycursor.execute("SELECT * FROM users WHERE age>20")
mycursor.execute("SELECT * FROM users WHERE name LIKE 'M%'")
result = mycursor.fetchall()
for i in result:
	print(i)


# AND / OR CLAUSES
mycursor.execute("SELECT * FROM users WHERE name LIKE '%i%' AND age > 30 OR user_id=1")
result = mycursor.fetchall()
for i in result:
	print(i)

# UPDATING RECORDS
mysql = "UPDATE users SET age = 53 WHERE name='JMD'"
mycursor.execute(mysql)
mydb.commit()


#LIMIT RESULTS
mycursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1") #offset: It will ignore offset value
result = mycursor.fetchall()
for i in result:
	print(i)

# ORDERING DESCending ORDER / ASC 			   age  ASC
mycursor.execute("SELECT * FROM users ORDER BY name DESC")

# DELETE RECORDS
mycursor.execute("DELETE FROM user WHERE user_id = 4")
mydb.commit()

# EXPORT THAT DATA IN CSV OR JSON AS A BACKUP COPY IN MYSQL WORKBENCH
# DELETE DROP TABLE

mysql = "DROP TABLE users"
mycursor.execute(mysql)
mysql = "DROP TABlE IF EXISTS users"