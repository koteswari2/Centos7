#!/bin/python
teststr='Hello DevOps!'
print teststr
print teststr[0]
print teststr[0:5]
print teststr[6:12]
print teststr[3:]
print teststr *2
print teststr + " Hola"
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
