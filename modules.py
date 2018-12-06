#!/bin/python

import os

service=os.system("systemctl status httpd")

if service==0:
  print "httpd is running"
elif service!=0:
  
 os.system("yum install httpd -y")
 os.system("systemctl start httpd")

os.system("yum install gzip -y")
os.system("ls -l")
os.system("wget -O web.zip https://www.free-css.com/assets/files/free-css-templates/download/page235/rex.zip")
os.system("unzip web.zip")
os.system("pwd")
os.system("cd Mark*")
os.system("pwd")
os.system("mv ~/git/Mar*/* /var/www/html/")
os.system("systemctl restart httpd")
