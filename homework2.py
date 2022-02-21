# Задача 1
def even_and_odd(num):
    even = 0
    odd = 0
    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    print("Четных чисел: " + str(even))
    print(("Нечетных чисел: " + str(odd)))
# even_and_odd(357896)

# Задача 2
def reverse_num(x):
    rev_x = 0
    while x > 0:
        rev_x = rev_x * 10 + x % 10
        x = x // 10

    print(rev_x)

# reverse_num(756)



# Задача 8

def duples_num():
    count = 0
    number = int(input("Введите число "))
    count_number = int(input("Какую цифру нужно посчитать: "))
    while number > 0:
        new_number = number % 10
        if new_number == count_number:
            count += 1
        number = number // 10
    print("Цифра " + str(count_number) + " встречается " +  str(count) + " раз(а)")


# duples_num()

# Задача 9

def sum():
    number = int(input("Введите число: "))
    max_summ = 0
    max_number = 0
    while number != 0:
        new_number = number
        summ = 0
        while number > 0:
            summ = summ + number % 10
            number = number // 10
        if summ > max_summ:
            max_summ = summ
            max_number = new_number
    number = int(input("Введите число: "))
    print("Максимальная сумма: " + str(max_summ) + " число: " + str(max_number))

# sum()

# Задача 4
def sum_of_elements():
    x = int(input("Сколько элементов нужно сложить: "))
    sum = 0
    element = 1
    while x > 0:
        sum = element + (element / 2)
        x -= 1
        # element = element / 2

    print(sum)

sum_of_elements()

#