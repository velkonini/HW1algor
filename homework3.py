import random
#Задача 1
# count = 0
# count2 = 0
# for i in range(2,10):
#       for j in range(2, 100):
#           if j % i == 0:
#               count += 1
#               new_count = count
#       count = 0
#       count2 = i
#       print(str(count2) + " " + str(new_count))

#Задача 2
def reverse_min_max():
    li = [random.randint(1,20) for i in range(10)]
    min = li[0]
    maxel = li[0]
    for i in li:
        for j in li:
            if i < min:
                min = i
            if j > maxel:
                maxel = j
    print(li)
    print(min, maxel)
    indxmin = li.index(min)
    indxmax = li.index(maxel)
    li[indxmin], li[indxmax] = li[indxmax], li[indxmin]
    print(li)

# reverse_min_max()

#Задача 3
def max_negative():
    li2 = [random.randint(-20, -1) for i in range(10)]
    li2.sort()
    print(str(li2[0]) + " -  максимальный отрицательный элемент")

# max_negative()

#Задача 4
def two_min_elements():
    li = [random.randint(1,10) for i in range(15)]
    count = 2
    print(li)
    while count > 0:
        min1 = li[0]
        for i in li:
            if i < min1:
                min1 = i
        print(min1)
        li.remove(min1)
        count -= 1


# two_min_elements()