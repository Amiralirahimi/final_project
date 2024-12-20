class Store :
    def __init__(self):
        self.myusers = {"amirali":1235}
        self.address=list()
        self.product={"a":22,"b":24,"c":25}
        self.shopping={}
    def add_user(self,username,password,address):
        if username in self.myusers :
        
         print("you have already registered")
        else:
           self.myusers[username] = password 
           self.address.append(address)
        print("...user added ...")

    def login_user(self,username,password):

        if self.myusers[username]==password :
           print("login was successful")
        else :
           print("the username or password is incorrect")
    def add_product(self,username,password,product,price):
       
       if username and password == "admin":
          self.product[product] = price
          print("...product added...")
          
       else:
          print("...you do not have access ...")

    def del_product(self,username,password,product):
       
       if username and password == "admin":
          del self.product[product]

       else :
          print("...you do not have access ...") 

    def update_product(self,username,password,product,price):
       
       if username and password == " admin" : 
          self.product.update([product,price])

       else :
          print ("...you do not have access ...")

    def show_product(self,username):
        if username in self.myusers :
           sort_product=sorted(self.product.items(),key=lambda x:x[1],reverse=True )
           for i in sort_product :
              print(i[0],i[1])

    def search_product(self,product,price):
       for k , v in self.product.items():
          if k==product and v==price :
             print(f" product is :{product}, price is {price}")

    def add_shopping_cart(self,username,product,price):
       
       if username in self.myusers :
         final_product=None
         for k,v in self.product.items():

            if k==product and v==price :
              self.shopping[product] = price
              print(self.shopping.items())
              mas=str(input("do you want to finalize your purchase?"))
              
              if mas == "yes":
               final_product = product
               print("...Thank you for your purchase...")
              else:
                  return

         if final_product is not None :
            del self.product[final_product]
       else:
         print("...you must login in to the site...")
         
    def payment(self,username):
      if username in self.myusers:
         with open("shoppinghistoy.txt","a") as file : 
            file.write(f"user:{username},\n shopping list:{self.shopping.items()}")

      

          
   
user1=Store()     
user1.add_user("admin","admin","bandar abbas")
user1.login_user("admin","admin")
user1.add_product("admin","admin","a22",40)
user1.search_product("a",22)
user1.add_shopping_cart("admin","a",22)
user1.payment("admin")
