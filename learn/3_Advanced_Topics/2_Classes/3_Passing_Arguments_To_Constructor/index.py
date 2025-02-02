class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")


kisah = Person("Kisah", 20, "London")
kisah.user_info()  # Name: Kisah, Age: 20, Location: London

jordan = Person("Jordan", 26, "USA")
jordan.user_info()  # Name: Jordan, Age: 26, Location: USA

alex = Person("alex", 19, "China")
alex.user_info()  # Name: alex, Age: 19, Location: China
