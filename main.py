import csv
import matplotlib.pyplot as plt


filename = 'data.csv'

def read_file():
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        next(reader)
        d = []
        # Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin
        for row in reader:
            d.append({
                'id': row[0],
                'car': row[1],
                'mpg': row[2],
                'cylinders': row[3],
                'displacement': row[4],
                'hp': row[5],
                'weight': row[6],
                'acc': row[7],
                'model': row[8],
                'origin': row[9],
                })
        return d


def main():
    data = read_file()
    plt.scatter([item['hp'] for item in data], [item['mpg']
                                                    for item in data])
    plt.show()

    
if __name__ == "__main__":
    main()
