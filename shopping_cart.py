class shopping_cart:
    def shopping(self):
        shopping = True
        cart = []
        stop = ''
        while shopping == True:
        
            add_or_rid = input("Would you like to add or rid an item?")
            if add_or_rid == "add" :
                add = input("What would you like to add?")
                cart.append(add)
            elif add_or_rid == 'rid':
                remove = input("What did you want to get rid of?")
                cart.remove(remove)
            stop = input("would you like to checkout? Y or N? ")
            if stop.upper() == "Y":
                shopping = False
           
            print(cart)
shoppingcart = shopping_cart()
shoppingcart.shopping()