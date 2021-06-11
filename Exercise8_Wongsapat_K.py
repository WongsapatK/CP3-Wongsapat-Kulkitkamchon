username = str(input("Please enter your username: "))
password = str(input("Please enter your password: "))
if username == "wong" and password == "kul":
    print("Welcome to myShop, please select the product")
    print("1. Water      7 THB")
    print("2. Ice Cream 20 THB")
    print("3. Apple     30 THB")
    productSelected = int(input("Please select the number of the product: "))
    if productSelected == 1:
        amountOfProduct = int(input("How many bottle of water do you want? >> "))
        print("You buy", amountOfProduct, "bottle(s) of water. Your total price", 7*amountOfProduct, "THB")
    elif productSelected == 2:
        amountOfProduct = int(input("How many cone of ice cream do you want? >> "))
        print("You buy", amountOfProduct, "cone(s) of ice cream. Your total price", 20*amountOfProduct, "THB")
    elif productSelected ==3:
        amountOfProduct = int(input("How many apple do you want? >> "))
        print("You buy", amountOfProduct, "apple(s). Your total price", 30*amountOfProduct, "THB")
else:
    print("Username or Password is incorrect!")