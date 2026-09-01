## we have a question finding a the sum of numbers 
## lets do guys
### lets find out factroial of n number
## we have do some mistake lets try again
i=10
(i-i) == 1 
for i in range(i,(i-i),-1):
    print(i*(i-1)*(i-2))
    i-=1 
frut = ["ap","pyap","map","orang","banana ","bas aaj ke list itna bohot hai "]
for fru in frut:
    print(fru)
numbers = [10,20,30,40,50,60,70,80,90,100]
for num in numbers:
    if num == 30:
        print("your number is found",num) ### ye concept yaad rakhana this is for finding a number in list 
        
        break
    ### lets try something for string in list
name_students=["mohit singh","rohit singh","kushal kumar meena","aadi","palak","payal","priya"]
for name in name_students:
    if name == "palak":
        print("your good name is bro",name)
    else :
        print(" your name is not found",name)
        break
i=1
new_numbeer = [10,10,20,30,40,10]
for num in new_numbeer:
    if num ==10:
        print("number of times your digit",i,num) ## 
        i+=1
### next question for finding greatest number in a list 
## lets do it
for name in name_students: ### ye countinue function hai for 
    ###2.skiping something if you have skip a particular part then use countinue function 
    if name == "palak":
        continue
    print("your good name",name)
## practice question on filI/O
## lets start kar te hai ab hum 
with open("testfile.txt","w+")as tf:
    data =tf.write("hi everyone\n " \
    "we are learning file\os\n"
    "using java\n"
    "i like programing java\n")
print(data)
with open("testfile.txt","r")as f:
    data =f.read()
    newdata=data.replace("java","python") #3 revise these
    ## concpect ("first the term that we want to replace","then the word that we need to replace with that  ")
    print(newdata) ## phele mane ek mistake ki thi "data.replace ko ek new variable 
    ## me store in kiya tha ess liye ab ess ne same value print kar de thi 
 ### ek khas baat aur jab humne read me replace kiya tab ye replace to hogya and output me hame esne show bhi kar diya 
 ## par jab tak humne "write wala function us enahi kiya to ye txt file me cahnge nahi show kare ga uss ke liye we have to use right mode"
with open("testfile.txt","w")as f:
    f.write(newdata)  ## if we do that directly our full data will erase and we have to write every thing from start 
word =" learning"
with open("testfile.txt","r")as f:
   data = f.read()
   if data.find(word)!= -1:
       print("your word is found in this file ")
   else:
       print("your word is not that file")
def check_forline(): ### yaha se hamara function start hota hai 
    word = " learning"
    data= True
    i =1
    with open("testfile.txt","r")as f:
        while data:
            data = f.readline()
            if(word in data):
                print(i)
                i+=1
            else:
                print("your word is not found")


