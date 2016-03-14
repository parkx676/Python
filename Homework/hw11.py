## Inheritance
## Juhwan Park (3917664)

## Vehicle class
class Vehicle():
    def __init__(self, make=None, model=None, year=None, mileage=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def ismake(self):
        return str(self.make)

    def ismodel(self):
        return str(self.model)
    
    def isyear(self):
        return str(self.year)

    def ismileage(self):
        return str(self.mileage)

    def isprice(self):
        return str(self.price)

    def setmake(self, make):
        self.make = make

    def setmodel(self, model):
        self.model = model

    def setyear(self, year):
        self.year = year

    def setmileage(self, mileage):
        self.mileage = mileage

    def setprice(self, price):
        self.price = price

    def Display(self):
        print("Make: " + str(self.ismake()) +
            "\nYear: " + str(self.isyear()) +
            "\nModel: " + str(self.ismodel()) +
            "\nMiles: " + str(self.ismileage()) +
            "\nPrice: " + str(self.isprice()))

## Each classes of car's type

class Car(Vehicle):
    def __init__(self, make, model, year, mileage, price, numdoor):
        super().__init__(make, model, year, mileage, price)
        self.numdoor = numdoor

    def setnumdoor(self, numdoor):
        self.numdoor = numdoor

    def isnumdoor(self):
        return self.numdoor

    def Display(self):
        super().Display()
        print("Number of doors: " + str(self.isnumdoor()))
        
class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, price, dtype):
        super().__init__(make, model, year, mileage, price)
        self.dtype = dtype

    def setdtype(self, dtype):
        self.dtype = dtype

    def isdtype(self):
        return self.dtype
    
    def Display(self):
        super().Display()
        print("Drive type: " + self.isdtype() + "-wheel drive")
    
class SUV(Vehicle):
    def __init__(self, make, model, year, mileage, price, capa):
        super().__init__(make, model, year, mileage, price)
        self.capa = capa

    def setcapa(self, capa):
        self.capa = capa

    def iscapa(self):
        return self.capa

    def Display(self):
        super().Display()
        print("Passenger capacity: " + str(self.iscapa()))

## Inventory class

class Inventory(list):
    def __init__(self, lst = []):
        self.lst = lst

    def addVehicle(self, car):
        self.lst += [car]

    def Display(self):
        for i in self.lst:
            print('\n')
            i.Display()

## main fuction with console

def main():
    inven = Inventory()
    done = False
    while not done:
        vetype = input("Enter a vehicle type: ").lower()
        while vetype != "car" and vetype != "truck" and vetype != "suv":
            print("Wrong Input!")
            vetype = input("Enter a vehicle type: ").lower()
        make = input("Enter a vehicle maker: ").capitalize()
        year = input("Enter a vehecle year: ")
        model = input("Enter a vehicle model: ").capitalize()
        mileage = input("Enter a vehicle mileage: ")
        price = input("Enter a vehicle price: ")
        
        if vetype == "car":
            numdoor = input("Enter a car's number of doors: ")
            while numdoor != '2' and numdoor != '4':
                print("Wrong Input! It should be 2 or 4.")
                numdoor = input("Enter a car's number of doors: ")
            automobile = Car(make, model, year, mileage, price, numdoor)
            inven.addVehicle(automobile)
        elif vetype == "truck":
            dtype = input("Enter a car's drive type: ")
            while dtype != '2' and dtype != '4':
                print("Wrong Input! It should be 2 or 4.")
                dtype = input("Enter a car's drive type: ")
            automobile = Truck(make, model, year, mileage, price, dtype)
            inven.addVehicle(automobile)
        elif vetype == "suv":
            capa = input("Enter a car's passenger capacity: ")
            automobile = SUV(make, model, year, mileage, price, capa)
            inven.addVehicle(automobile)
            
        ## User indication
        cont = input("Continue?(y/n): ").lower()
        if cont == 'n':
            done = True
            
    ## Calling the inventory Display method        
    inven.Display()

## Calling main function
main()
