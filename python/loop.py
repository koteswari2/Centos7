#!/bin/python
count = 0

while (count < 12):
  print 'The count is:',count
  count=count+1

print "Good Bye!"

fruits=['banana', 'apple', 'mango']
for index in range(len(fruits)):
  print'Current fruit:',fruits[index]
print "Good bye!"

Numbers=['one', 'Two', 'Three', 'Four']
for numbers in range(len(Numbers)):
  print'Numbers are:',Numbers[numbers]

count = 101
while (count > 100):
 print "Numbers are:",count
 count=count+1
 if count == 111:
   break
for word in 'Python':
 if word == 't':
   continue
 print 'current letter:', word

a=10
while a>0:
 a=a-1
 if a == 5:
   continue
 print 'current variable value:',a
print "Execution completed!"

for word in "DevOps":
  print "Value of word is " + " " + word

for Places in ['Hyderabad', 'Pune', 'Chennai', 'Bangalore']:
  print "%s are Metropolitean city" % (Places)

fruits = ["Mango", "Apple", "Grappes"]
for i in range (len(fruits)):
  print "Value of i is " + str(i)

