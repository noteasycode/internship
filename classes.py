import math
from functools import reduce


class First:
    def __init__(self, number):
        self.number = number

    def is_divisible_by(self, divisor):
        if (int(self.number) % divisor) == 0:
            print(f"The number {self.number} is divisible by number {divisor} without remainder.")
        else:
            print(f"The number {self.number} is not divisible by number {divisor} without remainder.")

    @staticmethod
    def stat_method(num1, num2):
        multiply = lambda a, b: a * b
        print(f"The result of multiply is {multiply(num1, num2)}")

    def __del__(self):
        print(f"The object {self.__class__}, was delete")


class Second(First):
    def __init__(self, number, color):
        super().__init__(number)
        self.obj = number
        self.__color = color

    def __checker(self):
        return type(self.obj) == str

    def str_checker(self):
        return "is a string" if self.__checker() else "is not a string"


class Third(First):

    @staticmethod
    def stat_method(num1, num2):
        print(f"The Greatest Common Divisor of {num1} and {num2} is {math.gcd(num1, num2)}")
        print(f"The lowest common multiple of {num1} and {num2} is {(num1 * num2) // math.gcd(num1, num2)}")



if __name__ == "__main__":
    print("The result of operations in Third class:")
    first_var = First(10)
    first_var.is_divisible_by(3)
    First.stat_method(2, 3)
    print("The result of operations in Second class:")
    second_var = Second('20', 15)
    print(f"The protected variable is: {second_var._Second__color}")
    print(f"The variable {second_var.number} {second_var.str_checker()}")
    second_var.is_divisible_by(10)
    print("The result of operations in Third class:")
    third_var = Third(11)
    Third.stat_method(85, 45)

"""
# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: x, my_floats))
filter_result = list(filter(lambda name: name, my_names, my_names))
"""
