#!/bin/python


''' Example for module '''

def add(val1,val2):
    total=val1+val2
    return total

def sub(val1,val2):
    subract=val1-val2
    return subract

import os

exitcode = os.system("yum --help")

if exitcode ==0:
   print "RHEL Family detected"
   os.system("yum update -y")
elif exitcode!=0:
   print "Not a RHEL Famile"
   os.system("apt update")
else:
   print "unsupported OS"
