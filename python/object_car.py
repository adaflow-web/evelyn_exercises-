class Car:

    def __init__(self, color, type, model, number_of_seats):
        self.color = color.capitalize()
        self.type = type
        self.model = model
        self.number_of_seats = number_of_seats

    def drive(self, speed):
        print ("The " + self.model + " model can reach " + str(speed) + " kms/hours.")

    def people(self, car_owner):
        print (car_owner + " has a " + str(self.number_of_seats) + " seats car.")

    def sell(self):
        print (self.color + " cars are the best sellers." )     

    def travel(self):
        print ("I prefer " + self.type + " to travel long distances.")  

peugeot = Car("white", "automatic", "308", 5)

peugeot.drive(188)
peugeot.people("Frédéric")
peugeot.sell()
peugeot.travel()


            