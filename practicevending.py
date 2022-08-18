#VENDING MACHINE

vending = int(input("Press \n 1 Cold Drink \n 2 Snack \n 3 Candy \n")) 

if vending == 1:
    coldDrink = int(input("Press \n 1 Mr Pibb \n 2 Sprite \n 3 Dr Brown \n"))
    if coldDrink == 1:
        amount = int(input("Enter amount of Mr Pibb \n"))
        if amount > 0 and amount < 20:
            cost = amount * 5
            print("The cost is ", cost)
        else:
            print("Invalid Amount")
    if coldDrink == 2:
        amount = int(input("Enter amount of Sprite \n "))
        if amount > 0 and amount < 20:
            cost = amount * 4
            print("The cost is ", cost)
        else:
            print("Invalid Amount")
    if coldDrink == 3:
        amount = int(input("Enter amount of Dr Brown \n"))  
        if amount > 0 and amount < 20:
            cost = amount * 7
            print("THe cost is ", cost) 
        else:
            print ("Invalid Amount")         

if vending == 2:
    snack = int(input("Press \n 1 Doritos \n 2 Plantains \n 3 Cookies \n "))
    if snack == 1:
        amount = int(input("Enter amount of Doritos \n"))
        if amount > 0 and amount < 20:
            cost = amount * 2
            print("The cost is ", cost)
        else:
            print("Invalid Amount")
    if snack == 2:
        amount = int(input("Enter amount of Plantains \n"))
        if amount > 0 and amount < 20:
            cost = amount * 3
            print("The cost is ", cost) 
        else:
            print("Invalid Amount") 
    if snack == 3:
        amount = int(input("Enter amount of cookies \n"))
        if amount > 0 and amount < 20:
            cost = amount * 4
            print("The cost is ", cost) 
        else:
            print("Invalid Amount")

if vending == 3:
    candy = int(input("Press \n 1 Lifesaver Gummies \n 2 Sour Patch \n 3 Starbursts \n"))
    if candy == 1:
        amount = int(input("Enter amount of Lifesaver Gummies \n"))  
        if amount > 0 and amount < 20:
            cost = amount * 3.50
            print("The cost is ", cost) 
        else:
            print("Invalid Amount")
    if candy == 2:
        amount = int(input("Enter amount of Sour Patch \n")) 
        if amount > 0 and amount <20:
            cost = amount * 2.75
            print("The cost is ", cost)
        else:
            print("Invalid Amount")
    if candy == 3:
        amount = int(input("Enter amount of Starbursts \n"))
        if amount > 0 and amount < 20:
            cost = amount * 2.50
            print("The cost is ", cost)
        else:
            print("Invalid Amount")
                                                                   

