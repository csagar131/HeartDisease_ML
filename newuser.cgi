#!/usr/bin/python3

# Import modules for CGI handling
import cgi, cgitb

#mysql database connectivity

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="dbuser",
  passwd="Resi*123",
  database="users"
)

mycursor = mydb.cursor()
mycursor.execute("select * from login")
myresult = mycursor.fetchall() # it gives the list

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('uname')
password  = form.getvalue('passwd')
repassword = form.getvalue('repasswd')

#fname = form.getvalue('firstname')
#lname = form.getvalue('lastname')

username = "'"+username+"'"
password = "'"+password+"'"





fname = 'null'
lname = 'null'




#if password == repassword:
query = 'INSERT INTO `login` VALUES ('+username+','+password+','+fname+','+lname+')'



result  = mycursor.execute(query)
mydb.commit()



print("Content-type:text/html\r\n\r\n")
print('<script>window.location.href="http://13.232.35.109/index.html";</script>')

