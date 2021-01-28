import csv

filename = 'data.csv'

def read_file():
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        next(reader)
        d = []
        for row in reader:
            d.append({
                'id': int(row[0]),
                'car': row[1],
                'mpg': float(row[2]),
                'cylinders': int(row[3]),
                'displacement': float(row[4]),
                'hp': float(row[5]),
                'weight': float(row[6]),
                'acc': float(row[7]),
                'model': row[8],
                'origin': row[9],
                })
        return d

