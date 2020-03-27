import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from b_back_pro.g_stats_tb.lin_reg.logistic_regression import LogisticRegression


class AccuracyCalculation:

    def __init__(dataset):
        dataset = datasets.load_breast_cancer()
        bc = dataset
        X, y = bc.data, bc.target

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

        regressor = LogisticRegression(learning_rate=0.0001, n_iters=1000)
        regressor.fit(X_train, y_train)
        predictions = regressor.predict(X_test)

        print("LR classification accuracy:", accuracy(y_test, predictions))

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy
