#Create a new class that we can use to make people
class MyPerson:
    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town
        
#MAIN BODY
#Now let's make some people!

person1 = MyPerson("Fred",3,"Wakefield")

#Let's interact with the person object that we just created.
print(person1.name)
print(person1.age)
print(person1.town)
