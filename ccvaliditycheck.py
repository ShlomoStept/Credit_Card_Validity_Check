#===================================================================================================================================================================================
# Author: Shlomo Stept
# ccvaliditycheck.py will open up a window and determine if any credit card number; entered by the user, is valid.
#===================================================================================================================================================================================


# Prompt for User to Enter A credit Card number as a long integer
userInput = input("Enter Your Credit Card Number as a long integer: ")


# Initilizing variables to keep track of, the Sum of every other even and odd, credit card number
totalEven=0
totalOdd=0

# Variable that detemines the number of loops requred due to length of the credit card number entered
numberofVariables = len(userInput)

# Initalizing variables to keep track of the Loop the program is on, and this is also determine/track the List/ (array) vairable the program needs to use/pull from the userInput
countEven = numberofVariables-2
countOdd = numberofVariables-1


# Test to determine of the credit card value entered is the correct length of a credit card (some new cards have 19 digits)
if numberofVariables > 12 and numberofVariables < 20:

# loop that runs through every ODD number moving from right to left (of the credit card) and adds them all up 
    for loopcounter in range(numberofVariables,0,-2):
        oddPlacesSingle = int(userInput[countOdd])
        totalOdd = totalOdd + oddPlacesSingle
        countOdd = countOdd - 2

# loop that runs through every EVEN number moving from right to left (of the credit card); doubles that number and then adds them all up           
    for loopcounter in range(numberofVariables-1,0,-2):
        evenPlacesDouble = 2 * int(userInput[countEven])
        
# Evaluation, whether the doubling, results in a value more than one digit, and if it does, adds the two digits to get a single digit number
        if len(str(evenPlacesDouble)) > 1:
            evenPlacesDouble = str(evenPlacesDouble)
            evenPlacesDouble = int(evenPlacesDouble[0]) + int(evenPlacesDouble[1])
        else:
            exit
            
        totalEven = totalEven + evenPlacesDouble
        countEven = countEven - 2
        
# Variable that takes the total of Even values that were doubles, and the total of all ODD values that were just summed, and adds the total odd and total even up       
    total = totalEven + totalOdd

# Test to determine if the Grand total, of odd-single and doubled-Even values is divisable by ten. The final step in determining the Validity of the Credit Card Number entered
    if len (str(total)) > 1:
        total = str( total )
        if int ( total [ (len(str(total))) -1 ]) == 0:




# Test to determine of the credit card  number entered is associated with VISA, MASTERCARD, DISCOVER, OR AMERICAN EXPRESS.  
            if int(userInput[0]) == 3 and int(userInput[1]) == 7 :
                print("\n\tYour American Express card is Valid, Congragulations!")

            elif int(userInput[0]) == 4:
                print("\n\tYour Visa card is Valid, Congragulations!")

            elif int(userInput[0]) == 5:
                print("\n\tYour Master Card card is Valid, Congragulations!")

            elif int(userInput[0]) == 6:
                print("\n\tYour Discover card is Valid, Congragulations!")
            else:
                print("\n\tYour Alternative credit card is Valid, Congragulations!")


# TEST RESULTS that return an invalid, if the credit card number failed to be devided by ten or any of the other validity tests previously run. 
        else:
            print("\nYour card is Invalid, Please try again.")
    else:
        print("\nYour card is Invalid, Please try again.")
else:
    print("\nYour card is Invalid,Please try again.")
