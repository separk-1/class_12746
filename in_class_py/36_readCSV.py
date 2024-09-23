import csv
""" As the csv_reader goes through the rows, it puts each the value of the cell into 
    a string variable with an index corresponding to the column number. We will go
    into the syntax in the next class because storing everything as strings isn't useful.
    This code came from the tutorial  https://realpython.com/python-csv/"""

with open('myData/sampleCSVFile.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',') # the reader does all the work of parsing the file
    line_count = 0
    for row in csv_reader: # this loops through each row in the csv file
        if line_count == 0: # if it's the first row, print the column headers
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else: # otherwise, print the value in the row for each header
            print(f'\t{row[0]} {row[1]} is taking {row[2]} {row[3]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
