#!/bin/python

import os

service=os.system("systemctl status httpd")

if service==0:
  print "httpd is running"
elif service!=0:
  os.system("systemctl start httpd")
else:
 os.system("yum install httpd -y")
packages=os.system("which wget")

if packages==0:
 print "wget is installed"

os.system("yum install gzip -y")
os.system("ls -l")
os.system("wget -O web.zip https://www.free-css.com/assets/files/free-css-templates/download/page235/agency.zip")
os.system("unzip web.zip")
os.system("pwd")
os.system("cd start*| cp -r * /var/www/html/")
