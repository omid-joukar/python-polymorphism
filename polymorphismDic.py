
class AnimalType(object):
    def quack(self): return self._doaction('quack')
    def feathers(self): return self._doaction('feathers')
    def bark(self): return self._doaction('bark')
    def fur(self): return self._doaction('fur')
    def animalName(self):
        return self.__class__.__name__.lower()
    def _doaction(self,action):
        if action in self.strings:
            return self.strings[action]
        else:
            return '{} is not in {}'.format(action,self.animalName)
    
class Person(AnimalType):
    strings = dict(
        quack="Quackkkkkkkk!",
        feathers="The duck has gray feathers")
class Dog(AnimalType):
    strings = dict(quack="The person said woof",
                   feathers="the person has skin",
                   bark="the person imitate duck" , 
                   fur="Furrrrr!")
class Duck(AnimalType):
    strings = dict(bark="Arf!" ,
                  fur="The dog has white spots")
def do_in_forest(dog):
    print(dog.fur())
    print(dog.bark())
def do_in_house(duck):
    print(duck.quack())
    print(duck.feathers())
def main():
    john = Dog()
    ali = Person()
    mohsen = Duck()
    for n in(john ,ali,mohsen):
        do_in_forest(n)
    for n in(john ,ali,mohsen):
        do_in_house(n)
if __name__=="__main__":main()
       
