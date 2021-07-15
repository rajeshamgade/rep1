# connect Database (sqllite3) using Python

# print(help(modules))


import sqlite3

myconn=sqlite3.connect('testdb')
'''
print("DataBase Created.......")

myconn.execute("create table test_table (id int primary key,name text not null,sal int);")
print ("Table Created Succesfully....")

myconn.execute("insert into test_table values(100,'Rajesh',2000);")
myconn.execute("insert into test_table values(200,'Manish',3000);")
myconn.execute("insert into test_table values(300,'kamal',4000);")
myconn.execute("insert into test_table values(400,'ravi',5000);")
myconn.execute("insert into test_table values(500,'Joy',6000);")
myconn.execute("insert into test_table values(600,'Nithin',7000);")

myconn.commit()
print("Data Inserted Succesfully......")
'''
mycursor=myconn.execute('select * from test_table')
import time
for  row in mycursor:
	print(row)
	time.sleep(1)

myconn.close()	
