ch = 'y'
while ch == 'y':
    a = int(input('enter the first number'))
    b = int(input('Enter the second number'))
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
        ch=input("Press y for continue")
        
    


   


    


