#Exercise 1,2,3

class Elevator:
    def __init__(self, bottom_floors, top_floors):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.currentfloor = bottom_floors
    def go_to_floor(self, floor):
        if floor < self.bottom_floors or floor > self.top_floors:
            print('invalid entry')
            return
        while self.currentfloor < floor:
            self.floor_up()
        while self.currentfloor > floor:
            self.floor_down()
    def floor_up(self):
        self.currentfloor += 1
        print(f'Elevator is on {self.currentfloor} floor')
    def floor_down(self):
        self.currentfloor -= 1
        print(f'Elevator is on {self.currentfloor} floor')

h = Elevator(1, 15)
h.go_to_floor(5)
h.go_to_floor(15)
h.go_to_floor(4)

class Building:
    def __init__(self, bottom_floors, top_floors, elevators):
        self.bottom_floors = bottom_floors
        self.top_floors = top_floors
        self.elevators = [Elevator(bottom_floors, top_floors) for _ in range(elevators)]
    def run_elevator(self, elnum, finalfloor):
        if 0 <= elnum < len(self.elevators):
            print(f'elevator number {elnum} goes to floor {finalfloor}')
            self.elevators[elnum].go_to_floor(finalfloor)
        else:
            print('no elevator with this number')
    def fire_alarm(self):
        self.finalfloor = self.bottom_floors
        print(f'elevators moved to floor {self.finalfloor} due to fire alarm')
building1=Building(5, 15, 4)
building1.run_elevator(2, 7)
building2=Building(3, 12, 2)
building2.run_elevator(1, 7)
building1.fire_alarm()
building2.fire_alarm()
