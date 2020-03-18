from functools import reduce


class First:
    def __init__(self, number, divisor):
        self.number = number
        self.divisor = divisor

    def __del__(self):
        print(f"The number {self.number}, was delete")

    def is_divisible_by(self):
        if (self.number % self.divisor) == 0:
            print(f"The number {self.number} is divisible by number {self.divisor} without remainder.")
        else:
            print(f"The number {self.number} is not divisible by number {self.divisor} without remainder.")


div_number = First(10, 3)

print(div_number.is_divisible_by())
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