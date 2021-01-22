import csv
import matplotlib.pyplot as plt


filename = 'data.csv'

def read_file():
    with open(filename, 'r') as fd:
        reader = csv.reader(fd, delimiter=';')
        next(reader)
        d = []
        # Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin
        for row in reader:
            d.append({
                'car': row[0],
                'mpg': row[1],
                'cylinders': row[2],
                'displacement': row[3],
                'hp': row[4],
                'weight': row[5],
                'acc': row[6],
                'model': row[7],
                'origin': row[8],
                })
        return d


def main():
    data = read_file()
    plt.scatter([item['origin'] for item in data], [item['hp']
                                                    for item in data])
    plt.show()

    
if __name__ == "__main__":
    main()
