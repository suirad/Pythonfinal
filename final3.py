from random import randint

num1, num2 = randint(1, 100), randint(1,100)

while True:
    try:
        if int(input("What is the sum of {} and {}? ".format(num1, num2))) == num1+num2:
            print("Correct")
            break
        else:
            print("Try again.")
    except ...:
        pass
