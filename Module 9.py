import random
class Car:
    def __init__(self, regnumber, maxspeed, currentspeed = 0, travelleddistance=0):
        self.regnumber = regnumber
        self.maxspeed = maxspeed
        self.currentspeed = currentspeed
        self.travelleddistance = travelleddistance
    def accelerate(self, speedchange):
        newspeed = self.currentspeed + speedchange
        if newspeed < 0:
            self.newspeed = 0
        elif newspeed > self.maxspeed:
            self.newspeed = self.maxspeed
        else:
            self.currentspeed = newspeed
    def drive(self, hours):
        self.travelleddistance += self.currentspeed * hours

cars = []
for i in range(1,11):
    regnumber = f"ABC{i}"
    maxspeed = random.randint(100,200)
    car = Car(regnumber, maxspeed)
    cars.append(car)
raceDone = True
while raceDone != True:
    for car in cars:
     speedchange = random.randint(0,15)
     car.accelerate(speedchange)

    car.drive(1)

    if car.travelleddistance >= 10000:
        raceDone = True
        break


for car in cars:
    print(f'The car {car.regnumber}:\n {car.maxspeed}km/h\ncurrent speed: {car.currentspeed}km/h\ntravelled distance: {car.travelleddistance}km')