#Programmer: Alejandro Blancas
#CI251 - Homework 3 Program 2
#Date: 2.10.2020
from datetime import datetime

def main():

    DATE_FORMAT = '%m-%d-%Y'
    file_name = 'GasPrices.txt'
    gasPrices = read_file(file_name, DATE_FORMAT)
    average_price(gasPrices)
    average_price_per_month(gasPrices)
    high_low_prices_per_year(gasPrices)
    sort_prices(gasPrices, descending = False, newFile = 'low_to_high.txt')
    sort_prices(gasPrices, descending = True, newFile = 'high_to_low.txt')
    
def get_value(x):
    return x[1]

def average_price(file_name):
    avg_dict = dict()
    for date_value in file_name:
        if date_value.year in avg_dict:
            avg_dict[date_value.year].append(float(file_name[date_value]))
        else:
            avg_dict[date_value.year] = [float(file_name[date_value])]
    for year in avg_dict:
        values = avg_dict[year]
        print("The average price in {Year} is ${cost:.3f}/gallon".format(Year = year, cost = sum(values)/len(values)))

def average_price_per_month(file_name):
    avg_dict = dict()
    for i in file_name:
        month_year = i.strftime('%m-%Y')
        #print(month_year)
        if month_year in avg_dict:
            avg_dict[month_year].append(float(file_name[i]))
        else:
            avg_dict[month_year] = [float(file_name[i])]
    for month in avg_dict:
        values = avg_dict[month]
        print("The average price in {Month} is ${cost:.3f}/gallon".format(Month = month, cost = sum(values)/len(values)))

def high_low_prices_per_year(file_name):
    price_dict = dict()
    for i in file_name:
        if i.year in price_dict:
            price_dict[i.year].append(float(file_name[i]))
        else:
            price_dict[i.year] = [float(file_name[i])]
    for year in price_dict:
        values = price_dict[year]
        print("In {Year}, the highest gas price is ${highest} and the lowest gas price is ${lowest}".format(Year = year, highest = max(price_dict[year]), lowest = min(price_dict[year])))

def sort_prices(file_name, descending, newFile):
    sorted_prices = sorted(file_name.items(), key = get_value, reverse = descending)
    with open(newFile, 'w') as file_object:
        file_object.write("Date\tPrice($/gallon)\n")
        for i, rate in sorted_prices:
            file_object.write("{i}\t{cost}\n".format(i = i.strftime('%d-%m-%y'), cost = rate))
    
def read_file(file_name, DATE_FORMAT):
    price_dictionary = dict()
    with open(file_name, 'r') as xfile:
        file_contents = xfile.readlines()
        for line in file_contents:
            date, price = line.strip('\n').split(":")
            price_dictionary[datetime.strptime(date, DATE_FORMAT)] = price
            #print(price_dictionary)
        return price_dictionary

main()
