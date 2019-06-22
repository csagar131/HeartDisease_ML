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
username = form.getvalue('Username')
password  = form.getvalue('Password')



for row in myresult:
        if (username == row[0]) and (password == row[1]):
                print("Content-type:text/html\n")
                print('<script>window.location.href="http://13.126.204.181/form.html";</script>')

else:
	print("Content-type:text/html\n")
	print("<h2>Username and Password Incorrect</h2>")
	#print(button2)


mycursor.close()


'''

if (username == myresult[0][0]) and (password == myresult[0][1]):
	
	print("Content-type:text/html\n")
	print('<script>window.location.href="http://13.232.35.109/form.html";</script>')
else:
	print("Content-type:text/html\n")
	print("<h2>Username and Password Incorrect</h2>")
	print(button2)

'''
