# # 1 Task
# def get_user_info():
#     while True:
#         name = input("Enter your name: ")
#         if name.isdigit():
#             print("Error: Name cannot be a number. Please enter a valid name.")
#             continue
#         surname = input("Enter your surname: ")
#         if surname.isdigit():
#             print("Error: Surname cannot be a number. Please enter a valid surname.")
#             continue
#         try:
#             age = int(input("Enter your age: "))
#         except ValueError:
#             print("Error: Age must be a number. Please enter a valid age.")
#             continue
#         return [name, surname, age]
#
# user1 = get_user_info()
# user2 = get_user_info()
# user3 = get_user_info()
# consumer_info = [user1, user2, user3]
# def get_user_by_index(index):
#     if 0 <= index < len(consumer_info):
#         user = consumer_info[index]
#         return f"Name: {user[0]}\nLastname: {user[1]}\nAge: {user[2]}"
#     else:
#         return "Invalid index."
#
# index = int(input("Enter user index (0, 1, or 2): "))
#
# print(get_user_by_index(index))

# # 2 Task
# actors_info = [
#     {"first_name": "Leonardo", "last_name": "DiCaprio", "age": 48, "famous_movie": "Inception"},
#     {"first_name": "Brad", "last_name": "Pitt", "age": 60, "famous_movie": "Fight Club"},
#     {"first_name": "Morgan", "last_name": "Freeman", "age": 86, "famous_movie": "The Shawshank Redemption"},
#     {"first_name": "Meryl", "last_name": "Streep", "age": 74, "famous_movie": "The Devil Wears Prada"},
#     {"first_name": "Tom", "last_name": "Hanks", "age": 67, "famous_movie": "Forrest Gump"}
# ]
# def find_actor(name):
#     for actor in actors_info:
#         if actor["first_name"].lower() == name.lower() or actor["last_name"].lower() == name.lower():
#             return (f"Name: {actor['first_name']} {actor['last_name']}\n"
#                     f"Age: {actor['age']}\n"
#                     f"Famous Movie: {actor['famous_movie']}")
#     return "Actor not found."
# name = input("Enter the actor's first or last name: ")
# print(find_actor(name))

# # 3 Task
# def unique_list(input_list):
#     return list(set(input_list))
# original_list = [1, 2, 2, 3, 4, 4, 5]
# unique_list_result = unique_list(original_list)
# print("Original List:", original_list)
# print("Unique List:", unique_list_result)
#

# #3 Task VersTwo
# def unique_list(input_list):
#     return list(set(input_list))
#
# def add_elements_to_list():
#     elements = []
#     count = 0
#     while count < 7:
#         element = input("Enter a number: ")
#         if element.isdigit():
#             elements.append(int(element))
#             count += 1
#         else:
#             print("Invalid input. Please enter a number.")
#     return elements
#
# original_list = add_elements_to_list()
# unique_list_result = unique_list(original_list)
# print("Original List:", original_list)
# print("Unique List:", unique_list_result)

# #4 task versOne
# def combine_sets(set1, set2):
#     combined_set = set1.union(set2)
#     return tuple(combined_set)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# result_tuple = combine_sets(set1, set2)
# print("Combined Tuple:", result_tuple)

# #4 task versTwo
# def combine_sets(set1, set2):
#     combined_set = set1.union(set2)
#     return tuple(combined_set)
# def get_set_from_user():
#     set_values = set()
#     count = 0
#     while count < 3:
#         value = input("Enter a number for the set: ")
#         if value.isdigit():
#             set_values.add(int(value))
#             count += 1
#         else:
#             print("Invalid input. Please enter a number.")
#     return set_values
#
# print("Enter values for set1:")
# set1 = get_set_from_user()
# print("Enter values for set2:")
# set2 = get_set_from_user()
# result_tuple = combine_sets(set1, set2)
# print("Combined Tuple:", result_tuple)

# #5 task
# def is_dict_empty(input_dict):
#     if not input_dict:
#         return True
#     else:
#         return False
# my_dict = {'4':3, '7':6}
# print("Is the dictionary empty?", is_dict_empty(my_dict))

# #6 task
# def count_characters(input_string):
#     char_count = {}
#     for char in input_string:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count
# input_string = 'TikaKhatiashvili'
# result_dict = count_characters(input_string)
# print("Dictionary:", result_dict)


# #7 task
# info_list = []
#
# count = 0
# while count < 5:
#     info = input("Enter information: ")
#     info_list.append(info)
#     count += 1
#
# print("Resulting list:", info_list)

# #8 task
# info_list = []
#
# count = 0
# while count < 5:
#     info = input("Enter information: ")
#     info_list.append(info)
#     count += 1
# print("Original List:", info_list)
#
# if info_list:
#     first_element = info_list[0]
#     last_element = info_list[-1]
#     info_list[0] = last_element
#     info_list[-1] = first_element
# print("List after changing first and last elements:", info_list)
# element_to_remove = input("Enter an element to remove: ")
# if element_to_remove in info_list:
#     info_list.remove(element_to_remove)
#     print("Element removed. Updated list:", info_list)
# else:
#     print("Element not found in the list.")

#9 task V1
# my_list = [1, 2, 3, 4, 5]
# length_method1 = len(my_list)
# print("Length of the list (method 1):", length_method1)

#9 task V2
# my_list = [1, 2, 3, 4, 5]
# count = 0
# for _ in my_list:
#     count += 1
# print("Length of the list (method 2):", count)

#10 task v1
# my_list = ["apple", "banana", "cherry", "date"]
# print("Method 1:")
# for index, value in enumerate(my_list):
#     print(f"Index {index}: {value}")

#10 task v2
# my_list = ["apple", "banana", "cherry", "date"]
# print("\nMethod 2:")
# for i in range(len(my_list)):
#     print(f"Index {i}: {my_list[i]}")
