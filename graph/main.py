import numpy
import networkx as nx

def weight(n):
    array = numpy.zeros(n, n)
    for i in range(n):
        for j in range(i + 1, n):
            array[i][j] = array[j][i] = numpy.random.randint(10, 100)
    return array

if __name__ == '__main__':
    print(weight())
