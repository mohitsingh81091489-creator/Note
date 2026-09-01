### let's play with lists,dictionary,tuples,that it 
cart=["apple","Milk","apple","bread","Sugar","Chocolate"]
print(cart)
### today i am learning tuples and list and try all concept on that
### i am started with list 
### list ke feautres 1.mutable hote hai ex
cart = [1,2,3,4,5]### list hamesa square brackets me noation hote hai 
print(type(cart)) ### it show its a list in type function 
### second baat hai 
newcart= []## type function me list show kare gaa
newcart1 =(1) ### jab hum esi ka type dekho ge to ye int show kare ga  sorry vo tuple ka feautres tha
print(type(newcart1)) ### it shows int only if you use tuple '()' only when we use this bracket
newcart2 = (1,)### kyu ki mane ',' lagaya hai es liye ye tuple ki tahra kaam kare gaa
print(type(newcart2))
### khas feature ye hai ki list me hum value change kar sak te hai but hum tuple me asa nahi hota at some specific place like i will show you donw
cart =[1,2,3,4,5,6,7] ### ab ye dekh naa m kya kar taa hoon 
cart[0] = 2 ### ye value replace ho jaaye gaa but tuple me nahi hoga ,,,ek aur khaAS baat ki agar h me replace kar ni hai value to ' [] ' bracket use kar naa hoga as you can see
### you use "() ' bracket then it show error
print(cart)
### can all do slicing in list ,,ex i will show you donw
print(cart[0:3]) ## dusri baat ye slicing ke time pee bhi hum ye " [] " = square bracket use kar te hai 
tuple = (1,2,3,4,5,5,6,)
tuple[0] = 5 ### error show kar raha hai ese pata chal taa hai ki tuple me value change nahi hoo ti hai 
print(tuple) 
print("mohit singh") ## esi si aap ek baat aur sikh sakte ho ki python me uppper si niche kaam kar ti hai,###
###agar upper ke sare function right tarike se likhe hai to upper wale sare function kaam kare gee par jaha par mistake hai
# ## use ke baad ke function kaam nahi kare ge par uss ke upar ke function kaam kare gee
