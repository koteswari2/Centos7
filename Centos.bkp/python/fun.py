#!/bin/python

def print_test(Hello,*vartuple):
    print Hello
    for var in vartuple:
     print var
print_test(12,2)
print_test(1,2,3,4,5,6,7,8,9)

def add_test(num1,num2):
   total = num1+num2
   return total


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

def tuple_example(apple,*vartuple):
   print apple
   for var in vartuple:
    print var
   return
tuple_example(10)
tuple_example(1,2,3,4,5,6,7)
