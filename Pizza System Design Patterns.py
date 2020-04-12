from datetime import datetime

#Singleton
class Cart():
    __instance = None

    def getInstance():
        if Cart.__instance == None:
            Cart()
        return Cart.__instance
    
    def __init__(self):
        if Cart.__instance != None:
            raise Exception("There can only be one cart!")
        else:
            Cart.__instance = self
        self.cart = []
 
    def get_total_price(self):
        total_price = 0
        for item in self.cart: 
            total_price += item.get_price()
        return total_price
    
    def get_cart(self):
        cart_items = []
        for item in self.cart: 
            cart_items.append(item.get_name())
        return cart_items
    
    def add_item(self, menu_item):
        self.cart.append(menu_item)

#Builder
class BuildPizza():
    def __init__(self):
        self.name = "Pizza"
        self.price = 6.99
    
        self.crust = None
        self.size = None
        self.sauce = None
        self.meats = []
        self.veggies = []
    
    def __str__(self):
        return "Pizza specifications: " + self.crust + ", " + self.size + ", " + str(self.meats) + ", " + str(self.veggies)
       
    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def choose_crust(self, crust_style):
        self.crust = crust_style
    
    def choose_size(self, new_size):
        self.size = new_size
        
    def add_meat(self, new_meat):
        self.meats.append(new_meat)
    
    def add_veggies(self, new_veggie):
        self.veggies.append(new_veggie)
        
    def create_pizza(self):
        return Pizza(self)
        
    
#Facade
class Checkout():
    def __init__(self, cart, user, card):
        self.cart = cart
        self.user = user
        self.card = card

    #Combine shipment verification into one method:
    def get_verif_info(self):
        return "Cart items: " + str(self.cart.get_cart()) + ", will be shipped to: " + self.user.get_address()
    
    #Combine payment validation into one method:
    def validate_card(self):
        valid_payment = False
        if(self.card.validate_num and self.card.validate_date and self.card.validate_sec_code):
            valid_payment = True
            return valid_payment
    
    def purchase(self):
        return "$" + str(self.cart.get_total_price()) + " has been charged to your card."

    
class CreditCard():
    def __init__(self, card_number, card_date, sec_code):
        self.card_number = card_number
        self.card_date = card_date
        self.sec_code = sec_code
        
    def get_card_number(self):
        return self.card_number
    
    def get_card_date(self):
        return self.card_date
    
    def get_sec_code(self):
        return self.sec_code
        
    def validate_num(self):
        valid_num = False
        if(self.card_number[0] == "4"):
            valid_num = True
            return valid_num

    
    def validate_date(self):
        user_date = datetime.strptime(self.card_date, "%d/%m/%Y")
        present = datetime.now()
        valid_date = False
        if(user_date.date() > present.date()):
            valid_date = True
            return valid_date
        
    def validate_sec_code(self):
        valid_code = False
        if(len(self.sec_code) == 3):
            valid_code = True
            return valid_code
 
class User():
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_address(self):
        return self.address

#Main
def main():
    
    pizza = BuildPizza()
    pizza.choose_crust("Hand-tossed")
    pizza.choose_size("Medium")
    pizza.add_meat("Pepperoni")
    pizza.add_veggies("Mushrooms")
    print(pizza)
    
    cart = Cart()
    cart.add_item(pizza)
    print(cart.get_cart())    
    print(cart.get_total_price())    
    
    user = User("Jonah", "jkavadlo1@live.maryville.edu", "28 Forest Crest Drive")    
    card = CreditCard("4012888888881881", "3/5/2020", "321")
    
    checkout = Checkout(cart, user, card)
    print(checkout.get_verif_info())
    print(checkout.validate_card())
    print(checkout.purchase())
    
    
main()
    