# RANDOM FOREST
# Importa le librerie necessarie
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import EvaluateModel as eva


def randForest(X_train, X_test, y_train, y_test, X, y):

    name = "RANDOM FOREST"
    # Crea il modello Random Forest
    clf = RandomForestClassifier(n_estimators=5, max_depth=2, random_state=0)
    # Addestra il classificatore sui dati di training
    clf.fit(X_train, y_train)
    # Effettua la predizione sui dati di training
    y_test_pred = clf.predict(X_test)

    eva.evaMod(X_train, X_test, y_train, y_test, clf, y_test_pred, name)

    # GridSearchCV
    parameters = {'n_estimators': (2, 3, 4, 5, 10, 100),
                  'max_depth': (1, 2, 3, 4, 5)
                  }
    clf2 = GridSearchCV(estimator=clf, param_grid=parameters, cv=10, n_jobs=-1)
    clf2.fit(X, y)
    # Risultati GridSearchCV
    means = clf2.cv_results_['mean_test_score']
    stds = clf2.cv_results_['std_test_score']
    params = clf2.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("Accuracy: %f (Standard deviation: %f) using: %r" % (mean, stdev, param))
    # Stampa i migliori Iperparametri
    print("\nBest mean score (with cv): %f (Standard deviation: %f) using %s" % (clf2.best_score_, np.mean(stdev), clf2.best_params_))
    print("Train-set score            : {:.3f}".format(clf2.score(X_train, y_train)))
    print("Test-set score             : {:.3f}".format(clf2.score(X_test, y_test)))


def randForest2(X_train2, X_test2, y_train2, y_test2, X2, y2):

    name = "RANDOM FOREST"
    # Crea il modello Random Forest
    clf = RandomForestClassifier(n_estimators=5, max_depth=2, random_state=0)
    # Addestra il classificatore sui dati di training
    clf.fit(X_train2, y_train2)
    # Effettua la predizione sui dati di training
    y_test_pred = clf.predict(X_test2)

    eva.evaMod2(X_train2, X_test2, y_train2, y_test2, clf, y_test_pred, name)

    # GridSearchCV
    parameters = {'n_estimators': (2, 3, 4, 5, 10, 100),
                  'max_depth': (1, 2, 3, 4, 5)
                  }
    clf2 = GridSearchCV(estimator=clf, param_grid=parameters, cv=10, n_jobs=-1)
    clf2.fit(X2, y2)
    # Risultati GridSearchCV
    means = clf2.cv_results_['mean_test_score']
    stds = clf2.cv_results_['std_test_score']
    params = clf2.cv_results_['params']
    for mean, stdev, param in zip(means, stds, params):
        print("Accuracy: %f (Standard deviation: %f) using: %r" % (mean, stdev, param))
    # Stampa i migliori Iperparametri
    print("\nBest mean score (with cv): %f (Standard deviation: %f) using %s" % (clf2.best_score_, np.mean(stdev), clf2.best_params_))
    print("Train-set score            : {:.3f}".format(clf2.score(X_train2, y_train2)))
    print("Test-set score             : {:.3f}".format(clf2.score(X_test2, y_test2)))




