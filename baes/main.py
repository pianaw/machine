import numpy as np
import pandas as pd

if __name__ == '__main__':
    symptoms = pd.read_csv('symptom.csv', delimiter=";")
    symptoms_stats = []
    symptoms_num = symptoms.shape[0]
    for i in range(symptoms_num):
        symptoms_stats.append(np.random.randint(0, 2))
    print(symptoms_stats)
    diseases = pd.read_csv('disease.csv', delimiter=";")
    prob_diseases = []
    for i in range(diseases.shape[0] - 1):
        prob_diseases.append(diseases.iloc[i][-1] / diseases.iloc[-1][-1])
    print(prob_diseases)
    prob_max = 0
    index_max = 0
    for i in range(len(prob_diseases)):
        proba = 1
        for j in range(len(symptoms_stats)):
            if symptoms_stats[j] == 1:
                proba *= symptoms.iloc[j][i + 1]
        proba *= prob_diseases[i]
        if proba > prob_max:
            prob_max = proba
            index_max = i
    print(diseases.iloc[index_max][0])