a = int(input('enter the first number'))
b = int(input('Enter the second number'))
while True:
    choice = input('Enter a operator(+,-,*,/,%):')
    if choice=='+':
        print('The answer is',a+b)
    elif choice=='-':
        print('The answer is',a-b)
    elif choice=='*':
        print('The answer is',a*b)
    elif choice=='/':
        print('The answer is',a/b)
    elif choice=='%':
        print('The answer is',a%b)
    else:
        print('Invalid operator') 

    


