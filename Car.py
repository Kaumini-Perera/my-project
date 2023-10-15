class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.meter = 0
        self.time = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed > 0:
            self.speed -= 5

    def step(self):
        self.time += 1
        self.meter += self.speed

    def average_speed(self):
        return self.meter/self.time