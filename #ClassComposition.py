class Author:
    
    def __init__(self, name, email, gender):
        self.name = name 
        self.email = email
        self.gender = gender 

        if gender != "m" and gender != "f":
            raise TypeError("Only M or F")

    def getName(self):
        return self.name 

    def getEmail(self):
        return self.email

    def setEmail(self):
        self.email = email 
    
    def getGender(self):
        return self.gender 

    def toString(self):
        return f"Author[name={self.name},email={self.email},gender={self.gender}]"

# author1 = Author("Ardelia", "ardeliashaula@gmail.com", "M")
#author1.toString()

class Book:

    def __init__(self, name, author, price , qty = 0):
        self.name = name 
        self.author = author
        self.price = price
        self.qty = qty 

    def getName(self):
        return self.name 

    def getAuthor(self):
        return self.authors

    def getPrice(self):
        return self.price

    def setPrice(self):
        self.price = price
    
    def getQty(self):
        return self.qty 
    
    def setQty(self):
        self.qty = qty
    
    def toString(self):
        return f"Book[name={self.__name},{self.__author.toString()},price={self.__price},qty={self.__qty}]"

    def getAuthorName(self):
        return self.author.getName()

    def getAuthorEmail(self):
        return self.author.getEmail()

    def getAuthorGender(self):
        return self.author.getGender()
    


    
    
    