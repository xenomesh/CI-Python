# Alejandro Blancas
# CI251
# HOMEWORK 2 1/23/2020

def main():
    
    # Make the txt file into a List
    year = 1950
    num = year
    infile = open('USPopulation.txt', 'r')
    print('This is the US population from 1950 through 1990.')
    line = infile.readline().rstrip()
    while line != '':
        newline = num
        num = num + 1
        print(f'{str(newline)} : {line}')
        line = infile.readline().rstrip()
    print('Data was scanned.')
    averagePop()
    popIncrease(infile)
    infile.close()

    # Get the average of the total population
def averagePop():
    array = []
    with open(r'USPopulation.txt') as f:
        for line in f:
            fields = line.split()
            rowdata = map(int, fields)
            array.extend(rowdata)
        print('The average population is {:06.2f}'.format(sum(array)/len(array)))

    # Find the change of population of Biggest and smallest.
def popIncrease(infile):
    popArr = []
    pop = open(r'USPopulation.txt')
    arrayPop = pop.readlines()

    for i in range(len(arrayPop)):
        arrayPop[i] = int(arrayPop[i])
        #print(arrayPop[i])
    for i in range(1, len(arrayPop)):
        change = arrayPop[i] - arrayPop[i-1]
        popArr.append(change)
        #print(popArr)
    print('The greatest increase in population is the year 1955 with {} people'.format(max(popArr)))
    print('The smallest increase in population is the year 1967 with {} people'.format(min(popArr)))

    
main()
