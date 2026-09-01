is_raining = False

if is_raining:
    print("Take an umbrella")
else :
    print("its not rainig bro ")
if "cat" == "Cat":
   print (True)
print("cat"== "Cat")## ess ka matalab python me upper and lower case ka bohot farak hota hai 
class new_student():
    pass




class Student: ## simple example without using self argumnet 
    name="mohit singh"
    collage ="singahinya unvirestiyu "
    fg= " m with p "
## s1 ki value hume store karani pade gi class student ki list m 
s1=Student() ## you have use the exact name if that class that you name that 
print(s1.name)## ab tum sikka naam print kara sakte hoo 
print(s1.collage,s1.fg)
class car:
    carbrand="rolls royce "
    carcolour="blue "
    type="luxury"
rcar1=car()
rcar2=car()
print(rcar1.carcolour,rcar2.carbrand)
## self ke function ke baare baat kar te hai ab 
class new_student:
  def __init__(self): ## mane kya galati ki thi "insted of writing "init" = i have write "int" so self call nahi huva bhaiyo
     print("you are our new student")
     
new1= new_student()
# 7 crore saval ka ye self aala function kaam kyu koni kar ro hai 
## 7 crore ka saval solve hogya mne init ko int likh diya tha 
## chalo new class bnate hai 
class luxurycar:
    def __init__(self,brand ,features,colur,type):
        self.brand=brand
        self.feature=features
        self.rang=colur
        self.type=type
        print("your car have this -",features)
        print("your car brand is ",brand)
        print("your car colur is ",colur)
        print("teri gadi ko type ye hai ladle ",type)
car1=luxurycar("rolls royce","comfort luxury fell when you sit that","black","luxury+sports")
print(car1)
class student:
    def __init__(self,physics,maths,chemistry): ### succesfull in my code and practice question 
        self.phy =int(physics)     ### i am the greatest of all time
        self.mat=int(maths)
        self.chem=int(chemistry)
    def average(self):
       newsum=(self.phy+self.chem+self.mat)
       print(newsum/3)
s1=student(98,94,93)
s1.average()
## another way to do that same question 
class studentname:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def staverage(self):
        sum=0
        for value in self.marks:
            sum+=value
        print("hi",self.name,"you have scored these marks",sum/3)
s1=studentname("tony stark",[53,87,76])
s1.staverage()            
class account: ## i need to practice that more question 
    def __init__(self,balance,accountno):## there is not proper concept clearity
        self.balance =balance
        self.account =accountno
    def debit(self,amount):
        self.balance=-amount
        print("rs",amount,"was debited")
        print("total amount",self.balance)
    def credit(self,amount):
        self.balance=+amount
        print("rs",amount,"was credited",self.balance)
        print("total amount",self.balance)
    def get_balance(self):
        return self.balance
acc1=account(5000,81091489)
acc1.debit(700)
acc1.credit(1800)


        

    