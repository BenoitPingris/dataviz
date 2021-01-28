import matplotlib.pyplot as plt
import numpy as np

from utils import read_file

def main():
    data = read_file()

    max_hp = max([item['hp'] for item in data])
    i = 0
    interval = 20
    ranges = []
    while i < max_hp:
        i += interval
        ranges.append(i)
    origins = ['US', 'Japan', 'Europe']
    hps = {origin: {i: 0 for i in ranges} for origin in origins}
    for origin in hps:
        for hp in sorted([item['hp'] for item in data if item['origin'] == origin]):
            i = 0
            while hp > ranges[i]:
                i += 1
            hps[origin][ranges[i]] += 1

    for origin in origins:
        plt.plot(ranges, [hps[origin][v] for v in hps[origin]], label=origin)
    plt.xlabel('Chevaux')
    plt.ylabel('Quantite')
    plt.title('Quantite de voitures en fonction des chevaux')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
