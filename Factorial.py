# Basically a application to show what is the factorial of the number that user chose


number = int(input('enter a number: '))
if number > 0:
    factorial = 1
    for item in range(1, number + 1):
        factorial = factorial * item
    print('The factorial for this number is:', factorial)
