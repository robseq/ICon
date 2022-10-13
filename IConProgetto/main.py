# PROGETTO DI INGEGNERIA DELLA CONOSCENZA
# Antonio Sequenza, Ruggiero Zagaria

# Importa le librerie necessarie
import pandas as pd
import DataHandler, RandomForest, KNN, SVM

if __name__ == '__main__':
    # Classificazione binaria (1° test)
    # --------------------------------------------------
    # Visualizza il dataset e le sue informazioni
    data = pd.read_csv("ObesityDataSet.csv", sep=";", header=0, index_col=False)
    print(data)
    print(data.info())
    print(data.describe())

    # Modifica il dataset e visualizza le informazioni
    data = DataHandler.dataHandler1(data)
    # Effettua lo split in train e test
    X_train, X_test, y_train, y_test, X, y = DataHandler.splitDataset(data)

    # Classificazione binaria
    RandomForest.randForest(X_train, X_test, y_train, y_test, X, y)
    KNN.knn(X_train, X_test, y_train, y_test, X, y)
    SVM.svm(X_train, X_test, y_train, y_test, X, y)

    # Classificazione binaria (2° test)
    # --------------------------------------------------
    # Visualizza il dataset e le sue informazioni
    # data1 = pd.read_csv("ObesityDataSet.csv", sep=";", header=0, index_col=False)
    # print(data1)
    #
    # # Modifica il dataset e visualizza le informazioni
    # data1 = DataHandler.dataHandler2(data1)
    # # Effettua lo split in train e test
    # X_train2, X_test2, y_train2, y_test2, X2, y2 = DataHandler.splitDataset1(data1)
    #
    # # # Classificazione binaria
    # RandomForest.randForest2(X_train2, X_test2, y_train2, y_test2, X2, y2)
    # KNN.knn2(X_train2, X_test2, y_train2, y_test2, X2, y2)
    # SVM.svm2(X_train2, X_test2, y_train2, y_test2, X2, y2)




