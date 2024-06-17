# #task1
# class Transport:
#     name = "Car"
#     capacity = 5
#     max_speed = 200
#     fuel_type = "Gasoline"
#
# print(Transport.name)
# print(Transport.capacity)
# print(Transport.max_speed)
# print(Transport.fuel_type)

# #task2
# class Transport:
#     name = "Car"
#     capacity = 5
#     max_speed = 200
#     fuel_type = "Gasoline"
#     @staticmethod
#     def is_eco_friendly():
#         eco_friendly_fuel_types = ["Electric", "Hybrid"]
#         return Transport.fuel_type in eco_friendly_fuel_types
# print(Transport.name)
# print(Transport.capacity)
# print(Transport.max_speed)
# print(Transport.fuel_type)
#
# print(Transport.is_eco_friendly())
#
# #task3
# class Transport:
#     name = "Car"
#     capacity = 5
#     max_speed = 200
#     fuel_type = "Gasoline"
#     @staticmethod
#     def is_eco_friendly():
#         eco_friendly_fuel_types = ["Electric", "Hybrid"]
#         return Transport.fuel_type in eco_friendly_fuel_types
#     @classmethod
#     def recommended_transport(cls, passenger_count):
#         if passenger_count <= 4:
#             return cls("Car", 4, 200, "Gasoline")
#         elif passenger_count <= 30:
#             return cls("Bus", 30, 100, "Diesel")
#         else:
#             return cls("Train", 200, 300, "Electric")
#     @classmethod
#     def compare_speed(cls, other_max_speed):
#         if cls.max_speed > other_max_speed:
#             return f"{cls.name} is faster"
#         elif cls.max_speed < other_max_speed:
#             return f"{cls.name} is slower"
#         else:
#             return f"{cls.name} has the same speed as the other transport"
#
# print(Transport.name)
# print(Transport.capacity)
# print(Transport.max_speed)
# print(Transport.fuel_type)
#
# print(Transport.is_eco_friendly())
#
# print(Transport.recommended_transport(20).name)
# print(Transport.compare_speed(180))

# #task4
# class Transport:
#     def __init__(self, name, capacity, max_speed, fuel_type):
#         self.name = name
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.fuel_type = fuel_type
#
#     name = "Car"
#     capacity = 5
#     max_speed = 200
#     fuel_type = "Gasoline"
#
#     @staticmethod
#     def is_eco_friendly():
#         eco_friendly_fuel_types = ["Electric", "Hybrid"]
#         return Transport.fuel_type in eco_friendly_fuel_types
#
#     @classmethod
#     def recommended_transport(cls, passenger_count):
#         if passenger_count <= 4:
#             return cls("Car", 4, 200, "Gasoline")
#         elif passenger_count <= 30:
#             return cls("Bus", 30, 100, "Diesel")
#         else:
#             return cls("Train", 200, 300, "Electric")
#     @classmethod
#     def compare_speed(cls, other_max_speed):
#         if cls.max_speed > other_max_speed:
#             return f"{cls.name} is faster"
#         elif cls.max_speed < other_max_speed:
#             return f"{cls.name} is slower"
#         else:
#             return f"{cls.name} has the same speed as the other transport"
#
# car = Transport("Car", 5, 200, "Gasoline")
# bus = Transport("Bus", 30, 100, "Diesel")
# train = Transport("Train", 200, 300, "Electric")
#
# print(car.name)
# print(bus.capacity)
# print(train.max_speed)
#
# print(Transport.is_eco_friendly())  # Output: False
#
# print(Transport.recommended_transport(20).name)  # Output: Bus
# print(Transport.compare_speed(180))  # Output: Car is faster
#
# #task5
# class Transport:
#     def __init__(self, name, capacity, max_speed, fuel_type):
#         self.name = name
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.fuel_type = fuel_type
#
#     @staticmethod
#     def is_eco_friendly(fuel_type):
#         eco_friendly_fuel_types = ["Electric", "Hybrid"]
#         return fuel_type in eco_friendly_fuel_types
#
#     @classmethod
#     def recommended_transport(cls, passenger_count):
#         if passenger_count <= 4:
#             return cls("Car", 4, 200, "Gasoline")
#         elif passenger_count <= 30:
#             return cls("Bus", 30, 100, "Diesel")
#         else:
#             return cls("Train", 200, 300, "Electric")
#
#     @classmethod
#     def compare_speed(cls, other_max_speed):
#         if cls.max_speed > other_max_speed:
#             return f"{cls.name} is faster"
#         elif cls.max_speed < other_max_speed:
#             return f"{cls.name} is slower"
#         else:
#             return f"{cls.name} has the same speed as the other transport"
#
#     def get_name(self):
#         return self.name
#
#     def get_capacity(self):
#         return self.capacity
#
# car = Transport("Car", 5, 200, "Gasoline")
# bus = Transport("Bus", 30, 100, "Diesel")
# train = Transport("Train", 200, 300, "Electric")
#
# print(car.get_name())
# print(bus.get_capacity())
#
# print(Transport.is_eco_friendly("Gasoline"))
#
# print(Transport.recommended_transport(20).name)
# print(Transport.compare_speed(180))

