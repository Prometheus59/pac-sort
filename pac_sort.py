from math import sqrt
from random import seed
from random import randrange
from csv import reader


def import_data(file):
    # File must in CSV (MS-DOS) format
    data = list()
    with open(file, 'r') as file:
        excel_data = reader(file)
        for x in excel_data:
            if not x:
                continue
            else:
                data.append(x)
    return data


def make_folds(dataset, fold_count):
    data_folds = list()
    data_dup = list(dataset)
    fold_size = int(len(dataset) / fold_count)
    for _ in range(fold_count):
        fold = list()
        while len(fold) < fold_size:
            data_length = len(data_dup)
            remove = randrange(data_length)
            fold.append(data_dup.pop(remove))
        data_folds.append(fold)
    return data_folds


def precision_test(guess, real):
    valid = 0
    length = len(real)
    for x in range(length):
        if (guess[x] == real[x]):
            valid += 1
    return valid / float(len(real)) * 100.0


def validate(dataset, fold_count, neighbour_count):
    # store rankings
    ranks = list()
    # Split into folds
    folds = make_folds(dataset, fold_count)
    for fold in folds:
        test_set = list()
        training_set = list(folds)
        training_set.remove(fold)
        # Get sum of all items in training set
        training_set = sum(training_set, [])
        for x in fold:
            x_dup = list(x)
            x_dup[-1] = None
            test_set.append(x_dup)
        estimate = knn(training_set, test_set, neighbour_count)
        real = [element[-1] for element in fold]
        # Truncate precision result to 3 decimal places
        precision = float('%.3f' % (precision_test(estimate, real)))
        ranks.append(precision)
    return ranks


def euclidean_dist(vector1, vector2):
    size = len(vector1)-1   # Ignore output value in csv file
    dist = 0
    for x in range(size):   # Extend for all kinds of feature vectors
        dist += (vector1[x] - vector2[x])**2
    return sqrt(dist)


# return first element of tuple
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

# prediction = classify(test_dataset, test_dataset[0], 3)
# print('Expected %d, Got %d.' % (test_dataset[0][-1], prediction))


def knn(train_set, test_set, neighbour_count):
    results = list()
    for item in test_set:
        result = classify(train_set, item, neighbour_count)
        results.append(result)
    return(results)


# Converts each element of the data array to
#   a floating point number
def str_to_fp(data, str_col):
    for x in data:
        element = x[str_col].strip()
        x[str_col] = float(element)


def make_prediction(training_set, testing_row, neighbour_count):
    neighbours = get_neighbours(training_set, testing_row, neighbour_count)
    results = [result[-1] for result in neighbours]
    # Return result with the highest count
    return max(set(results), key=results.count)


# Driver Code
# Evaluate accuracy of knn algorithm implementation
seed(1)
# Import Dataset Here
filename = 'boolean.csv'
dataset = import_data(filename)
for i in range(len(dataset[0])-1):
    str_to_fp(dataset, i)
# # convert class column to integers
# str_column_to_int(dataset, len(dataset[0])-1)
# # evaluate algorithm
fold_count = 5
neighbour_count = 5
rankings = validate(
    dataset, fold_count, neighbour_count)
print('\nResults for k-fold cross validation (5 folds): ')

for index, rank in enumerate(rankings):
    print('Fold %d: %s%%' % (index+1, rank))
print('\nMean Accuracy (Avg. Error over all folds): %.3f %%' %
      (sum(rankings)/float(len(rankings))))


# New prediction
new_data = [1, 1, 0]
result = make_prediction(dataset, new_data, neighbour_count)
print("The prediction for " + str(new_data) + " is " + result)
