# 1. მომხმარებელს შემოაყვანინეთ ასაკი. თუ ასაკი 18-ზე ნაკლებია, დაუპრინტეთ "You are a minor!", თუ ასაკი 18-დან 64-ის ჩათვლით არის, დაუპრინტეთ "You are an adult!", სხვა შემთხვევაში დაუპრინტეთ "You are a senior!"
# 2. მომხმარებელს შემოაყვანინეთ ორი რიცხვი. შეადარეთ ისინი და დაუპრინტეთ რომელი რიცხვია უფრო დიდი. თუ რიცხვები ერთმანეთის ტოლია, დაუპრინტეთ "Numbers are equal!"
# 3. შექმენით მარტივი კალკულატორი. მომხმარებელს შემოაყვანინეთ ორი რიცხვი და მათემატიკური ოპერაცია (+, -, *, /). if, elif და else-ის გამოყენებით შეასრულეთ შესაბამისი მოქმედება და დაუპრინტეთ შედეგი. გაითვალისწინეთ, რომ ნულზე გაყოფა არ შეიძლება
# 4. მომხმარებელს შემოაყვანინეთ ტემპერატურა და ამინდის მდგომარეობა (sunny, rainy, snowy). თუ ტემპერატურა 25-ზე მეტია და ამინდი მზიანია, დაუპრინტეთ "Perfect weather for a walk!", თუ ამინდი წვიმიანი ან თოვლიანია, დაუპრინტეთ "Bad weather for a walk!", სხვა შემთხვევაში — "Normal weather!"
# 5. მომხმარებელს შემოაყვანინეთ სამი ინფორმაცია: username, password და ასაკი. თუ username არის "admin", password არის "Adm1n_123" და ასაკი 18 ან მეტია, დაუპრინტეთ "Full access granted!". თუ username და password სწორია, მაგრამ ასაკი 18-ზე ნაკლებია, დაუპრინტეთ "Limited access!". სხვა შემთხვევაში დაუპრინტეთ "Access denied!"


#1
# age = int(input("Enter Your Age: "))

# if age < 18:
#     print("You are a minor!")
# elif age <= 64:
#     print("You are an adult!")
# else:
#     print("You are a senior!")


#2
# num1 = float(input("Enter Number 1: "))
# num2 = float(input("Enter Number 2: "))

# if num1 < num2:
#     print("number 2 is higher")
# elif num1 > num2:
#     print("Number 1 is higher")
# elif num1 == num2:
#     print("Numbers are equal!")


#3
# num1 = float(input("enter number1: "))
# num2 = float(input("enter number2: "))
# math = input("enter math operation: ")

# if math =="+":
#     print(num1 + num2)
# elif math =="-":
#     print(num1 - num2)
# elif math =="*":
#     print(num1 * num2)
# elif math =="/":
#     if num2 == 0:
#         print("nulze ariyofa dzami")
#     else:
#         print(num1 / num2)


#4
# weather = input("enter Weather: ")
# temperature = float(input("enter Temperature: "))

# if temperature >= 25 and weather == "sunny":
#     print("Perfect weather for a walk!")
# elif weather == "rainy" or weather == "snowy":
#     print('Bad weather for a walk!')
# else:
#     print("Normal weather!")


#5
# user = input("enter your user: ")
# passw = input("enter your password: ")
# age = int(input("enter your age: ")) 

# if user == "admin" and passw == "admin123" and age >= 18:
#     print("Full access granted!")
# elif user == "admin" and passw == "admin123" and age < 18:
#     print("Limited access!")
# else:
#     print("Access denied!")