#craete class pets from class animal and dog from pets and bark method in dog
#multilevel inheritance

class animal:
    animaltype="Mammal"
class pets(animal):
    color="white"
class dog(pets):
    def bark(self):
        print("bow bow!")

d=dog()
d.bark()
