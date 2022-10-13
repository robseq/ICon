import pickle
import Interface as int
import warnings
warnings.filterwarnings('ignore')


def interface():
    print("Benvenuto/a! Ti dirò a quale livello di peso appartieni in base al tuo stile di vita.")
    print("Inoltre, ti restituirò il BMI associato!")
    model = open("SVM_model.pkl", "rb")
    model = pickle.load(model)
    print("Inserisci i seguenti valori: ")
    print("-------------------------------------------------------------------------------------")
    Gender = float(input("Inserisci il sesso: (1.Femmina 0.Maschio) "))
    Age = float(input("Inserisci l'età: "))
    Height = float(input("Inserisci l'altezza: "))
    Weight = float(input("Inserisci il peso: "))
    Family_overweight = float(input("Hai familiari obesi o che lo sono stati? (0.No 1.Yes ) "))
    Freq_consume_cal = float(input("Mangi spesso cibi molto calorici? (0.No 1.Si) "))
    Freq_consume_veg = float(input("Ogni quanto mangi vegetali? (1.Sempre 2.A volte 3.Raramente) "))
    N_daily_meals = float(input("Inserisci il numero di pasti quotidiani: (0.Tra 1 e 2 1.Tre 2.Più di tre) "))
    Smoke = float(input("Fumi? (0.No 1.Si) "))
    Daily_water = float(input("Quanta acqua bevi giornalmente? "
                              "(1.Meno di un litro 2.Tra uno e due litri 3.Più di due litri) "))
    Consume_b_meals = float(input("Quanto spesso mangi tra i pasti principali? "
                                  "(1.Sempre 2.Frequentemente 3.A volte 4.Raramente) "))
    Count_daily_cal = float(input("Conti le calorie che consumi durante il giorno? (0.No 1.Si) "))
    Freq_daily_activity = float(input("Quanto attività fisica svolgi settimanalmente? "
                                "(1.Da 1 a 2 giorni 2.Da 3 a 4 giorni 3.Da 5 a 6 giorni 4.Nessuna attività fisica) "))
    Freq_screen_time = float(input("Quanto tempo passi sui dispositivi elettronici? "
                                   "(0.Da 0 a 2 ore 1.Da 3 a 5 ore 2.Più di 5 ore) "))
    Consume_alcohol = float(input("Bevi alcohol? (1.Non consumo 2.Raramente 3.Settimanalmente 4.Giornalmente) "))
    Transportation = float(input("Quale mezzo di trasporto usi per spostarti? "
                                 "(0.Automobile 1.Motorbike 2.Bici 3.Mezzo pubblico 4.A piedi) "))

    def resultbmi():
        bmi = Weight / (Height * Height)
        if bmi <= 18.5:
            print("Sei sottopeso")
            print("BMI: ", bmi)
        elif (bmi >= 18.5) and (bmi <= 24.9):
            print("Sei normopeso")
            print("BMI: ", bmi)
        elif (bmi >= 25) and (bmi <= 29.9):
            print("Sei sovrappeso")
            print("BMI: ", bmi)
        elif (bmi >= 30) and (bmi <= 34.9):
            print("Sei obeso di tipo 1")
            print("BMI: ", bmi)
        elif (bmi >= 35) and (bmi <= 39.9):
            print("Sei obeso di tipo 2")
            print("BMI: ", bmi)
        elif bmi >= 40:
            print("Sei obeso di tipo 3")
            print("BMI: ", bmi)

    values = [[Gender, Age, Height, Weight, Family_overweight, Freq_consume_cal, Freq_consume_veg, N_daily_meals,
               Smoke, Daily_water, Consume_b_meals, Count_daily_cal, Freq_daily_activity,
               Freq_screen_time, Consume_alcohol, Transportation]]
    prediction = model.predict(values)

    if prediction == 1:
        print("Livello di obesità: obeso")
        resultbmi()
        print("--------------------------------")
        return 0
    elif prediction == 0:
        print("Livello di obesità: non obeso")
        resultbmi()
        print("--------------------------------")
        return 0


# Inizio
int.interface()


