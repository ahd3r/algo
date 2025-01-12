"""
Implement a multiset that implements the following methods:

add(element)
remove(element)
count(element)
"""

class MultiSet(object):
    def __init__(self):
        self.multiset = {}

    def add(self, element):
        if element not in self.multiset:
            self.multiset[element] = 1
        else:
            self.multiset[element] += 1

    def remove(self, element):
        if element not in self.multiset:
            raise Exception("Element does not presented in multiset")
        else:
            if self.multiset[element] > 1:
                self.multiset[element] -= 1
            else:
                del self.multiset[element]

    def count(self, element):
        if element in self.multiset:
            return self.multiset[element]
        else:
            return 0

# m = MultiSet()
# print(m.count(1)) # 0
# m.add(1)
# m.add(1)
# print(m.count(1)) # 2
# m.remove(1)
# print(m.count(1)) # 1

"""
Given city names and their corresponding populations, write a program to output a city name subject to the following constraint: the probability of the program to output a city's name is based on its population divided by the sum of all cities' population. Assume the program will be repeatedly called many times.

For example: O(c) c = # cities for space

NY: 7M
SF: 5M
LA: 8M
The probability to generate “NY” is 7/20, “SF” is 5/20 and “LA” 8/20.

generateCity() -> one of "NY", "SF", "LA"
"""
import random

class City(object):
    def __init__(self, cities): # O(C)
        self.citySum = sum(cities.values())
        self.cities = {}
        s = 0
        for c in cities.keys():
            s += cities[c]
            self.cities[c] = s

    def generateCity(self): # O(C)
        r = random.randint(0, self.citySum)
        for city in self.cities.keys():
            if r < self.cities[city]:
                return city

c = City({"NY": 7000000, "SF": 1000000, "LA": 8000000})
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
print(c.generateCity())
