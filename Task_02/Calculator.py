num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
opt_sign = input('Enter an operation sign: (+,-,x,/) ')

def operation(opt_sign):
    match opt_sign:
        case '+':
            return num_1+num_2
        case '-':
            return num_1-num_2
        case 'x':
            return num_1*num_2
        case '/':
            if (num_2==0):
                return 'Not Defined'
            return num_1//num_2
        case _:
            return 'Something is wrong!'

print(operation(opt_sign))