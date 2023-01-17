import numpy as np


class KMeans:
    k = 1

    def __init__(self, k):
        self.k = k

    def fit(self, X):
        pass

    def init_centroids(self, points):
        x_sum, y_sum = 0, 0
        points_count = len(points)

        for i in range(points_count):
            x_sum += points[i][0]
            y_sum += points[i][1]
        x_sum /= points_count
        y_sum /= points_count
        R = 0
        for i in range(points_count):
            R = max(R, dist([x_sum, y_sum], points[i]))
        # centroids
        centroids = []
        for i in range(self.k):
            x_cntr = x_sum + R * np.cos(2 * np.pi * i / self.k)
            y_cntr = y_sum + R * np.sin(2 * np.pi * i / self.k)
            centroids.append([x_cntr, y_cntr])
        return centroids

def random_point(n):
    points = []
    for i in range(n):
        points.append(np.random.randint(1, 100, 2))
    return  points

def dist(p_i, p_j):
    return np.sqrt((p_i[0] - p_j[0])**2 + (p_i[1] - p_j[1])**2)

if __name__ == '__main__':
    X = random_point()

    kmeans = KMeans(4)
    kmeans.fit(X)
