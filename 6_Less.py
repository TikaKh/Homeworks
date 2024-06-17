#  #first
# from abc import ABC, abstractmethod
#
# class Country(ABC):
#
#     @abstractmethod
#     def get_population(self):
#         pass
#
#     @abstractmethod
#     def get_capital(self):
#         pass
#
#     @abstractmethod
#     def get_official_language(self):
#         pass

# #second
# from abc import ABC, abstractmethod
# class Country(ABC):
#
#     @abstractmethod
#     def get_population(self):
#         pass
#
#     @abstractmethod
#     def get_capital(self):
#         pass
#
#     @abstractmethod
#     def get_official_language(self):
#         pass
#
# class Georgia(Country):
#     def __init__(self, population, capital, official_language, budget):
#         self.population = population
#         self._capital = capital
#         self.__official_language = official_language
#         self.__budget = budget
#
#     def get_population(self):
#         return self.population
#
#     def get_capital(self):
#         return self._capital
#
#     def get_official_language(self):
#         return self.__official_language
#
#     def get_budget(self):
#         return self.__budget

# #third
# from abc import ABC, abstractmethod
# class Country(ABC):
#
#     @abstractmethod
#     def get_population(self):
#         pass
#
#     @abstractmethod
#     def get_capital(self):
#         pass
#
#     @abstractmethod
#     def get_official_language(self):
#         pass
# class Georgia(Country):
#     def __init__(self, population, capital, official_language, budget):
#         self.population = population
#         self._capital = capital
#         self.__official_language = official_language
#         self.__budget = budget
#
#     def get_population(self):
#         return self.population
#
#     def get_capital(self):
#         return self._capital
#
#     def get_official_language(self):
#         return self.__official_language
#
#     def get_budget(self):
#         return self.__budget
#
#
# georgia = Georgia(3729600, "Tbilisi", "Georgian", 15000000000)
#
# print("Population:", georgia.get_population())
# print("Capital:", georgia.get_capital())
# print("Official Language:", georgia.get_official_language())
# print("Budget:", georgia.get_budget())
#
