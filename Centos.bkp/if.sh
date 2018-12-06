#!/bin/bash
if [ $1 -gt 100 ]
then
   echo "First Arg is greater than 100"
   echo
   echo "####Memory size###"
   free -m
elif [ $1 -lt 60 ]
then
    echo "greater than 50 and lesser than 100"
   echo
 
else
   echo "less than 50"
fi
   date
   pwd
