### function = bar bar hume ek kaam karana ho value change hoo ri ho 
### instead of writing that code several time we can use function
def sum (a,b):  ### guys it works, firstly find what we did mistake last time 
    sum = a+b
    return sum
print(sum(2,3))
def multi (a,b): ### our next function that we called it mulit function 
    multi = a*b
    print(multi)
    return multi
multi(4,5)
print(multi(3,4)) ## it print two times because use this using
###print function (apart from that we already def that print(multi) that why it primt two times 
multi(75,64) ## now it works properly 
### simple funda yrr phele "def _____():,, ___ = name of your function ,,()= parameter or we can say the value assign to them 
### it may be default some time 
#### but when we use it second time like in the in print()= jab hum yaha par ess ko use kar te hai to unn ko argument bol te hai 
### funct 2 type hote hai 
# 1. in bulid function ,2.user define function as we already use avove 
mmt= multi(11,123) ### return value ko variable me store kar ne ke badm mee humme print fun use karne ki koi jaruart nahi hoti 
mmt= multi(13,43) ###  bas humme argumnets ,value assgin kar ni padti hai 
### ab hum default parameters pe study kree gee ex.
def cal_prod(a =2, b= 3):
    print(a*b)
    return a*b 
cal_prod()## ek baat agar hum ne ye "bracket()" using nahi kiya to value print nahi hoga sooooo guys use that 
### as you see the upper output u can see that humne value nahi di to usnne default value le le hai that how it works 
### if u did not aasigin that value it error ex.
def cal_power(a,b):
    print(a**b)
    return a**b
cal_power(2,6)### IT WILL SHOW ERROR SO U CAN UNDERSTAND that i will assign value for that 
### ento aaj ke bohot hai for function chalo eb 
### eb apn log Recursion ke bare me study kare ge 
# why we use this for repeating functiion or we can when a function call itself reapetlly

def add(a,b):
    c=a+b
    print(c)
    return c

def factorial (n):
    if n == 0:
      return 1
    else :
        return n*factorial(n-1)
 ### lets try this using for loop
n= int(input("enter a number:"))
factorials =1
for i in range (1,n+1):
    factorials = factorials*1
    print("your factorial is ",factorials)