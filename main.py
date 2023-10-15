from Car import Car

c = Car()
print("I'm a car!")
while True:
    action = input("What should I do? [A]ccelerate, [B]rake, show [O]demeter, or show average [S]peed?")
    if action not in "ABOS" or len(action) != 1:
        print("I don't know how to do that")
        continue
    if action == "A":
        c.accelerate()
    elif action == "B":
        c.brake()
    elif action == "O":
        print("The car has driven {} kilometers".format(c.meter))
    elif action == "S":
        print("The car's average speed was {} kph".format(c.average_speed()))
    c.step()
