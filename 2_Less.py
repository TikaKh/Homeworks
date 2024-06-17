# # #first Quiz
# attempts = 0
# while attempts < 5:
#     question = print(f"Which is the water-supply system (aqueduct) built by the empire still functioning today?\nPossible answers:\n     1. Sumerians\n     2. Seljuks\n     3. Rome\n     4. Mongols\n")
#     answer =input ("Open Correct Number or Word : ")
#     if answer == "1" or answer == "Sumerians" or answer == "2" or answer == "Seljuks" or answer == "4" or answer == "Mongols" :
#         print(f"Your Answer is incorrect, Correct Answer is Rome")
#     elif answer == "3" or answer == "Rome":
#         print("Your Answer is correct")
#         break
#     else:
#         print("Unintelligible answer")
#     attempts += 1
#     if attempts >= 5:
#         print("You've exceeded the maximum number of attempts.")

# #Second
#
# print("We Have Tree Type Product : \n1.Laptops \n2.Personal Computers \n3.Mobile Phones")
# product = input("Open Product Type 1,2 or 3 : ")
# MaxPrice = int(input("Enter Max Price: "))
# if product == "1":
#     Laptops = ["Lenovo","Acer","Macbook"]
#     if 1500 <= MaxPrice <= 2000:
#         print("You can buy a laptop.")
#     else:
#         print("This price range is not suitable for buying a laptop.")
# if product == "2":
#     PComputers = ["HP","Dell","Philips"]
#     if 3500 <= MaxPrice <= 7000:
#         print("You can buy a PC.")
#     else:
#         print("This price range is not suitable for buying a PC.")
# if product == "3":
#     Mobile = ["Iphone","Samsung x9","Redme Note 10"]
#     if 1700 <= MaxPrice <= 6000:
#         print("You can buy a Mobile Phone.")
#     else:
#         print("This price range is not suitable for buying a Mobile Phone.")




# #Third
# print("What is the season of the year ? \n1.Spring \n2.Summer \n3.Autumn \n4.winter")
# answer = input("Open 1,2 3,or 4 : ")
# if answer == "1":
#     print("You can Visit \n1.Barcelona \n2.Morocco \n3.Tokyo")
#     sanswer = input("Open 1,2 or 3 : ")
#     if sanswer == "1":
#         print("You can See : \n1.Camp Nou Stadium of FC Barcelona\n 2.Casa Batlló, must see of Gaudì\n3.Sagrada Familia")
#     elif sanswer == "2":
#         print(
#             "You can See : \n1.Ben Youssef Madrasa\n 2.Cascades d'Ouzoud\n3.Crocoparc")
#     elif sanswer == "3":
#         print("You can See : \n1.Senso-ji\n 2.Shinjuku Gyoen National Garden\n3.Sumo at Ryogoku Kokugikan")
#     else:
#         print("Maybe you're not ready to travel")
# if answer == "2":
#     print("You can Visit \n1.Indonesia \n2.Greece \n3.Italy")
#     sanswer = input("Open 1,2 or 3 : ")
#     if sanswer == "1":
#         print("You can See : \n1.Tanah lot \n 2.Besakih Great Temple\n3.Ceking Rice Terrace")
#     elif sanswer == "2":
#         print(
#             "You can See : \n1.Heraklion Archaeological Museum\n 2.Ancient Agora of Athens\n3.Odeon of Herodes Atticus")
#     elif sanswer == "3":
#         print("You can See : \n1.Fontana di Trev\n 2.Duomo di Milano \n3.The Sansevero Chapel")
#     else:
#         print("Maybe you're not ready to travel")
# if answer == "3":
#     print("You can Visit \n1.France \n2.Korea \n3.Canada")
#     sanswer = input("Open 1,2 or 3 : ")
#     if sanswer == "1":
#         print("You can See : \n1.Cathédrale Notre-Dame de Paris\n 2.Musée d'Orsay\n3.Cathédrale Notre-Dame de Paris")
#     elif sanswer == "2":
#         print(
#             "You can See : \n1.N Seoul Tower\n 2.Bukchon Hanok Village\n3.Everland")
#     elif sanswer == "3":
#         print("You can See : \n1.Ripley's Aquarium of Canada\n 2.Royal Ontario Museum\n3.Montmorency Falls")
#     else:
#         print("Maybe you're not ready to travel")
# if answer == "4":
#     print("You can Visit \n1.Auckland \n2.Auli \n3.Goa")
#     sanswer = input("Open 1,2 or 3 : ")
#     if sanswer == "1":
#         print("You can See : \n1.Dehradun\n 2.New-dell\n3.Jodhpur")
#     elif sanswer == "2":
#         print(
#             "You can See : \n1.Ben Youssef Madrasa\n 2.Cascades d'Ouzoud\n3.Crocoparc")
#     elif sanswer == "3":
#         print("You can See : \n1.Butterfly Beach\n 2.Dona Paula Beach\n3.Dona Paula Beach")
#     else:
#         print("Maybe you're not ready to travel")

# #Fourth
# print("Let's focus on future career plans,first question is which direction interests you ? \n1.Front-End \n2.Back-End \n3.UI/UX Design")
# firstAnswer = input("Open1,2 or 3 : ")
# print("How many hours can you devote to studying? \n1) 0 hour \n2) 5 hour \n3) 10 hour")
# secondAnswer = input("Open 1,2 or 3 : ")
# print("Do you like solving problems? \n1) Yes \n2) No ")
# thirdAnswer = input("Open 1 or 2 : ")
#
# if (secondAnswer == "2" or secondAnswer == "3") and firstAnswer == "1" and thirdAnswer == "1":
#     print("You can Learn  a Javascript,HTML,CSS or Angular")
# elif (secondAnswer == "2" or secondAnswer == "3") and firstAnswer == "2" and thirdAnswer == "1":
#     print("You can Learn a C# ,Python,Java,Php or Nodejs")
# elif (secondAnswer == "2" or secondAnswer == "3") and firstAnswer == "3" and thirdAnswer == "1":
#     print("You can Learn a Miro,Figma, Sketch or Flowmapp")
# else:
#     print("You can Find a rich man and marry him :)")

# # fifth
# weekdays = {
#     "1": "Monday",
#     "2": "Tuesday",
#     "3": "Wednesday",
#     "4": "Thursday",
#     "5": "Friday",
#     "6": "Saturday",
#     "7": "Sunday"
# }
# number = input("Enter a number between 1 and 7: ")
#
# if number in weekdays:
#     print("The corresponding weekday is:", weekdays[number])
# else:
#     print("Invalid input. Please enter a number between 1 and 7.")