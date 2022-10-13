# VALUTAZIONI MODELLI
# Importa le librerie necessarie
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import precision_recall_curve, confusion_matrix


def evaMod(X_train, X_test, y_train, y_test, clf, y_test_pred, name):
    print(name + ':')
    print("---------------------------------------------------------------")
    # Accuracy score
    print(f'Accuracy train : {clf.score(X_train, y_train):.3f}')
    print(f'Accuracy test  : {clf.score(X_test, y_test):.3f}')
    # Classification report
    print("\nClassification Report:\n", metrics.classification_report(y_test, y_test_pred))
    # Confusion matrix
    print(sns.heatmap(confusion_matrix(y_test, y_test_pred), annot=True, fmt='.4g',
                      xticklabels=['Not obese', 'Obese'],
                      yticklabels=['Not obese', 'Obese'],
                      cbar=False, cmap='Blues'))
    plt.show()
    # Mostra la curva del precision-recall
    precision, recall, thresholds = precision_recall_curve(y_test, y_test_pred)
    plt.plot(recall, precision)
    plt.title("Precision-recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.show()
    print("---------------------------------------------------------------\n")


def evaMod2(X_train2, X_test2, y_train2, y_test2, clf, y_test_pred, name):
    print(name + ':')
    print("---------------------------------------------------------------")
    # Accuracy score
    print(f'Accuracy train : {clf.score(X_train2, y_train2):.3f}')
    print(f'Accuracy test  : {clf.score(X_test2, y_test2):.3f}')
    # Classification report
    print("\nClassification Report:\n", metrics.classification_report(y_test2, y_test_pred))
    # Confusion matrix
    print(sns.heatmap(confusion_matrix(y_test2, y_test_pred), annot=True, fmt='.4g',
                      xticklabels=['Not obese', 'Obese'],
                      yticklabels=['Not obese', 'Obese'],
                      cbar=False, cmap='Blues'))
    plt.show()
    # Mostra la curva del precision-recall
    precision, recall, thresholds = precision_recall_curve(y_test2, y_test_pred)
    plt.plot(recall, precision)
    plt.title("Precision-recall Curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.show()
    print("---------------------------------------------------------------\n")







