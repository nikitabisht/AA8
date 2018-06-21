#question1

print("we represent time in a way that's easy for us understand . python stores it in tuples. these python tuples are made of nine numbers"
      " index (0) field (years) value(1995)"
      " index (1) field (Month) value (1to12)"
      "index (2) field (Day) value (1to31)"
      "index (3) feild (Hour) value (0to23)"
      "index (4) field (Mnutes) value (0to59)"
      "index (5) field (Second) value(0to61)"
      "index (6) field (Day of week) value (0to6)"
      "index (7) field (Day of year) value (1 to 366)"
      "index (8) field (DST) value (-1,0,1) ")


#question2

import datetime
d=datetime.datetime.now().strftime('%H : %M : %S')
print(d)

#end

#question3

import datetime,time
a=(input("today is"))
d= datetime.date.today()
print(d.month)

#question4

import datetime,time
a=(input("today is"))
d= datetime.date.today()
print(d.day)

#end

#question5

import datetime
d=datetime.date.today()
d.strftime("%d%m%Y")
print(d.day)

#end

#question6

import time
localtime = time.asctime(time.localtime(time.time()))
print ("local current time :" , localtime)

#end

#question7

import math
a= int(input("enter the number"))
print(math.factorial(a))

#end

#question8

import math
a= int(input("number:"))
b= int(input("number:"))
print(math.gcd(a,b))

#end

#question9

import os
print(os.getcwd())
print(os.environ)

#end