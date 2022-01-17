import math
x1 = 1
x2 = 1
pee = [x1, x2]


def make_seq(x1, x2):
    i = 1
    while i < num:
        x1 = x1 + x2
        x2 = x1 + x2
        pee.append(x1)
        pee.append(x2)
        i += 1


num = int(input("Which fibonacci number would you like?: "))
higher_digits = str(math.floor(num / 10))
make_seq(1, 1)

if num > 20 and num % 10 == 1:
    print("The " + higher_digits + "1st fibonacci number is: " + str(pee[num - 1]))
elif num > 20 and num % 10 == 2:
    print("The " + higher_digits + "2nd fibonacci number is: " + str(pee[num - 1]))
elif num > 20 and num % 10 == 3:
    print("The " + higher_digits + "3rd fibonacci number is: " + str(pee[num - 1]))
else:
    print("The " + str(num) + "th fibonacci number is: " + str(pee[num - 1]))
