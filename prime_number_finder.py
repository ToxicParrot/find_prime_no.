#first project on github
#this is gonna just be an interview test, nothing special, just the prime number finder 

'''
EDIT
I used the function and tested everything was correct. I now want to put it in a loop so that I can continue using the code without having to run it each time.
so i'm going to tab everyhing and place it in a while function that checks if a variable is true. if i choose to stop the loop, the variable will be set to false 
and this will end the code 
'''

loop = True 

while loop == True: 
    #Going to make this a little more personal by using user inputs to drive a code
    user_num = input('which number do you want to check: \n')

    #defining a function that I can run to check whether the number is a prime or not
    def prime_check(num): 
        #going to create a loop that checks the number against all previous numbers
        #ERROR FIX: the input i used from user_num is a string, it first needs to be convereted to be used in my loop 
        num = int(num)
        for i in range(2, num): 
            #check if the number is divisible by every number in the range, if it is and return 0 remainders then we know it is not a prime and can break the loop
            if num % i == 0: 
                return False 
                break
        #if the num % i expression doesn't return 0 then we know it is a prime, thus returning True. I will use this later to Drive a string reply
        else: return True
    print(" ")
    #creating an if statement to check what was returned in my function, if True then return a string saying its a prime, if False then return saying its not.
    if prime_check(user_num) == True: 
        print('{number} is a prime number!'.format(number = user_num))
    else: print('{number} is not a prime number!'.format(number = user_num))
    print('')
    
    #creating the choice to loop and find another number
    choice = input('would you like to check another number? Y/N  \n')

    if 'n' in choice.lower():
        print('____________________________________')
        #I can either use the break function to stop the loop, or set loop to False. in this case I used the break function to make the code less noisey.
        break
    else:
         print('____________________________________')






