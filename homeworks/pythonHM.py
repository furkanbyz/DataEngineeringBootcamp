import random


def numberGenerator():
    for i in range(50):
        number = [5, 5, 5, "-"]

        for i in range(3):
            list1 = [1, 2, 3]
            number.append(random.choice(list1))

        number.append("-")

        for i in range(4):
            sayı = int(random.random()*10)
            number.append(sayı)

        my_str = ''.join(map(str, number))
        print(my_str)


numberGenerator()
