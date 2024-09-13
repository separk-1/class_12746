import os
import csv

print('The current working directory is ', os.getcwd())

'''The change directory statement below changes the current directory. You can either specify 
the complete path or a path relative to We were in the 12-746 folder,
'''

os.chdir('MyData')
print('After the changing the directory to MyData, the current working directory is ', os.getcwd())

with open('projectdatabase.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # the reader does all the work of parsing the file
    line_count = 0
    for row in csv_reader: # this loops through each row in the csv file
        line_count += 1
    print(f'Processed {line_count} lines.')

os.chdir('..')
print('After moving up one level (..), the current working directory is ', os.getcwd())
