import matplotlib.pyplot as plt
from utils import read_file

def scatter(data):
    plt.scatter([item['weight'] for item in data], [item['acc']
                                                    for item in data])
    plt.xlabel('Poids')
    plt.ylabel('Acceleration')
    plt.show()

def bar(data):
    plt.bar([item['hp'] for item in data], [item['acc'] for item in data])
    plt.xlabel('Chevaux')
    plt.ylabel('Acceleration')
    plt.show()

def main():
    data = read_file()
    scatter(data)
    #bar(data)

if __name__ == "__main__":
    main()
