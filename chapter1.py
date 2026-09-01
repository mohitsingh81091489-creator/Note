### learn dictionary and sets in this chapter 
info ={
    "keys": " values", ### left wali ko key bol ti hai ,right wale ko value bol ti hai 
    "name" : "Mohit singh", ### format yaad rakh na ye ,"", = srting ke liya hai ,
    ###int ko direct bhi likh sak te hai as you  can see the example below 
    "age": "23", ### dictionary mutable hoti hai inko hum change kar de te hai 
    "is_adult": True,
    11 : 23.24, ### key asi bhi hoo sakti hai 

}
print(type(info))
print(info["name"]) ### ya baat bhi yaad rakhiyo ki jab hum dictnary me se direct kisi ko call kar te hai tab 
###'[]' yee bracket use kar tee hai ,agar'()' ye use kiya to error show hoga vaha par 
### value kaise change kar sak te hai dictionary me ye dekhno  
info["name"] = "rohit singh" ### app ne ye to notice kiya hi hoga ki app ko value change
### kar ni hai tab ' [] ' en brackets ka use kiya hai ye baat yaad karkh naa 
print(info) ### apne dekha ki output me mohit singh ki jagah par rohit singh aa gya 
### this is how it works 
### let see a null dictionary in this code below
Null_dict ={} ## ye hai null dictionary   
Null_dict["name"] = "palak" ### dusri baat hum null dictionary me value direct add kar sakte hai like this ,
### yee automatic add hoojaye gaa append function ko use kar ne ki load koni aapne ko  
print(Null_dict)
### ab hum nested dictionary ke baaree me padhe gee  
# dictionary ke andar dicitonary 
marksinfo ={"name": "Mohit singh",
            "subjects" :("maths", "physics","chemstriy" ),
            "marks" :{### ye aap yaha se dekh sak te ho guys 
                "physics": 42,
                "chemstry":32,
                "Maths":88,} # ye yaha khatam hoti hai as u can see this 
            }
print(marksinfo)
print(marksinfo["marks"]) ## to ye marks wali dictionary print hoo jaaye gi 
print(marksinfo["marks"]["Maths"]) ## to app dekho ki ye dictionary ki andar ki keys ko print
## kare gaa this the method for calling function in nested dict ke andar wali dict ki value print karne ka method hai  
### all dictinary methods 
# 1 dict keys
# 2 dict value
# 3 dict items
# 4 dict get wala function hogya 
# 5 dict update wala function or es pe thodi practice  
## ke hum yaha kare gee
print(marksinfo.keys()) ## ek baat agar hum (marksinfo.keys)=  agar hum ye right kar te hai to hum me a ek numberical value mil ti hai 
## but when we use this = (marksinfo.keys()) = tab hi ye hame value de ga
print(marksinfo.values()) ## same factor as we have in our keys
print(marksinfo.get("name")) ## for calling a value from dict we already have a formula then why we use this ....?
### answer is jab dict me koi "key " naa hoo aur hum ne use call koi to vo error show kar
#  taa hai but when wew use this get function then it show none 
print(marksinfo.items()) ## ye duno ko ek sath laa ta hai key and value ko 
## bas ento hi yaad kar le darling
marksinfo.update({"age":12})
print(marksinfo)



 ### es ke sare function hogye hai ab hum "sets' ke bare me study kare gyee 
 ### sets = unorderd collection 
 ##3 sets = unqiue ,and immutable hai 
 ### esi me hum kabhi bhi dict ,ya list ko nahi karkh sak te hai kyu ki vo mutable hoti hai ess liye that the reason 
set = {1,2,3,4,56,}
print(type(set)) ## jasa ki app dekh sakte hai ki ye output me set show kare gaa
set1= {1,2,2,2,3,4,"hello world ","hello world" } ## just like the same in maths set me 
###jo duplicate value hai set un ko ignore kar dee gaa
print(set1) ## output mee app ne dekha ki last wala phele aagya phele wala badme  me aagya esliye es ko unorder bol te hai 
## jasa ki app dekh sakte hai ki ye output me set show kare gaa
### {'hello world ', 1, 2, 3, 4, 'hello world'} ye output hai set1 ka you notice one thing hello world print 2 times
#  becuase humne ek space add kar diya tab hum code likh raha thi esliye ye 2 time print hogya that the reason 
### sets ke kuch function hote hai as 
set.remove(2) ## ye to remove function hota hai 
print(set) ## output 2 remove hogya ,ye yaad rakh na ki hum ne kon sa bracket use kiya tha = () 
set.pop()
print(set) ## pop function me ye kisi ko bhi remove kar sakta hai randomly value ko udaaa de hai ye 
set.add(75) ## this is add functio for sets 
print(set)
set.clear()
# 1. remove
# 2. pop 
# 3.add 
# 4.clear is me sb clear ho jaa hai 
# 5.
# sets me hum union or intersection nhi kar sakte hai same like we do in maths
set1 = {1,2,3,4,5,}
set2 = {4,3,2,5,6,7,8,9,}
print(set1.union(set2)) ## output is {1,2,3,4,5,6,7,8,9} jasa ki maths me hota hai 
print(set1.intersection(set2)) ## it show only common world in both 
set3 ={}## for empty set if we do this then its comes a dict so we have to use something else i do that below 
print(type(set3))    ###   <class 'dict'> 
### now it show set when we print type, this is not working right now i will check and rewrite this again = for empty set
 
