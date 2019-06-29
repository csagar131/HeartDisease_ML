apt update

#    apt upgrade -y yes

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





