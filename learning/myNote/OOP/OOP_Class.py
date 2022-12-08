
# Contoh 1
class Dog:
    # class Attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))


print ("==============================================================================================================")


# Contoh 2
# Class Attribute
class Dog:
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate the Dog object
jake = Dog("Jake", 7)
doug = Dog("Doug", 4)
william = Dog("William", 5)

# Determine the oldest Dog
def get_biggest_number(*args):
    return max(args)

# Output
print("The oldest Dog is {} years old.".format(
    get_biggest_number(jake.age, doug.age, william.age)))


print ("==============================================================================================================")


# Contoh 3
class Dog:
    # class Attribute
    species = 'mammal'
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def description(self):
        return ("{} is {} years old".format(self.name, self.age))
    
    # instance method
    def speak(self, sound):
        return ("{} says {}".format(self.name, sound))

# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))


print ("==============================================================================================================")


# Contoh : 4
# parent class
class Dog:
    # class attribute
    species = "mamalia"
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return ("{} is {} years old". format(self.name, self.age))

    # Instance method
    def speak(self, sound):
        return ("{} says {}". format(self.name, sound))

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return ("{} run {}". format(self.name, speed))

# Child class (inherits from Dog class)
class BullDog(Dog):
    def run(self, speed):
        return ("{} run {}". format(self.name, speed))

# Instantiate the Dog object
mikey = Dog("Mikey", 6)
# call our instance methods
print (mikey.description())
print (mikey.speak("gruf gruf"))

# Child classes inherit attributes and behaviors from the parent class
jim = BullDog("Jim", 12)
print (jim.description())
# Child classes have specific attributes and behaviors as well
print (jim.run("slowly"))
# Is jim an instance of Dog()?
print(isinstance(jim, Dog))

# Is julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))

# Is johnny walker an instance of BullDog()
johnnywalker = RussellTerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, BullDog))

# Is julie and instance of jim?
print(isinstance(julie, jim))


print ("==============================================================================================================")


# Contoh 5
# Parent class
class Pets:
    Dogs = []
    def __init__(self, Dogs):
        self.Dogs = Dogs

# Parent class
class Dog:
    # class attribute
    species = 'mammal'
    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
    # Instance method
    def description(self):
        return self.name, self.age

    # Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)

    # Instance method
    def eat(self):
        self.is_hungry = False

# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# Child class (inherits from Dog class)
class BullDog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

# Create instances of Dogs
my_Dogs = [
    BullDog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]

# Instantiate the Pets class
my_pets = Pets(my_Dogs)

# Output
print("I have {} Dogs.".format(len(my_pets.Dogs)))

for Dog in my_pets.Dogs:
    Dog.eat()
    print("{} is {}.".format(Dog.name, Dog.age))
print("And they're all {}s, of course.".format(Dog.species))

are_my_Dogs_hungry = False

for Dog in my_pets.Dogs:
    if Dog.is_hungry:
        are_my_Dogs_hungry = True

if are_my_Dogs_hungry:
    print("My Dogs are hungry.")
else:
    print("My Dogs are not hungry.")

# modifed
class Orang:
    #Orangs = []
    Hurang = []
    def __init__(self, Hurang):
        #self.Orangs = Orangs
        self.Hurang = Hurang

class Bocil:
    gender = 'Pria'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return ("Your {} and Your age {}". format(self.name, self.age))

    def speak(self, sound):
        return ("{} says {}". format(self.name, self.age))

    #def eat(self):
        #self.is_hungry = False

class Sultan(Bocil):
    def harta(self, harta):
        return ("{} have {}". format(self.name, self.harta))
    
class Kere(Bocil):
    def harta(self, harta):
        return ("{} have {}". format(self.name, self.harta))
    
my_grup = [
    Sultan("Kisah", 18),
    Kere("Anton", 20),
    Bocil("windah", 25)
]

my_orang = Orang(my_grup)

print("Grup ini berisi {} orang". format(len(my_grup)))

a = Sultan("Kisah", 27)
print(a.description())


# Print umur mereka dan gender mereka
for b in my_orang.Hurang:
    print ("{} is {}". format(b.name, b.age))
print ("and they're all {}, of course.". format(b.gender))


# Pengecekan lapar atau tidak
for x in my_orang.Hurang:
    if x.is_hungry is True:
        are_orang_hungry = True
    else:
        are_orang_hungry = False

if are_orang_hungry:
    print ("Semua orang lapar")
else:
    print ("Semua orang tidak lapar")
    

print ("==============================================================================================================")


# Contoh 6
# Parent class
class Pets:
    Dogs = []
    def __init__(self, Dogs):
        self.Dogs = Dogs
    def walk(self):
        for Dog in self.Dogs:
            print(Dog.walk())
    def speak(self):
        for Dog in self.Dogs:
            print(Dog.speak("Hallo"))
# Parent class
class Dog:
    # class attribute
    species = 'mammal'
    is_hungry = True
# Initializer / instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Instance method
    def description(self):
        return self.name, self.age
# Instance method
    def speak(self, sound):
        return "%s says %s" % (self.name, sound)
# Instance method
    def eat(self):
        self.is_hungry = False
    def walk(self):
        return "%s is walking!" % (self.name)
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)
# Child class (inherits from Dog class)
class BullDog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)
# Create instances of Dogs
my_Dogs = [
    BullDog("Tom", 6), 
    RussellTerrier("Fletcher", 7), 
    Dog("Larry", 9)
]
# Instantiate the Pet class
my_pets = Pets(my_Dogs)
# Output
my_pets.walk()
my_pets.speak()