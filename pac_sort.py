from math import sqrt
# Import Dataset Here


def euclidean_dist(vector1, vector2):
    size = len(vector1)-1   # Ignore output value in csv file
    dist = 0
    for x in range(size):   # Extend for all kinds of feature vectors
        dist += (vector1[x] - vector2[x])**2
    return sqrt(dist)


def get_dist(tuple):
    return tuple[1]


def get_neighbours(train, test_row, neighbour_count):
    dists = list()
    for train_row in train:
        dist = euclidean_dist(test_row, train_row)
        dists.append((train_row, dist))
    dists.sort(key=get_dist)
    neighbours = list()
    for i in range(neighbour_count):
        neighbours.append(dists[i][0])
    return neighbours


test_dataset = [[2.7810836, 2.550537003, 0],
                [1.465489372, 2.362125076, 0],
                [3.396561688, 4.400293529, 0],
                [1.38807019, 1.850220317, 0],
                [3.06407232, 3.005305973, 0],
                [7.627531214, 2.759262235, 1],
                [5.332441248, 2.088626775, 1],
                [6.922596716, 1.77106367, 1],
                [8.675418651, -0.242068655, 1],
                [7.673756466, 3.508563011, 1]]

neighbours = get_neighbours(test_dataset, test_dataset[0], 3)
for neighbour in neighbours:
    print(neighbour)
