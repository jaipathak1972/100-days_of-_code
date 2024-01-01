def add(*args):

    sum = 0
    for arg in args:
        sum += arg
    return sum

def calculator(**kwargs):

    print(kwargs)

    for key, value in kwargs.items():
        print(key)

calculator(add = 3 , multi = 5)

class Car:
    def __init__(self,**kw) -> None:
        self.make = kw["name"]
        self.model = kw["model"]
        self.color = kw.get("apple")
my_car = Car(make= "apple" , model = "use")
print(my_car.model)

