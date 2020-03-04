# Name: Alejandro Blancas
# CI251
# Homework 3 Program 1: Character analysis

def main():

    file_variable = open("text.txt" , "r")
    textList = []
    for line in file_variable:
        line = line.rstrip("/n")
        mylist = line
        textList.append(mylist)

    
    print("finding number of uppercase Letters in text.txt file")
    totalUpCaLetters = countUpperCase(textList)
    print("number of uppercase Letters : ",totalUpCaLetters)
    print()
    print("finding number of lowercase letters in text.txt file")
    totalLoCaLetters = countLowerCase(textList)
    print("number of Lower case Letters : ",totalLoCaLetters)
    print()
    print("finding number of digits in text.txt file")
    totalDigits = countDigits(textList)
    print("number of digits : ",totalDigits)
    print()
    print("finding number of whitespaces in text.txt file")
    totalWhiteSpaces = countWhiteSpace(textList)
    print("number of whitespaces : ",totalWhiteSpaces)
        
def countUpperCase(anyList):
    count = 0
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].isupper():
                count+= 1
    return count

def countLowerCase(anyList):
    count = 0
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].islower():
                count+= 1
    return count

def countDigits(anyList):
    count = 0
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].isdigit():
                count+= 1
    return count

def countWhiteSpace(anyList):
    count = 0
    for row in range(len(anyList)):
        for i in range(len(anyList[row])):
            if anyList[row][i].isspace():
                count+= 1
    return count

main()
