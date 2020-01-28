# Alejandro Blancas
# CI251
# Homework 2 1/23/2020
import matplotlib.pyplot as plt

def main ():
    
    data = []
    num = open(r'GasPriceAverages.txt')
    readNum = num.readlines()

    index = 0
    while index < len(readNum):
        readNum[index] = readNum[index].rstrip('\n')
        index += 1 
    y_coords = readNum
    x_coords = list(range(1,53))

    plt.plot(x_coords, y_coords)
    plt.xlim(xmin=1, xmax=52)
    plt.title('1994 Weekly Gas Averages')
    plt.xlabel('Weeks')
    plt.ylabel('Prices')
    plt.show()

#Bar Graph method
#for i in range(1, len(readNum)):
#    newArr = readNum[i]
#    data.append(newArr)    
#plt.bar(range(len(data)), data)

main()
