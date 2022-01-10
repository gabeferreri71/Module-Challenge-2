import csv


def load_csv(csvpath):
#opens file path to read "r" the .csv file and load the .csv information into the "data" list   
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")
# skips header
        next(csvreader)

        for row in csvreader:
            data.append(row)
    return data
