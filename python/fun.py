#!/bin/python

def print_test():
   print "Hello"
   print "Bollo"

def add_test(num1,num2):
   total = num1+num2
   return total


print print_test()
print add_test(2,5)

def print_details(Name,Age=3):
   print "Name:",Name
   print "Age",Age
   return 
print print_details("siva",43)

def movie(story,direction):
   movie=story + direction
   return movie
print movie("hari","vvv")

def sivainfo(name,age=30):
  print "Name is %s" %name
  print "Age is %d"  %age

sivainfo("siva",100)
