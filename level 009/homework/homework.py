# 1. კომენტარის სახით, თქვენი სიტყვებით ახსენით როგორ მუშაობს if else-ი
# 2. მომხმარებელს შემოაყვანინეთ რიცხვი და შეამოწმეთ ეს რიცხვი ლუწია თუ კენტი, თუ ლუწია დაპრინტეთ: "Number is even" თუ არა: "Number is odd"
# 3. მომხმარებელს შემოაყვანინეთ სრული გადასახადი და თუ ეს რიცხვი 100-ზე მეტია მიეცით 10%-იანი ფასდაკლება თუ არა დაუპრინტეთ: "No discount!"
# 4. მომხმარებელს შემოაყვანინეთ ტემპერატურა და შეამოწმეთ, თუ ტემპერატურა 25-ზე მეტია დაუპრინტეთ: "It's hot outside!" თუ არა: "It's not hot outside!"
# 5. მომხმარებელს შემოაყვანინეთ ორი რიცხვი და შეადარეთ რომელი უფრო მეტია

#1  if არის პირველ ხასრისხიანი პირობა რომელიც უნდა გამოვიყენოთ პირველი if ის გარეშე elif და else ვერ გამოვიყენებთ
#რაც შეეხება else-ს რაც შეეხება საბოლოო პირობაა თუ არც ერთ სხვა დანარჩენ პირობას არ დაეთნხმა


#2
# user = input("შეიყვანე რიცხვი: ")

# num = int(user)

# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")


#3
# num = float(input("enter your price: "))

# if num < 0 or num < 100 :
#     print("No discount!")
# else:
#     print("u got 10% discount")


#4
# temperature = float(input("enter temperature: "))

# if temperature > 25:
#     print("It's hot outside!")
# else:
#     print("It's not hot outside!")

#5
# num1 = float(input("enter your number1: "))
# num2 = float(input("enter your number2: "))

# if num1 < num2:
#     print("მეტია!")
# else:
#     print("ნაკლებია")