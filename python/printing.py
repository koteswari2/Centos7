#!/bin/python
formater = "%r %r"
print formater % (3, 4)
print formater % (formater, formater)

days = "Mon Tue Wed Thu Fri Sat Sun"
print days

numbers = "1, 2, 3, 4"
print  numbers

Month = raw_input()
Days = raw_input()
print "%s having %r days" % (Month, Days)
if Days == 28:
  print "Month is leap yea %s" % (Month)
