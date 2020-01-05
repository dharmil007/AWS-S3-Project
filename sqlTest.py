import mysql.connector
from datetime import date


dates = date.today()

try:
    myDB = mysql.connector.connect(
        host = "uspl-db01.cdqeogcqmqye.us-east-1.rds.amazonaws.com",
        port = "3377",
        user = "uspl_backup",
        passwd = "*d!X5b*@z8",
        database = "BACKUP_TEST"    
    )

    mycursor = myDB.cursor()
    print("DB Connected")
except Exception as s1:
    print ("Cant connect to database",s1)
    quit()

try:
    sqlCreate = "CREATE TABLE IF NOT EXISTS test1 (id INT AUTO_INCREMENT primary key , name varchar(255), dob DATE, location varchar(255), salary INT, height VARCHAR(255), SSN INT)"
    mycursor.execute(sqlCreate)
    print ("Tabel Created")
except Exception as S2:
    print ("Cannot create table",S2)
    quit()

try:
    sqlInsert  = "INSERT INTO test1 (NAME, DOB, LOCATION, SALARY, HEIGHT, SSN) VALUES (%s, %s, %s, %s, %s, %s)"
    val = ("SAGAR", "1992-25-56", "DELHI, INDIA", 50000, "5.11", 798896563)
    mycursor.execute(sqlInsert, val)
    myDB.commit()
    print ("DATA Inserted")

except Exception as s3: 
    print ("Cannot insert into db",s3)
    quit()


mycursor.close()
myDB.close()

