# Theme Park Task

class Attraction:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity

    def get_details(self):
        return f"Attraction: {self._name}, Capacity: {self._capacity}"

    def start(self):
        print(f"The attraction {self._name} is starting.")


class ThrillRide(Attraction):
    def __init__(self, name, capacity, min_height):
        super().__init__(name, capacity)  
        self._min_height = min_height

    def start(self):
        print(f"Thrill Ride {self._name} is now starting. Hold on tight!")

    def is_eligible(self, height):
        if height >= self._min_height:
            return True
        else:
            print(f"You must be at least {self._min_height}cm tall to ride {self._name}.")
            return False


class FamilyRide(Attraction):
    def __init__(self, name, capacity, min_age):
        super().__init__(name, capacity)  
        self._min_age = min_age

    def start(self):
        print(f"Family Ride {self._name} is now starting. Enjoy the fun!")

    def is_eligible(self, age):
        if age >= self._min_age:
            return True
        else:
            print(f"You must be at least {self._min_age} years old to ride {self._name}.")
            return False


class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role

    def work(self):
        print(f"Staff {self._name} is performing their {self._role}.")


class Visitor:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def ride(self, attraction):
        if isinstance(attraction, ThrillRide) and attraction.is_eligible(self._height):
            print(f"{self._name} is riding the Thrill Ride {attraction._name}.")
        elif isinstance(attraction, FamilyRide) and attraction.is_eligible(self._age):
            print(f"{self._name} is riding the Family Ride {attraction._name}.")
        else:
            print(f"{self._name} is not eligible for {attraction._name}.")



coaster = ThrillRide("Dragon Coaster", 20, 140)
carousel = FamilyRide("Merry Go Round", 30, 4)
visitor = Visitor("Marli", 17, 155)

coaster.start() 
visitor.ride(coaster)  

carousel.start() 
visitor.ride(carousel)  
