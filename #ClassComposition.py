class Author:
    def __init__(self, name, email, gender):
        self.__name = name
        self.__email = email
        self.__gender = gender
        if gender != "m" and gender != "f":
            raise TypeError(" should be m or f")

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getGender(self):
        return self.__gender

    def toString(self):
        return f"Author[name={self.__name},email={self.__email},gender={self.__gender}]"


class Book:
    def __init__(self, name, author, price, qty=0):
        self.__name = name
        self.__author = author
        self.__price = price
        self.__qty = qty

    def getName(self):
        return self.__name

    def getAuthor(self):
        return self.__author

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

    def getQty(self):
        return self.__qty

    def setQty(self, qty):
        self.__qty = qty

    def toString(self):
        return f"Book[name={self.__name},{self.__author.toString()},price={self.__price},qty={self.__qty}]"

    def getAuthorName(self):
        return self.__author.getName()

    def getAuthorEmail(self):
        return self.__author.getEmail()

    def getAuthorGender(self):
        return self.__author.getGender()

poetry = Author("Lang Leav", "langleav@langleav.com", "f")
poetry2 = Book("The Dark Between the Stars", poetry ,"50", 2)

print(poetry.toString())
print(poetry2.toString())


