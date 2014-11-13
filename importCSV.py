import csv
with open('/Users/Bernard/GitHub/Repos1/sb407.csv',newline='') as csvfile:
    spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
    next(csvfile)   #skips the headers
    for row in spamreader:
        print(', '.join(row))

