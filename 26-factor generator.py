#Factor Generator App

print('Welcome to the Factor Generator App')

while True :
    number = int(input('\nEnter a number to determine all factors of that number : '))
    factors = []
    print('\nFactors of ', number , 'are : ' )
    for i in range(1,number+1):
        if number % i == 0:
            factors.append(i)
            print(i)
    print('\nIn summary: ')
    for i in range(len(factors)):
        print("\n",factors[i] ,' *', int(number/factors[i]) , ' =' , number )
    run_again = input('\nRun again(y/n)').lower().strip()

    if run_again == 'n':
        print('Thanks for playing ')
        break
        
        
