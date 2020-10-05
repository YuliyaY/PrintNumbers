# Write a program in Python or Java that counts backwards from 100 to 1
# and prints: “Agile” if the number is divisible by 5,
# “Software” if the number is divisible by 3,
# “Testing” if the number is divisible by both,
# or prints just the number if none of those cases are true.


if __name__ == '__main__':

    for x in range(1, 101):
        if (x % 3 == 0) and (x % 5 == 0):
            print("Testing")
        elif x % 3 == 0:
            print("Software")
        elif x % 5 == 0:
            print("Agile")
        else:
            print(x)

