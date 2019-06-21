#!/usr/bin/python3

import cgi, cgitb
import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



# Create instance of FieldStorage
form = cgi.FieldStorage()

gender = form.getvalue('gender')
age = form.getvalue('age')
cp = form.getvalue('cp')
trestbps = form.getvalue('trestbps')
chol = form.getvalue('chol')
fbs = form.getvalue('fbs')
restecg = form.getvalue('restecg')
thalach = form.getvalue('thalach')
exang = form.getvalue('exang')

oldpeak = form.getvalue('oldpeak')

slope = form.getvalue('slope')

ca = form.getvalue('ca')

thal = form.getvalue('thal')



# machine learning code

df = pd.read_csv('/var/www/cgi-bin/heart.csv')


features = df[['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']]
features = features.fillna(features.mean())
features = features.values
label = df[['target']].values



x_train,x_test,y_train,y_test = train_test_split(features,label,test_size=0.01,random_state=4)

clf = RandomForestClassifier(criterion='entropy',n_estimators=7)


trained = clf.fit(x_train,y_train)

predicted = trained.predict(x_test)



from numpy import array
a = array( [age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal] )


a.reshape(-1,1)


result = list(trained.predict([a]))[0]

#---------------------------------------------------------------------------------------------------------------------------

if result == 0:
	arrow = 1
elif result == 1:
	arrow = 2



from gplot import Gauge

labels = ['POSITIVE','NEGATIVE']
colors = ['#BA2F16','#45CE30']
#arrow = 1
title='Heart Disease Predictor'
fname = False
g = Gauge()
g.gauge(labels,colors, arrow, title,fname)



#-------------------------------------------------------------------------------------------------------------------------



a =''' 
<form action = '/cgi-bin/maps.cgi' method = "GET" >
<input class='box' type='text' placeholder='  Enter city' name='city' required /></br>
<input type='submit' value='Find Doctors' /></br>
</form>


'''



print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Heart Disease Predictor</title>')

print('</head>')
print('<body>')
print('<h1>Heart disease predictor is here where are you??\n\n</h1>')
if result == 0:
	print("<h2> You dont have heart disease. </h2>")
	print("<p>")
	print("<img src='http://13.232.35.109/negative.jpg'/>")
	print("</p>")
else:
	print("<h2> Ohh! You may have heart disease. </h2>")
	print("<p>")
	print("<img src='http://13.232.35.109/positive.jpg'/>")
	print("</p>")
	print(a)
	
print('</body>')
print('</html>')

