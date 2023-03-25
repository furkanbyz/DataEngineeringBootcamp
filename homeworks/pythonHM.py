import random

def numberGenerator():
    for i in range(50):
        print("Number",i,":")
        number=[5,5,5]
    
        for i in range(7):
            sayı=int(random.random()*10)
            number.append(sayı)

        print(number)
    

numberGenerator()