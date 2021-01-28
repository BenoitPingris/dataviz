import matplotlib.pyplot as plt
from utils import read_file

def histogram(data):
    plt.hist([item['weight'] for item in data], edgecolor='black')
    plt.legend()
    plt.xlabel('Poids')
    plt.ylabel('Nombre')
    plt.axvline(sum([item['weight'] for item in data])/len(data), color='red')
    plt.show()

if __name__ == "__main__":
    histogram(read_file())
