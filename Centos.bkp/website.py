#!/bin/python

import os

service=os.system("systemctl status httpd")
if service == 0:
  print "httpd services are running"
elif service!=0:
  os.system("yum install -y httpd")  
  print "HTTPD is installed"

packages=os.system("which wget")
if packages == 0:
   print "WGET installed"
elif packages != 0:
    os.system("yum install -y wget zip")
os.system("systemctl restart httpd")
os.system("cd /tmp")
os.system("wget -o web.zip https://www.free-css.com/assets/files/free-css-templates/download/page235/agency.zip")
os.system("zip -xfv start*")
os.system("cd start*| mv * /var/www/html/")
os.system("systemctl restart httpd")

