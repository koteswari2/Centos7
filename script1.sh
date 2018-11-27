#!/bin/sh
echo
echo "Hello World"
echo "welcome to bash script"
echo
PACKAGE="httpd wget unzip"
SVC='httpd'
DOC='/var/www/html'
echo
echo "###################"
echo "install Software"
yum install $PACKAGE -y
echo
echo "**************************"
echo "Software installed Successfully"
echo
echo
echo "Service restart"
echo "Please Provide your URL:"
read URL
echo
echo "Provide Directory:"
read DIR
systemctl start $SVC
echo
wget -O web.zip $URL
echo
echo"######################"
echo "Downloaded Artifact"
echo
unzip web.zip
echo
cd $DIR
cp -r * $DOC/
echo
systemctl restart $SVC
echo
ip addr
echo
echo "Competed"
