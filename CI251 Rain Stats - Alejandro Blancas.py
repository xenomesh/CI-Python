# Initalize a list with names of the months

MONTH = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def main():

    rain_stat = print('Input the amount of rainfall for each month')
    #Input
    i = 0
    numbers = []
    sizeOfList = len(MONTH)
    while i < sizeOfList:
        print(MONTH[i], end = ': ')
        numbers.append(input())
        i += 1

    print('\t' 'Details of Rainfall')
    print('------------------------------')
    inputList(numbers)
    print('\n')
    print('\t Summary of rainfall')
    print('------------------------------')
    summary(numbers)
    

def inputList(numbers):
    i = 0
    sizeOfList = len(MONTH)
    while i < sizeOfList:
        result = '{} : {} '.format(MONTH[i], numbers[i])
        i += 1
        print(result, end = ' inch\n')

def summary(numbers):
    newNumbers = [float(i) for i in numbers]
    names = [i for i in MONTH]
    i = 0
    p = ''
    result = 0
    average = 0
    highest = 0
    maxMonth = ''
    sizeOfList = len(MONTH)
    while i < sizeOfList:
        result += newNumbers[i]
        highest = max(newNumbers)
        i += 1
    average = result / sizeOfList
    print('Total rainfall: ', result)
    print('Average rainfall: ', average)
    print('Highest rainfall: ', highest)
    print('The month of highest rainfall: ', maxMonth) #The only solution I can think of is using dict to do a key:value pair.

main()
