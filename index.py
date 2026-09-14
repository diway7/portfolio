class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, {self.name}.")
    
    def get_older(self):
        self.age += 1
        print(f"{self.name} в следующее день рождение будет {self.age} лет.")

person1 = Person("Айко", 14)
person2 = Person("Саша", 16)

person1.introduce()
person2.introduce()

person1.get_older()
person2.get_older()