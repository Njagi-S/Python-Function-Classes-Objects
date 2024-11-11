# 1.Create a class Animal with attributes species and sound.Add a method make_sound that prints: "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.

class Animal:
    def __init__(self,species,sound):
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        return f"The {self.species} goes {self.sound}!"

Dog = Animal("Dog","Barks")
Cat = Animal("Cat","Meows")
Hen = Animal("Hen","Clucks")
print(Dog.make_sound())
print(Cat.make_sound())
print(Hen.make_sound())


# 2.Create a class Book with attributes like title, author, and year.
# Add a method that returns a description of the book.
# Create an object of Book and print out the description.

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def description(self):
        return f"The title of the book is {self.title}, the author is {self.author} and it was published in the year {self.year}."

book = Book("Harry Potter","J.K Rowling",2000)
print(book.description())

# 3.Define a class BankAccount with attributes owner and balance (set balance to 0 by default).Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
# Ensure that the withdraw method does not allow the balance to go negative.

class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} Has been deposited from your account. Your balance is :{self.balance}"
        else:
            return "Invalid amount! Deposit Cannot Be Less Than Zero."

    def withdraw(self,amount):
        if amount > self.balance:
             return f"Hello {self.owner}, Insufficient funds for withdrawing {amount}."              
        else:
            self.balance -= amount
            return f"Hello {self.owner}, {amount} has been withdrawn from your account." 
    def get_balance(self):
        return f"Your current balance is {self.balance}"

account = BankAccount("Njagi")

account.deposit(10000)
print(account.withdraw(8000))
print(account.get_balance())