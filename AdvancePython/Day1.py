


Moperation  = int(input('Enter the number of mathematical operations you want to perform:' '\n' ' 1->Addition, 2->Subtraction, 3->Multiplication, 4->Division: '))

# print(Moperation) 

if Moperation == 1:
    a = int(input('Enter first number for addition: '))
    b = int(input('Enter second number for addition: '))
    print('The sum is:', a + b)
    
elif Moperation == 2:
    a = int(input('Enter first number for subtraction: '))
    b = int(input('Enter second number for subtraction: '))
    print('The difference is:', a - b)
    
elif Moperation == 3:
    a = int(input('Enter first number for multiplication: '))
    b = int(input('Enter second number for multiplication: '))
    print('The product is:', a * b)

elif Moperation == 4:
    a = int(input('Enter first number for division: '))
    b = int(input('Enter second number for division: '))
    if b != 0:
        print('The quotient is:', a / b)
    else:
        print('Error: Division by zero is not allowed.')
else:
    print('Invalid operation selected. Please choose a valid option (1-4).')    


