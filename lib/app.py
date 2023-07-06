class Dog: 
    def bark(self):
        print("Woof")

fido = Dog()
# provides you with a list of the object's methods and attributes.
fido.__dir__()
to_print = fido.bark()
print(to_print)