# #task6
# class Transport:
#     def __init__(self, name, capacity, max_speed, fuel_type):
#         self.name = name
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.fuel_type = fuel_type
#
#     @staticmethod
#     def is_eco_friendly(fuel_type):
#         eco_friendly_fuel_types = ["Electric", "Hybrid"]
#         return fuel_type in eco_friendly_fuel_types
#
#     @classmethod
#     def recommended_transport(cls, passenger_count):
#         if passenger_count <= 4:
#             return cls("Car", 4, 200, "Gasoline")
#         elif passenger_count <= 30:
#             return cls("Bus", 30, 100, "Diesel")
#         else:
#             return cls("Train", 200, 300, "Electric")
#
#     @classmethod
#     def compare_speed(cls, other_max_speed):
#         if cls.max_speed > other_max_speed:
#             return f"{cls.name} is faster"
#         elif cls.max_speed < other_max_speed:
#             return f"{cls.name} is slower"
#         else:
#             return f"{cls.name} has the same speed as the other transport"
#
#     def get_name(self):
#         return self.name
#
#     def get_capacity(self):
#         return self.capacity
#
#     def __repr__(self):
#         return f"Transport(name={self.name}, capacity={self.capacity}, max_speed={self.max_speed}, fuel_type={self.fuel_type})"
#
# car = Transport("Car", 5, 200, "Gasoline")
# bus = Transport("Bus", 30, 100, "Diesel")
# train = Transport("Train", 200, 300, "Electric")
#
# print(car.get_name())
# print(bus.get_capacity())
#
# # Calling static method
# print(Transport.is_eco_friendly("Gasoline"))
#
# print(Transport.recommended_transport(20).name)
# print(Transport.compare_speed(180))
#
# print(car)  # Output: Transport(name=Car, capacity=5, max_speed=200, fuel_type=Gasoline)
# print(bus)  # Output: Transport(name=Bus, capacity=30, max_speed=100, fuel_type=Diesel)

# #task7
# class Transport:
#     def __init__(self, name, capacity, max_speed, fuel_type):
#         self.name = name
#         self.capacity = capacity
#         self.max_speed = max_speed
#         self.fuel_type = fuel_type
#
#     @staticmethod
#     def is_eco_friendly(fuel_type):
#         eco_friendly_fuel_types = ["Electric", "Hybrid"]
#         return fuel_type in eco_friendly_fuel_types
#
#     @classmethod
#     def recommended_transport(cls, passenger_count):
#         if passenger_count <= 4:
#             return cls("Car", 4, 200, "Gasoline")
#         elif passenger_count <= 30:
#             return cls("Bus", 30, 100, "Diesel")
#         else:
#             return cls("Train", 200, 300, "Electric")
#
#     @classmethod
#     def compare_speed(cls, other_max_speed):
#         if cls.max_speed > other_max_speed:
#             return f"{cls.name} is faster"
#         elif cls.max_speed < other_max_speed:
#             return f"{cls.name} is slower"
#         else:
#             return f"{cls.name} has the same speed as the other transport"
#
#     def get_name(self):
#         return self.name
#
#     def get_capacity(self):
#         return self.capacity
#
#     def __repr__(self):
#         return f"Transport(name={self.name}, capacity={self.capacity}, max_speed={self.max_speed}, fuel_type={self.fuel_type})"
#
# car = Transport("Car", 5, 200, "Gasoline")
# bus = Transport("Bus", 30, 100, "Diesel")
# train = Transport("Train", 200, 300, "Electric")
# bike = Transport("Bike", 2, 25, "None")
# scooter = Transport("Scooter", 1, 50, "Electric")
#
# print(car.get_name())
# print(bus.get_capacity())
# print(train.max_speed)
# print(bike.fuel_type)
# print(scooter.get_name())
#
# print(Transport.is_eco_friendly("Gasoline"))
# print(Transport.is_eco_friendly("Electric"))
#
# print(Transport.recommended_transport(20).name)
# print(Transport.compare_speed(180))
#
# print(car)
# print(bus)
# print(train)
# print(bike)
# print(scooter)
