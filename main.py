# #Задача 1
# number = int(input('Введите число: '))
# third_number = number % 10
# sec_number = int(number / 10) % 10
# first_number = int(int(number / 10) / 10)
#
# sum = first_number + sec_number + third_number
# mult = first_number * sec_number * third_number
#
# print(first_number, sec_number, third_number)
# print('Сумма цифр трехзначного числа: ' + str(sum))
# print('Результат умножения трехзначного числа: ' + str(mult))
#


# Задача 5

def eng_alphabet(letterOne, letterTwo):
    alphabet = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    new_eng = alphabet.split(",")
    print(new_eng)
    for i in new_eng:
        if letterOne == i:
            letterOneInd = new_eng.index(i) + 1
            print(letterOneInd)
        if letterTwo == i:
            letterTwoInd = new_eng.index(i) + 1
            print(letterTwoInd)

    if letterOneInd > letterTwoInd:
        print("Расстояние между буквами: " + str(letterOneInd - letterTwoInd))
    else:
        print("Расстояние между буквами: " + str(letterTwoInd - letterOneInd))

# eng_alphabet("B", "Z")


#Задача 8

def leapyear(year):
    if year % 4 == 0 or year % 100 !=0  and year % 400 == 0:
        print("Год високосный")
    else:
        print("Год невисокосный")

#leapyear(2013)

# Доп. задача 1

def delete_duples():
    li = [2, 2, 4, 5, 22, 5, 29, 14, 23, 23, 3, 7, 17, 4]
    for i in li:
        while li.count(i) > 1:
            li.remove(i)
    print(li)

#delete_duples()

# Доп. задача 2

def movezeros():
    li2 = [0, 1, 2, 0, 11, 17, 0 ,3]
    zero_count = 0
    for i in li2:
        if i == 0:
            zero_count += 1
            li2.remove(i)
    while zero_count > 0:
        li2.append(0)
        zero_count -=1
    print(li2)

#movezeros()