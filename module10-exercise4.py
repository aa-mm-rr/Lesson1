import random


class Car:
    def __init__(self, regnumber, maxspeed):
        self.regnumber = regnumber
        self.maxspeed = maxspeed
        self.curspeed = 0
        self.travelleddistance = 0

    def accelerate(self, speedchange):
        newspeed = self.curspeed + speedchange
        if newspeed < 0:
            self.curspeed = 0
        elif newspeed > self.maxspeed:
            self.curspeed = self.maxspeed
        else:
            self.curspeed = newspeed

    def drive(self, hours):
        self.travelleddistance += self.curspeed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hourpasses(self):
        for car in self.cars:
            speedchange = random.randint(-10, 15)
            car.accelerate(speedchange)
            car.drive(1)

    def status(self):
        print(
            f"{'Registration':<12} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<20} {'Travelled Distance (km)':<20}")
        print("=" * 67)
        for car in self.cars:
            print(
                f"{car.regnumber:<12} {car.maxspeed:<15} {car.curspeed:<20} {car.travelleddistance:<20.1f}")
        print("=" * 67)

    def racefinished(self):
        return any(car.travelleddistance >= self.distance for car in self.cars)


cars = []
for i in range(1, 11):
    regnumber = f"ABC-{i}"
    maxspeed = random.randint(100, 200)
    car = Car(regnumber, maxspeed)
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)

hourspassed = 0
while not race.racefinished():
    race.hourpasses()
    hourspassed += 1
    if hourspassed % 10 == 0:
        print(f"\nStatus after {hourspassed} hours:")
        race.status()


print(f"\nFinal status after {hourspassed} hours:")
race.status()
