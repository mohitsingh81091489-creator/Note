### lets countinue our file functions 
## firstly started how we can open aa file 
file = open("myfile.txt","r") 
data = file.readable()
print(data)

with open("myfile.txt", "r") as file: ##when you open this using,"with open" 
    ## ek khas baat darling ye hai ki aap ko esi ko close karne ki jaruart nahi padti hame ye automatically close ho jaaati hai 
    data = file.read()

print(data)
print ### my mistake from that i have learn one thing i use open my with "w" = this codw so when i write something it will erase all t6hat the last things 
file = open("myfile.txt","a")
data=file.write("I am the greatest of all time\n ") ### \n se you can write the thing in the new line 
## if use nnot use this \n your content will be write on the already exsisting contain
f=open("yourfile.txt","r")
data =f.read(8) ### i directly write that m.read but it does not print when i store this into data then it will print in the output 
print(data) 
print(type(data))
f.close() ### for the type of the data
## we can also read some specific part also like i want to read only 5 letter 
## mera doubt and question ye hai ki jab mane bina close kiye same naam
##  se file bnai or uske kuch words likhe to ye kaam nahi kar 
f= open("yourfile.txt",'r')
line1 = f.readline()
print(line1)
line2 =f.readlines(1) ## jo phele hi read hogya tha vo print nahi huva aap ne dekha hi hoga ye to 
print(line2)
f=open("yourfile.txt","a")
f.write("\nthari mari hai bhai ")
with open("new guys.txt","w")as fm:
    data =fm.write(" you are the new boy here ")

### nwo we have to hand on "r+" mood ess me aap read bhi kar skte hai and write bhi kar skte hai
## " ar jo write hoga vo starting me aajaye ga and overwrite hojye ga starting ye words pe"
## you can try 
### our last operation for deleteing a file 1. phele hume ek module donwload 
### karna hoga "import os",then we have do 2.step that is os.remove("file name ") 
import os
os.remove("new guys.txt") ## as you can see guys this will delete from this code 