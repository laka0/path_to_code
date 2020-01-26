"""import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator"""

import functools
import time
import logging

logging.basicConfig(filename="machine.log", level=logging.INFO)

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        logging.info(f"Running: {func.__name__!r}          [  exec-time = {run_time:.4f} secs  ]")
        return value
    return wrapper_timer

import time
from random import randint
class CoffeeMachine():
    water_level = 100

    @timer
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False
        
    @timer
    def boil_water(self):
        return "boiling..."

    @timer
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
        print(self.boil_water())
        print("Coffee is ready!")

    @timer
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)

machine = CoffeeMachine()
for i in range(0, 5):
    machine.make_coffee()

machine.make_coffee()
machine.add_water(70)