# 1. კომენტარის სახით თქვენი სიტყვებით ახსენით როგორ მუშაობს and, or და not-ის ლოგიკა
# 2. შექმენით ავტორიზაციის სისტემა: მომხამრებელს შემოაყვანინეთ username-ი და password-ი, შეამოწმეთ თუ username-ი უდრის: "admin"-ს და პაროლი უდრის: "admin123", მაშინ დაუპრინტეთ: "Login successful!" სხვა შემთხვევაში: "Login failed!"
# 3. მომხმარებელს შემოაყვანინეთ ერთი კვირის დღე, თუ ეს დღე არის saturday ან sunday მაშინ დაპრინტეთ: "It's the weekend!", სხვა შემთხვევაში: "It's a working day!"
# 4. მომხმარებელს შემოაყვანინეთ სრული გადასახადი, თუ ეს რიცხვი 100-ზე მეტია ან ტოლია და 500-ზე ნაკლებია დაუპრინტეთ: "You received a 10% discount!", სხვა შემთხვევაში: "No discount available!"
# 5. მომხმარებელს შემოაყვანინეთ ტემპერატურა, თუ ეს რიცხვი ნაკლებია 0-ზე ან მეტია 35-ზე დაუპრინტეთ: "Extreme temperature!", სხვა შემთხვევაში: "Temperature is normal!"
# 6. მომხმარებელს შემოაყვანინეთ რიცხვი, თუ ეს რიცხვი უნაშთოდ იყოფა 3-ზე ან 5-ზე დაპრინტეთ: "Special number!", სხვა შემთხვევაში: "Regular number!"
# 7. კომენტარის სახით მიუწერეთ თუ რა იქნება შედეგი(True/False):
#     A. not True or False and not True
#     B. True and not False or False
#     C. not (True or False) and True
#     D. False or True and not (False or False)
#     E. not True and (False or True) or False


#1
# and - ორივე პირობის შესრულებას ითოვს
# or - ითხოვს რომ შესრულეს ერთი პირობა მაინც
# not - ეუბნება კოდს რომ შეანაცვლოს მნიშნელობა


#2
# user = input("enter your username: ")
# password = input("enter your password: ")

# if user == "admin" and password == "admin123":
#     print("Login successful!")
# else:
#     print("Login failed!")


#3
# day = input("enter your day!: ")

# if day == "saturday" or day == "sunday":
#     print("It's the weekend!")
# else:
#     print("It's a working day!")

#4
# pay = float(input("enter your number: "))
# if pay >= 100 and pay < 500:
#     print("You received a 10% discount!")
# else:
#     print("No discount available!")


#5
# temperature = float(input("enter temperature:  "))

# if temperature < 0 or temperature > 35:
#     print("Extreme temperature!")
# else:
#     print("Temperature is normal!")


#6
# number = int(input("enter your number: "))
# if number % 3 or number % 5:
#     print("Special number!")
# else:
#     print("Regular number!")


#7
#     A. not True or False and not True | false
#     B. True and not False or False | true
#     C. not (True or False) and True | false
#     D. False or True and not (False or False) | true
#     E. not True and (False or True) or False | false