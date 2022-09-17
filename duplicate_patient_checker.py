# Program that checks on CSV file for duplicate patients based on last/first name and date of birth
import csv

filename = 'pt_d.csv'

fullname = []

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        # append lastname, firstname, date of birth as a list
        fullname.append([row[0], row[1], row[7]])

# sort by last name
fullname.sort()

# Creating an empty list that will add in duplicate names
duplicates = []

# Write duplicates in separate file
with open('duplicates.csv', 'w', encoding='UTF-8', newline='') as duplicatefile:
    writer = csv.writer(duplicatefile)
    for i in range(0, len(fullname) - 1):
        if fullname[i] == fullname[i + 1]:
            duplicates.append(fullname[i])
    writer.writerows(duplicates)

