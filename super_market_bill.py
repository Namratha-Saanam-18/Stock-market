from datetime import datetime

print(50*"_",'\n',20*" ","WELCOME",'\n',50*"_")

menu='''
                *Menu*

    item        quantity        price
    potato      20 kgs          Rs 30 per kg
    tomato      50 kgs          Rs 30 per kg
    maggie      5 kgs           Rs 100 per kg
    beans       10 kgs          Rs 200 per kg

'''

items={"potato":[20,30],
       "tomato":[50,30],
       "maggie":[5,100],
       "beans":[10,200]}

print(menu)
option=int(input("Do you want to buy then, press 1:"))
item_list=[]
price_list=[]
qty_list=[]
total_price=0
count=0

if option==1:
    name=input("enter your name: ")
    while True:
        item=input("which item do you need: ")
        if item in items.keys():
            kg=int(input("enter the no of kgs u need : "))
            if kg<=items[item][0]:
                price=items[item][1]*kg
                print("the total cost of ",item," is ",price)
                item_list.append(item)
                price_list.append(price)
                total_price+=price
                qty_list.append(kg)   
                count+=1         
            else:
                print("Sorry! we don't have sufficient quantity")
        else:
            print("sorry! we dont have that item: ")
        op=int(input("Do you want to buy more items then, press 1:"))
        if op==1:
            print("Ok")
        else:
            print("Ok! ")
            break
    #Bill
    bill=int(input("Can i make the bill, press 1: "))
    if bill==1:
        print(40*"*","Nammu's super market",40*"*")
        print(45*"-","Vikarabad",46*"-")
        print("Name: ",name,55*" ","Date: ",datetime.now())
        print(102*"_")
        print(10*" ","S.No",10*" ","Item",10*" ","quantity",10*" ","Price")
        for i in range(count):
            print(12*" ",i,10*" ",item_list[i],13*" ",qty_list[i],14*" ",price_list[i])
        print(102*"_")
        Gst_amt=(total_price*5)%100
        print("Total amount",total_price," "*60,"Gst_amount: ",Gst_amt)
        print(102*"_")
        print(70*" ","Total amount: ",total_price+Gst_amt)
        print(102*"_")

else:
    print("Ok! Thank You :)")
            

