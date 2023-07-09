#1 (було не зрозуміло як вивесть число посередині, тому трохи підглянув рішення)

user_input = int(input("Enter the number:   "))

a = user_input // 100
b = (user_input // 10) % 10
c = user_input % 10

d = a + b + c

print(d)

#2

number = float(input("Enter the number  "))

a = number % 1
# виведе дрібну частину
b = round(a, 1)
# округлить дрібну частину до одного символу

print(a)
print(b)

#3

list_ten = [10, 20, 30, 40, 50]
list_ten.reverse()
print(list_ten)

#4



list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]

print(list_of_six)

for a in list_of_six:
    if a % 5 == 0 and a <150:
        print(a)


#5

# це я підглянув впевнений що рішення не вірне. Про те сам зробити не зміг

import random

def a():
    attempt = 3
    while attempt > 0:
        b = input("Enter the number ")
        c = random.randint(1, 10)

        if b == c:
            print("Winner")
            return
        else:
            print("Loser")

        attempt -= 1

    print("Game Over")

a()

#6

#7