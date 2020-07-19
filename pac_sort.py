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


def get_neighbours(train_set, test_row, neighbour_count):
    # Get distances of each rows and sort
    dists = list()
    for row in train_set:
        dist = euclidean_dist(test_row, row)
        dists.append((row, dist))
    dists.sort(key=get_dist)

    # Add distances to neighbour list
    neighbours = list()
    for i in range(neighbour_count):
        neighbours.append(dists[i][0])
    return neighbours


def classify(training_set, test_row, neighbour_count):
    neighbours = get_neighbours(training_set, test_row, neighbour_count)
    results = [row[-1] for row in neighbours]  # Get last element of each row
    return max(set(results), key=results.count)


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


prediction = classify(test_dataset, test_dataset[0], 3)
print('Expected %d, Got %d.' % (test_dataset[0][-1], prediction))
