#!/bin/python

print "WELCOME TO PYTHON PRACTISE SESSION"
print "######## String ###########"
teststr='Hello DevOps!'
print teststr
print teststr[0]
print teststr[0:5]
print teststr[6:12]
print teststr[3:]
print teststr *2
print teststr + " Hola"
print "**completed**"
print ""
print ""

print "########  list ###########"
list1=['ansible', 'puppet', 1111, 86.96, 'git', 'aws']
list2=['miner','boy']
print list1
print list1[0]
print list1[-1]
print list1[2:4]
print list1[3:]
print list1*2
print list1 + list2
print list2*2
print " "
print " "


print "########  Tuple ###########"
list1=['ansible', 'puppet', 1111, 86.96, 'git', 'aws']
tuple1=('ansible', 'puppet', 1111, 86.96, 'git', 'aws')
tuple2=('miner','boy')
print tuple1
print tuple1[0]
print tuple1[1:3]
print tuple1 + tuple2
print tuple2*2
tuple=('ansible', 'puppet', 1111, 86.96, 'git', 'aws')

list=['ansible', 'puppet', 1111, 86.96, 'git', 'aws']
#tuple[5]='terra'
#list[5]='terra'

dict1={}
dict1['profile']="superman"
dict1['passcode']="zeus"
dict2={'name':'siva', 'age':30,}
print dict1['profile']
print dict2
print dict2.keys()
print dict2.values()

a=10
b=20

if (a==b):
 print "a is equal to b"
else:
 print "a is equal to b"
if (a!=b):
 print "a is not equalto b"
if (a>b):
 print "a is greater than b"
if (a<b):
 print "a is lesthan b"

#if elif else example

num=10
if num > 100:
 print "Number is greaterthan 100"
elif num < 100:
 print "Number is lessthan 100"
else:
 print "Value of numb is equal to num"

#WHILE LOOP

num=110
while num>100:
 print 'Hello',num
 num=num+1
 if num==111:
    break
print "Break test completed"

count = 0
while count<19:
 count=count+1
 if count==10:
   continue
 print 'value is:',count
print "bye"

a =  10
while a>0:
 a=a-1
 if a==5:
   continue
 print 'current value is:',a
print "bye!!!"
  

