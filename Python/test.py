class Circle():
    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    
    def multiply_radius(self,number):
        self.radius = self.radius*number
        print(f"Radius has been changed to {self.radius}")
    
mycircle = Circle(radius=4)
mycircle.multiply_radius(20)
print(mycircle.radius)


class Person():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def hello(self):
        print("hello!")
    
    def report(self):
        print(f"I am {self.first_name} {self.last_name}")
    
        
a = Person("John","Smith")
a.hello()
a.report()

class Agent(Person):
    def __init__(self, first_name, last_name,code_name):
        Person.__init__(self, first_name, last_name)
        self.code_name = code_name
        
    def reveal(self, passcode):
        
        if passcode==123:
            print("I am a secret agent!")
        else:
            self.report()
            
x = Agent("John","smith","mr.X")
x.hello()
x.code_name
x.report()
x.reveal()

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} written by {self.author}"
    
    def __len__(self):
        return self.pages
mybook = Book("Python Rocks!","Jose",120)
print(mybook)
print(len(mybook))
 