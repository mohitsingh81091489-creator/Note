### in this chapter will discuss about loops concepts
### 1 .while loop and 2.is for loop 
### lets star with while loop 
i= 1
while i<=5 :
    print("hello Chotte bhai ")
    i+=1 ## ye baat yaad karkhna ki agr tum ne ye i+= 1 nahi kiya to ye ek infinite loop bn jaaye gaaa and if you not stop that
    ## your system will crashh 
### iterator = variable in loop
###    itreation = loop cycle 
i = 5 
while i<= 10:
    print("your next number is ",i)
    i+=1
### practice question for you guys 
# 1 1 to 100 count 
## 100 to 1 count 
### multiplication table for "n" for n number
# print[1,4,9,16,......,,100]
# print[search for 'x'in loop ]
## lets start guys 
i = 1 
while i<=10:
    print("your number is ",i) 
    i+=1
### first question is complete
i= 10
while i>= 1:
    print(" your reverse counting is this ",i)
    i-=1
## next question for print table 
n= 13
i = 1 
while i<= 10:
    print("your table is this ",i*n)
    i+= 1   
my_list = [1,4,9,16,25,36,49,64,81,100] ## this special case for print items in a list 
## yaad ye rakh naa ki jaise hum ne i liya tha unn me iss me hum items lena hoga if you not take at then it will show a error guys 
print(my_list[0])
for items in my_list:
    print(items)
    items+=1
x= 25
while items in my_list:
    items= x
print(" your number is found ",items)
### other then that we have do some mistaj=ke in the last one but in that we do that using something else method
veggy = ["patato","brinjal","tomato","apple","banaanna "]
for vag in veggy:
    print(vag)
for value in veggy:
 pass  ### ye pass function hai we use it when i write something like loop and else function and hum uss ko skip kara hoo so we use pass function 