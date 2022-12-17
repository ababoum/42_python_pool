"""Decorators in Python"""

import sys
import time
from random import randint
import os


def print_into_file(msg:str, filepath: str):
    with open(f'{filepath}', "a") as f:
        print(msg, file=f)


def log(func):
    def wrapper(*args, **kwargs):
        timestmp_start = time.time()
        ret = func(*args, **kwargs)
        elapsed_time = time.time() - timestmp_start
        print_into_file(
            f'({os.getenv("USER")})Running: \
{func.__doc__:19}\
[ exec-time = {(elapsed_time, elapsed_time * 1000)[elapsed_time < 1]:.3f} \
{("s", "ms")[elapsed_time < 1]} ]', 'machine.log')
        return ret
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        """Start Machine"""
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        """Boil Water"""
        return "boiling..."

    @log
    def make_coffee(self):
        """Make Coffee"""
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        """Add Water"""
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
