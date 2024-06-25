
from datetime import datetime

name = input("Enter your name : ")

#  Items list
lists ='''
---------------------------------
   Item          Price
---------------------------------
   Rice         Rs 20/kg
   Sugar        Rs 30/kg
   Salt         Rs 20/kg
   Oil          Rs 80/litre
   Panner       Rs 110/kg
   Maggie       Rs 50/kg
   Boost        Rs 90/each
   Colgate      Rs 85/each
---------------------------------
'''


price = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []


items = {'Rice':20,'Sugar':30,'Salt':20,'Oil':80,'Panner':110,'Maggie':50,'Boost':90,'Colgate':85}


option = int(input("For list of items , Enter 1 : "))

if (option == 1):
    print(lists)
    
for i in range(len(items)):
    inp1 = int(input("If you want to buy press 1 (or) For exit press 2  : "))
    
    if(inp1==2):
        break
    
    if(inp1==1):
        item = input("Enter yout items : ")
        quantity = int(input("Enter quantity : "))
        
        if item in items.keys():
            price = quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=((totalprice*18)/100)
            finalamount=gst+totalprice
        else :
            print(" Sorry, You enetered item is not avaiable ")
            
    else :
        print("You entered wrong number")
            
            
    inp = input("Can I bill the items (yes/no) : ") 
    
    if ((inp.lower())=="yes"):
        if(finalamount!=0):         
            print("\n\n\n",40*"=","KTDM Super Market",40*"=")
            print(28*" ","Kothagudem")
            print("Name : ",name,30*" ","Date : ",datetime.now())
            print(75*"-")
            print("S.NO.",8*" ","Items",8*" ","Quantity",3*" ","price")
            for i in range(len(pricelist)):
                print(i+1,")",ilist[i],"-----",qlist[i],"-----",plist[i])
            print(100*"-")
            print(50*" ","TotalAmount : ","Rs",totalprice)
            print("gst amount",60*" ","Rs",gst)
            print(100*"-")
            print(50*" ","finalamount : ","Rs",finalamount)
            print(100*"-")
            print(50*" ","Thanks for visiting...")
            print(100*"-")
                 
