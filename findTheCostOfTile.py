state = True
print('Welcome!')
while state == True:
    print('To find out the cost of your tiles to cover a floor plan please enter the height:')
    height = int(input())

    print('Please enter the width:')
    width = int(input())

    print('And finally, please enter the cost of a tile in GBP:')
    cost = float(input())

    totalArea = height * width
    totalCost = totalArea * cost

    print('The total cost is: £' + str(totalCost) + ' for you to cover a total area of ' + str(totalArea) + 'm squared.')

    print('Would you like to work out the cost of another area?')
    userDecision = input()

    if userDecision.upper() == 'YES' or userDecision.upper() == 'Y':
        state = True
    else:
        state = False
    