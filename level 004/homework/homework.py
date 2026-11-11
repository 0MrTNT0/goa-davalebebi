#1. კომენტარის სახით ახსენით თუ როგორ მუშაობს, რა შედეგი გამოაქვს და რა სიმბოლობით შედგება გაკვეთილზე ნასწავლი მათემატიკური ოპერაცები
#2. მომხმარებელს შემოაყვანინეთ რიცხვი და დაპრინტეთ მისი კვადრატი და კუბი
#3. მომხმარებელს შემოაყვანინეთ ორი რიცხვი და შეასრულეთ ყველა მათემატიკური ოპერაცია
#4. მაღაზიაში არის გარკვეული რაოდენობის კანფეტი, ერთ ყუთში 12 კანფეტი ეტევა
#     მომხმარებელს შემოაყვანინეთ კანფეტების რაოდენობა და გამოთვალეთ:
#     A. სულ რამდენი ყუთი გაივსება
#    B. რამდენი კანფეტი დარჩება
#5. მომხმარებელს შემოაყვანინეთ წუთების რაოდენობა და გამოთვალეთ:
#     A. რამდენი სრული საათია
#     B. რამდენი წუთი დარჩა
#   მაგალითად: 135წთ --> 2 სრული საათი და 15 წუთი


#დავალება 1
# ** ახარისხება | ამრავლებს თავის თვს იმდენჯერ რამდენიც ხარისხია მაგალითად 2 ** 2 = 8
# // მთელი გაყოფა | მთელ ნაწილს გიტოვებს მაგალითად 19 // 5 = 3
# % ნაშთიანი გაყოფა | გაყოფის შემდეგ გიტოვებს მხოლოდ ნაშთს მაგალითდ : 13 % 5 = 3

number67 = int(input("enter your number1: "))
number69 = int(input("enter your number2: "))
print(f"ახარისხება: {number67 ** number69}")
print(f"მთელი გაყოფა: {number67 // number69}")
print(f"ნაშთიანი გაყოფა: {number67 % number69}")

#დავალება 2
Number_1 = int(input("enter your number!: "))
print(f"კვადრატი: {Number_1 * 2}")
print(f"კუბი: {Number_1 ** 3}")


#დავალება 3
number1 = int(input("enter number 1: "))
number2 = int(input("enter number 2: "))

print("გამოკლება: " + str(number1 - number2))
print("მიმატება: " + str(number1 + number2))
print("გამრავლება: " + str(number1 * number2))
print("გაყოფა: " + str(number1 / number2))
print("ახარისხება: " + str(number1 ** number2))
print("მთელი გაყოფა: " + str(number1 // number2))
print("ნაშთიანი გაყოიფა: " + str(number1 % number2))

#დავალება 4
box = int(input("enter your candys: "))
nobox = int(box / 12)
finalcandy = (box - nobox * 12)
print(str(nobox) + ' box of candy ' + str(finalcandy) + ' candy outside the box')



#დავალება 5
minute = int(input("enter your minute: "))
hours = int(minute  / 60)
finalminute = minute - hours * 60
print(str(hours) + ' საათი და ' + str(finalminute) + "წუთი" )