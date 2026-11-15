# 1. კომენტარის სახით თქვენი სიტყვებით ახსენით რა არის input და როგორ ვიყენებთ
# 2. კომენტარის სახით თქვენი სიტყვებით ახსენით რა არის type casting-ი
# 3. კომენტარის სახით ჩამოწერეთ ყველა ნასწავლი მონაცემთა ტიპები და მიუწერეთ მაგალითები
# 4. კომენტარის სახით ჩამოწერეთ გაკვეთილზე ნასწავლი შედარების ოპერატორები და დაწერეთ მათი დანიშნულება/რას აკეთებენ
# 5. მომხმარებელს შემოაყვანინეთ ორი რიცხვი და დაპრინტეთ ყველა მათემატიკური შედარების ოპერაცია
# 6. მომხმარებელს შემოაყვანინეთ ასაკი და შეამოწმეთ არის თუ არა ის 18-ის ან მეტის
# 7. ავტომობილი მიდის A ადგილიდან B ადგილას, მომხმარებელს შემოაყვანინეთ: 
#     ავტომობილის სიჩქარე(კმ/სთ)
#     გასავლელი მანძილი(კმ)
#     დრო(სთ)
#    გამოთვალეთ: რამდენი დრო დასჭირდება ავტომობილს დანიშნულ ადგილას მისასვლელად და ჩაეტევა თუ არა დროში(True/False)
# 8. მომხმარებელს შემოაყვანინეთ სამი ან მეტი პროდუქტის ფასი და თანხა რამდენიც აქვს, შეამოწმეთ თუ ეყოფა თანხა(True/False)
# 9. კომპიუტერში მომხმარებელს სურს პროგრამის გადმოწერა, მომხმარებელს შემოაყვანინეთ პროგრამის ზომა(GB) და თავისუფალი ადგილი კომპიუტერში(GB). შეამოწმეთ ეყოფა თუ არა თავისუფალი მეხსიერება მომხმარებელს რომ პროგრამა გადმოწეროს(True/False)
# 10. შექმენით საგნების ცვლადები, მაგ: math, history, art... და მომხმარებელს შემოაყვანინეთ წლიური ნიშნები ამ საგნების, გამოთვალეთ საშვალო არითმეტიკული და შეამოწმეთ პასუხი თუ აღემატება 5-ს და მომხმარებელს თუ ელის სახლში გალახვა
# 11. ამ კოდებში error-ებია, იპოვეთ ეს error-ები, კომენტარის სახით ახსენით თუ რა არის შეცდომა და დაწერეთ სწორი ვერსია:

# num1 = input("Enter first number: ")
# num2 = int(input("Enter second number: "))

# result = num1 + num2
# print(result)



# num1 = int(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# result = num1 - "5" * num2
# print(result)



# hours = input("Enter hours worked: ")
# rate = float(input("Enter hourly rate: "))
# bonus = input("Enter bonus: ")

# salary = hours * rate
# total = salary + bonus
# final_salary = total / "2"

# print(final_salary)



# price = float(input("Enter product price: "))
# quantity = input("Enter quantity: ")
# discount = float(input("Enter discount percentage: "))

# subtotal = price + quantity
# discount_amount = subtotal * discount
# final_price = subtotal - "10"

# print(int(final_price))



# num1 = int(input("Enter first number: "))
# num2 = input("Enter second number: ")
# num3 = float(input("Enter third number: "))

# total = num1 + num2
# average = total / num3
# remainder = average % "2"
# result = int(remainder + num1)

# print(result)





#1 input-ით შეგვიძლია მომხარებელს ინფორმაცია შემოვაყვანინოთ


#2 type casting არის მონაცმეთ ტიპის გარდაქმნა მაგალითდ მთელი რიცხვი ათწილადში 


#3 მონაცემთა ტიპები:
# string/str - სტრინგი ინახავს მონააცემებს ბრჭყალებში - ""   ''
# integer/int - ინტიჯერი ინახავს რიცხვებს მაგალითად - 1,-3 ,300 ,-3938,5000
# float/float - ფლოატი ინახავს ათწილად რიცხვებს - 1.0, 18.2 , -37,2 ,38.1 , 12.7
# boolean/bool - ბულინი არის მონაცემთ ტიპი რომელსაც აქვს მხოლოდ ორი მნიშვნელობა True და False


#4  შედარების ოპერატორიები:
# <   ,   >   ,   <=  ,   >=  ,   ==  ,   !=

# age =  int(input("enter your age: "))
# if age < 0 or age > 100 :
#     print("მკვდარიხარ :(")

# trafficlight = input("enter your color: ")
# if trafficlight == "red" or trafficlight == "yellow":
#     print("გაჩერდი ბრაატ!")
# else:
#     print("წადი ბრატ მწავნეა!")


#5
# num1 = float(input("enter your first number: "))
# num2 = float(input("enter your second number: "))

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 ** num2)
# print(num1 // num2)
# print(num1 % num2)


#6
# age = int(input("enter your age: "))
# print(age >= 18)


#7
# v = float(input('შემოიყვანე ავტომობილის სიჩქარე (კმ/სთ): '))
# s = float(input('შემოიყვანე გასავლელი მანძილი (კმ): '))
# t1 = float(input('რამდენი დრო გაქვს მისასვლელად: '))
# t2 = s/v
# if t1 >= t2:
#     print(True)
# else:
#     print(False)


#8

# product1 = float(input("enter product1 price: "))
# product2 = float(input("enter product2 price: "))
# product3 = float(input("enter product3 price: "))
# money = float(input("enter your money: "))

# totalp = product1 + product2 + product3
# if money >= totalp:
#     print(True)
# else:
#     print(False)


#9
# sizep = float(input("enter program size(gb): "))
# freespace = float(input("enter free space on your pc(gb): "))

# if freespace >= sizep:
#     print(True)
# else:
#     print(False)


#10
# math = float(input("შეიყვანე მათმატიკის წლიური ნიშანი: "))
# history = float(input("შეიყვანე ისტორიის წლიური ნიშანი: "))
# art = float(input("შეიყვანე ხელოვნების წლიური ნიშანი: "))

# total = (math + history + art) / 3
# if total > 5:
#     print("გადარჩი!")
# else:
#     print("დააგერხა სახლშ გაიტყიპები (⊙_⊙;)")

#11
#11.1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2
print(result)

#11.2
num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 - 5 * num2
print(result)


#11.3
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
bonus = float(input("Enter bonus: "))

salary = hours * rate
total = salary + bonus
final_salary = total / 2

print(final_salary)


#11.4
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))

subtotal = price + quantity
discount_amount = subtotal * discount
final_price = subtotal - 10

print(int(final_price))

#11.5
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = num1 + num2
average = total / num3
remainder = average % 2
result = int(remainder + num1)

print(result)

