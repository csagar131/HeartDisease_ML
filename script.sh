#!/bin/bash
apt update

apt upgrade -y yes

apt install vim -y

apt install apache2 -y

systemctl start apache2

systemctl enable apache2

apt-get install mysql-server -y

apt install python3-pip -y



pip3 install pandas
pip3 install numpy
pip3 install sklearn
pip3 install matplotlib
pip3 install sklearn
pip3 install googlemaps
pip3 install folium
pip3 install mysql_connector


a2enmod cgid
systemctl restart apache2

setenforce=0


git clone https://github.com/csagar131/HeartDisease_ML

cp /root/HeartDisease_ML/*.html /var/www/html/
cp /root/HeartDisease_ML/*.jpg /var/www/html/
echo "copying to /www/html successful"

cp /root/HeartDisease_ML/*.cgi /usr/lib/cgi-bin/
cp /root/HeartDisease_ML/*.py /usr/lib/cgi-bin/
echo "copying to /cgi-bin/ successful"


dbname='users'
dbuser='dbuser'
passwd='Resi*123'



# Functions
ok() { echo -e '\e[32m'$dbname'\e[m'; } # Green

#EXPECTED_ARGS=3
#E_BADARGS=65
MYSQL=`which mysql`

Q1="CREATE DATABASE IF NOT EXISTS $dbname;"
Q2="GRANT ALL ON *.* TO '$dbuser'@'localhost' IDENTIFIED BY '$passwd';"
Q3="FLUSH PRIVILEGES;"
SQL="${Q1}${Q2}${Q3}"

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: $0 dbname dbuser dbpass"
  exit $E_BADARGS
fi

$MYSQL -uroot -p -e "$SQL"

ok "Database $dbname and user $dbuser created with a password $passwd"




uname='sagar'
passwd='sagar'
fname='sagar'
lname='chouhan'


mysql -uroot -proot users << EOF
create table login(username varchar(30) primary key not null,password varchar(30) not null,fname varchar(30),lname varchar(30));
insert into login (username,password,fname,lname) values ('$uname','$passwd','$fname','$lname');
EOF






