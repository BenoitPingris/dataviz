import matplotlib.pyplot as plt
from utils import read_file

def pie(data):
    explode = (0, 0, 0)
    nbr = [[item['origin'] for item in data].count('US'), [item['origin'] for item in data].count('J
apan'), [item['origin'] for item in data].count('Europe')]
    fig1, ax1 = plt.subplots()
    labels = ['US', 'Japan', 'Europe']
    ax1.pie(nbr, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

if __name__ == "__main__":
    pie(read_file())
