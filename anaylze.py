import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('./dataset_cybersecurity_michelle.csv')
df_new = df[df['phishing'] == 1]

def getInfo(): 
    data = {}
    for key in df_new.keys():
        pair = []
        mean = df_new[key].sum() / len(show)
        sd = df_new[key].std()
        pair.append(mean)
        pair.append(sd)
        data[key] = pair
    return data