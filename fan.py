class Fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_on = False

    def __repr__(self):
        return repr((self.make, self.radius, self.color, self.speed, self.is_on))

    def switch_on(self):
        self.is_on = True
        self.speed = 3

    def switch_off(self):
        self.is_on = False
        self.speed = 0

    def increase_speed(self, speed):
        self.speed += speed

    def decrease_speed(self, speed):
        if(self.speed - speed >= 0):
            self.speed -= speed
        else:
            self.speed = 0


fan = Fan('Manufacturer 1', 5, 'Green')
fan.switch_on()
print(fan)
fan.increase_speed(2)
print(fan)
fan.decrease_speed(4)
print(fan)
fan.switch_off()
print(fan)