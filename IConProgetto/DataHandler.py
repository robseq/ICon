# DATASET HANDLER
# Importa le librerie necessarie
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def dataHandler1(data):
    # Verifica se esistono valori nulli all'interno del dataset
    print(data.isna().any())

    # Rinomina alcune colonne
    data.rename(columns={"family_history_with_overweight": "Family_overweight", "FAVC": "Freq_consume_cal",
                         "FCVC": "Freq_consume_veg", "NCP" : "N_daily_meals", "CAEC" : "Consume_b_meals",
                         "SMOKE": "Smoke", "CH2O": "Daily_water", "SCC": "Count_daily_cal",
                         "FAF": "Freq_daily_activity", "TUE": "Freq_screen_time", "MTRANS": "Transportation",
                         "CALC": "Consume_alcohol", "NObeyesdad": "ObesityLevel"}, inplace=True)

    # Converte tutte le features in valori numerici
    data["Gender"] = data["Gender"].apply(lambda x: 1 if x == "Female" else 0)
    data["Age"] = data["Age"].apply(lambda x: int(float(int(x * 100)) / 100))
    data["Height"] = data["Height"].apply(lambda x: round(x, 2))
    data["Weight"] = data["Weight"].apply(lambda x: round(x, 1))
    data["Family_overweight"] = data["Family_overweight"].apply(lambda x: 1 if x == "yes" else 0)
    data["Freq_consume_cal"] = data["Freq_consume_cal"].apply(lambda x: 1 if x == "yes" else 0)
    data["Freq_consume_veg"] = data["Freq_consume_veg"].apply(lambda x: int(round(x, 0)))
    data["N_daily_meals"] = data["N_daily_meals"].apply(lambda x: int(round(x, 0)))
    data["Consume_b_meals"], unique_CAEC = pd.factorize(data["Consume_b_meals"], sort=True)
    data["Smoke"] = data["Smoke"].apply(lambda x: 1 if x == "yes" else 0)
    data["Daily_water"] = data["Daily_water"].apply(lambda x: int(round(x, 0)))
    data["Count_daily_cal"] = data["Count_daily_cal"].apply(lambda x: 1 if x == "yes" else 0)
    data["Freq_daily_activity"] = data["Freq_daily_activity"].apply(lambda x: int(round(x, 0)))
    data["Freq_screen_time"] = data["Freq_screen_time"].apply(lambda x: int(round(x, 0)))
    data["Consume_alcohol"], unique_CALC = pd.factorize(data["Consume_alcohol"], sort=True)
    transportation = {"Automobile": 1, "Bike": 2, "Motorbike": 3, "Public_Transportation": 4, "Walking": 5}
    data["Transportation"] = data["Transportation"].map(transportation, na_action='ignore').apply(lambda x: int(x))
    obesity_level = {"Insufficient_Weight": 0, "Normal_Weight": 0, "Overweight_Level_I": 0, "Overweight_Level_II": 0,
                     "Obesity_Type_I": 1, "Obesity_Type_II": 1, "Obesity_Type_III": 1}
    data["ObesityLevel"] = data["ObesityLevel"].map(obesity_level, na_action='ignore').apply(lambda x: int(x))
    print(data)

    # Proporzione classe target
    from collections import Counter
    plt.pie(Counter(data['ObesityLevel']).values(), labels=["Obeso", "Non obeso"], autopct='%1.1f%%', startangle=-60,
            shadow=True)
    plt.title('Proporzione obesità')
    plt.show()

    return data


def dataHandler2(data1):
    # Rinomina alcune colonne
    data1.rename(columns={"family_history_with_overweight" : "Family_overweight", "FAVC": "Freq_consume_cal",
                         "FCVC" : "Freq_consume_veg", "NCP" : "N_daily_meals", "CAEC" : "Consume_b_meals",
                         "SMOKE" : "Smoke", "CH2O" : "Daily_water", "SCC" : "Count_daily_cal",
                         "FAF" : "Freq_daily_activity", "TUE" : "Freq_screen_time", "MTRANS" : "Transportation",
                         "CALC" : "Consume_alcohol", "NObeyesdad" :"ObesityLevel"}, inplace=True)

    # Converte tutte le features in valori numerici
    data1["Gender"] = data1["Gender"].apply(lambda x: 1 if x == "Female" else 0)
    data1["Age"] = data1["Age"].apply(lambda x: int(float(int(x * 100)) / 100))
    data1["Height"] = data1["Height"].apply(lambda x: round(x, 2))
    data1["Weight"] = data1["Weight"].apply(lambda x: round(x, 1))
    data1["Family_overweight"] = data1["Family_overweight"].apply(lambda x: 1 if x == "yes" else 0)
    data1["Freq_consume_cal"] = data1["Freq_consume_cal"].apply(lambda x: 1 if x == "yes" else 0)
    data1["Freq_consume_veg"] = data1["Freq_consume_veg"].apply(lambda x: int(round(x, 0)))
    data1["N_daily_meals"] = data1["N_daily_meals"].apply(lambda x: int(round(x, 0)))
    data1["Consume_b_meals"], unique_CAEC = pd.factorize(data1["Consume_b_meals"], sort=True)
    data1["Smoke"] = data1["Smoke"].apply(lambda x: 1 if x == "yes" else 0)
    data1["Daily_water"] = data1["Daily_water"].apply(lambda x: int(round(x, 0)))
    data1["Count_daily_cal"] = data1["Count_daily_cal"].apply(lambda x: 1 if x == "yes" else 0)
    data1["Freq_daily_activity"] = data1["Freq_daily_activity"].apply(lambda x: int(round(x, 0)))
    data1["Freq_screen_time"] = data1["Freq_screen_time"].apply(lambda x: int(round(x, 0)))
    data1["Consume_alcohol"], unique_CALC = pd.factorize(data1["Consume_alcohol"], sort=True)
    transportation = {"Automobile": 1, "Bike": 2, "Motorbike": 3, "Public_Transportation": 4, "Walking": 5}
    data1["Transportation"] = data1["Transportation"].map(transportation, na_action='ignore').apply(lambda x: int(x))
    obesity_level = {"Insufficient_Weight": 0, "Normal_Weight": 0, "Overweight_Level_I": 0, "Overweight_Level_II": 0,
                     "Obesity_Type_I": 1, "Obesity_Type_II": 1, "Obesity_Type_III": 1}
    data1["ObesityLevel"] = data1["ObesityLevel"].map(obesity_level, na_action='ignore').apply(lambda x: int(x))

    return data1


def splitDataset(data):
    # Effettua lo split in train e test set
    X = data.drop(['ObesityLevel'], axis=1)
    y = data['ObesityLevel']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    return X_train, X_test, y_train, y_test, X, y


def splitDataset1(data1):
    # Effettua lo split in train e test set
    X2 = data1.drop(['ObesityLevel'], axis=1)
    y2 = data1['ObesityLevel']
    X_train2, X_test2, y_train2, y_test2 = train_test_split(X2, y2, test_size=0.40, random_state=42)

    return X_train2, X_test2, y_train2, y_test2, X2, y2

