class Vehicle:
    def __init__(self, max_speed, color):
        self.max_speed = max_speed
        self.color = color
        print(f'The vehicle speed is {max_speed}mph and the color is {color}')
    def change_maxspeed(self):
        self.max_speed += 50
        print(f'The vehicle new max speed is {self.max_speed} and color is {self.color}')

p = Vehicle(100, 'red')
p.change_maxspeed()

