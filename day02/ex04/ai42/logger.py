import time
from random import randint
import datetime


def log(f):
    def wrapper(*args, **kwargs):
        fd = open("machine.log", "a")
        now1 = datetime.datetime.now()
        response = f(*args, **kwargs)
        now = str(datetime.datetime.now() - now1)
        fd.write("Running: %.20s [exec_time = %sms]" % (f.__name__.ljust(20), now[-3:-1]))
        fd.write("\n")
        return f(*args, **kwargs)
    return wrapper

class CoffeeMachine():
    def __init__(self, water):
        self.water_level = water

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
                print(self.boil_water())
                print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine(100)
    for i in range(0, 5):
        machine.make_coffee()
        machine.make_coffee()
        machine.add_water(70)
