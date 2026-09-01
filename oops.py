### from zero 
## lets start with every thing
class student:
    name="mohit singh"
s1=student()
print(s1)
print(student.name) ## ye to m ye likh sakta hoon ya fir 
print(s1.name) ## it depend on me wheter which one i need to choose 
### now we will discuss about constructor 
# every class have a function we called it init function 
class new_student:
    name= "rohit singh"
    def __init__(abcd): 
        ## yaha par self likh na important hota hai without that its not working
        ## yaha par hum self ke alav bhi likh sakte hai par every programer write self so we also have to write that 
        print("you are new student\n","please enter your name in this form ")
s1=new_student()
## "self" is our first parameter other then that we can also take other parameter
#example 
class old_student: ## as you can see that 
    def __init__(self,fullname,subject,course):
     self.naamaapka =fullname
     self.yfsub=subject
     self.cor =course 
s1=old_student("deepak","maths","b.tech")
print(s1.naamaapka,s1.yfsub,s1.cor) ### ek baat ye bhi yaad rakho ki self."jo naam yaha par 
##likh tha vo hi naam you have to write when you have to print that ",otherwise it will show you error or value is not assgin 
 ## doubt
 ## parametrized constrouctor
class old_student:
   def __init__(self,fullname,subject,course):
      self.name =fullname
      self.yrsub=subject
      self.course=course 
s1=old_student("maths","b.tech","rohitss")
print(s1.name,s1.yrsub,s1.course) ## you cannot change the sequence because it directly store value according sequence 
## ek hov hai defalt and  ek hov hai parametrized constrouctor
### ye default constructor
def __init__(self): ## do chij yaad rakhi ye class attribute ,object attribute
   pass  #3 jo chij common hai hum uss class atribute bana de hai kyui memory ek baar store ho 
## class and instance attributes
## jis ki har value different hoti we use self."paramater" beacuse we have to assgin different different value to this 
# self.name = to har student ka name different hoga ess liye 
## or koi chijj sab me common hai jise collage name so hum hamri
#  class ke blue print m uss ko add kar de ge taki hame baar baar naa likha pade 
class car:
   brand= "rolls royce" # ye class ka attribute hai 
   color = 'black' # class atribute or object atribute me hum object attribute ko jayada priority de hai 
   ## yani agar object atribute pe jo likha gaya vo final answer hai ,or agar es pe koi value nahi de to class atribute se ye vlaue le gaa
   def __init__(self,color,brand):
       self.color = color  
       self.brand = brand
c1=car("mayback","white")
print(c1.color,c1.brand) ## as u can see the output ## mayback white## 
## Methods in class 
# class me duu chij store ho sakti hai ek to data(attributes) and second.Methods
# method = simple meaning function in class 
class newcar:
   def __init__(self,csname,color,price):
      self.csname = csname
      self.color = color
      self.price = price

   def welcome(self): ##c and we learn from our mistake 
         print("hello sir",self.csname)
c1= newcar("rohit","blue","10cr")
c1.welcome()
class bankale_boys:
   def __init__(self,name,course,day):
      self.name=name
      self.course=course
      self.day=day
   def mojaale(self):
      print("tham ve log ho jo bank mar rahe ho",self.name,"aur humara course hai",self.course)
b1=bankale_boys("Mohit singh","b.tech(ai&ml)","wednesday")
b1.mojaale()
## now we are going to study static methods
# in static method we do not use self parameter 
# example ,simple ye hai ki static me hame self use karne ki koi h=jarurat nahi hai 
class chota_kuchupuchu:
   def __init__(self,name,age):
      self.name=name
      self.age=age
   @staticmethod
   def hello():
      print("hello chote kuchu puchu",  "aap ki age kya hai ") ## wew cannot use self aalo parametr in this ,
      #yase m purwale self ko call kar raha tha it not work at there 
b1=chota_kuchupuchu("palak",13) # we can not call object function in this in this staticmethod
b1.hello()
## now we will study abstraction and capsulaction 
# abstraction = simple baat ya hai jase car ke andar ke engine hide hota hai aur we dont have 
# any idea what is going in that engine,the same way we will hide aur unessary 
# things from that code and only show important things to the user in an "class" remeber this for class
class car:
   def __init__(self): ## ye es ka example hai 
      self.acc=False
      self.brk=False
      self.clutch=False
   def start(self):
      self.acc=True
      self.clutch=True
      print("car started ......")
car1=car()
car1.start()
## capsulaction 
# simple words me 
# caplsulaction = [data + function ] in a single unit that is called capsulaction 
# for deleting object in the class "we use "del objectname" ex del s1",s1= student s1,student me store hone wali value 
class tharonam:
   def __init__(self,name):
      self.name=name
      print("your name",self.name)
thro1=tharonam("rohti singh")
del thro1
print(thro1.name) ## u can see that yoo delete ho rr bhaio
      

