class Animal:
    def __init__(self, name, species, age, sound, zoo_name):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        self.zoo_name = zoo_name

    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}")

    def info(self):
        print(f"{self.name} is a {self.species} that is {self.age} years old. It belongs to the {self.zoo_name} zoo.")

    def __str__(self):
        return f"{self.name} is a {self.species} that is {self.age} years old."

class Lion(Animal):
    def __init__(self, name, age, zoo_name):
        super().__init__(name, "lion", age, "roar", zoo_name)

class Bird(Animal):
    def __init__(self, name, age, zoo_name, wingspan):
        super().__init__(name, "bird", age, "chirp", zoo_name)

    def info(self):
        print(f"{self.name} is a {self.species} that is {self.age} years old. It belongs to the {self.zoo_name} zoo and has a wingspan of {self.wingspan} feet.")

    def make_sound(self):
        print(f"{self.name} the {self.species} chirps {self.sound}")


if __name__ == '__main__':
    lion1 = Lion("Simba", 5, "Safari Park")
    lion2 = Lion("Nala", 4, "Safari Park")
    bird1 = Bird("Tweety", 2, "City Zoo", 1.5)
    bird1.wingspan = 1.5
    bird2 = Bird("Polly", 3, "City Zoo", 2.0)
    bird2.wingspan = 2.0

    animals = [lion1, lion2, bird1, bird2]
    for animal in animals:
        animal.info()
        animal.make_sound()
