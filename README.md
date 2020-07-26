# pac-sort

Supervised learning - Data classification algorithm to classify various Pac-Man related websites

## TESTING

### **Keywords feature vector**

### 18 Items for input to KNN algorithm:

```
Results for k-fold cross validation (5 folds):
Fold 0: 100.0
Fold 1: 100.0
Fold 2: 66.667
Fold 3: 100.0
Fold 4: 33.333

Mean Accuracy (Avg. Error over all folds): 80.000 %
```

### 40 Items for input to KNN algorithm:

```
Results for k-fold cross validation (5 folds):
Fold 0: 75.0
Fold 1: 100.0
Fold 2: 87.5
Fold 3: 100.0
Fold 4: 87.5

Mean Accuracy (Avg. Error over all folds): 90.000 %
```

### 73 Items for input to KNN algorithm:

```
Results for k-fold cross validation (5 folds):
Fold 0: 92.857
Fold 1: 100.0
Fold 2: 100.0
Fold 3: 92.857
Fold 4: 100.0

Mean Accuracy (Avg. Error over all folds): 97.143 %
```

### **Boolean Feature Vector**

### 20 Items for input to KNN algorithm

```
Results for k-fold cross validation (5 folds):
Fold 1: 50.0%
Fold 2: 100.0%
Fold 3: 100.0%
Fold 4: 50.0%
Fold 5: 75.0%

Mean Accuracy (Avg. Error over all folds): 75.000 %
The prediction for [1, 1, 0] is Pac-Man
```

### 40 Items for input to KNN algorithm

```
Results for k-fold cross validation (5 folds):
Fold 1: 87.5%
Fold 2: 75.0%
Fold 3: 75.0%
Fold 4: 100.0%
Fold 5: 62.5%

Mean Accuracy (Avg. Error over all folds): 80.000 %
```

### 73 Items for input to KNN algorithm

```
Results for k-fold cross validation (5 folds):
Fold 1: 92.857%
Fold 2: 64.286%
Fold 3: 71.429%
Fold 4: 85.714%
Fold 5: 71.429%

Mean Accuracy (Avg. Error over all folds): 77.143 %
```

## Interpretation of results

As the number of items used in the training set is increased, the mean accuracy of the algorithm also increases.
