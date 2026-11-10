#1. მომხმარებელს input-ის დახმარებით კითხეთ სახელი შეინახეთ ცვლადში და print-ის დახმარებით მიესალმეთ: "Hello, სახელი"
#2. მომხმარებელს კითხეთ ასაკი შეინახეთ ცვლადში და გამოთვალეთ თუ რამდენი წლის იქნება ის 5 წლის შემდეგ
#3. მომხმარებელს შემოაყვინენთ დღეების რაოდენობა და გადააქციეთ საათებად
#4. მომხმარებელს კითხეთ ორი რიცხვი და შეინახეთ ცვლადებში: num1, num2 გამოთვალეთ მათი: ჯამი, სხვაობა, ნამრავლი და განაყოფი
#5. მომხმარებელს შემოაყვანინეთ 3 ან მეტი რიცხვი და გამოთვალეთ მათი საშვალო არითმეტიკული

#დავალება 1
name = input("whats your name?:")
print("hello" + " " + name)



#დავალება 2
age = int(input("whats your age?: "))
print(5 + age)



#დავალება 3
days = int(input("Days To Hours :) Enter Day: "))
hours = int(days * 24 )
final_hours = (hours)
print(int(final_hours))




#დავალება 4
num1 = input("Number 1 : ") #სხვაობაზე ვერმივხვდი  რაუნდამექნა
num2 = input("Number 2 : ")

final = int(num1) + int(num2)
final1 = int(num1) * int(num2)
final3 = int(num1) / int(num2)

print(final)
print(final1)
print(final3)


#დავალება 5
number1 = input("Enter Your Number 1 : ")
number2 = input("Enter Your Number 2 : ")
number3 = input("Enter Your Number 3 : ")

shedegi = int(number1) + int(number2) + int(number3)
shedegi2 = int(shedegi) / 3

print(shedegi2)
