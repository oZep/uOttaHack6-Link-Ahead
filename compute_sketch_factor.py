import math
import feature_extraction
import pandas as pd

alpha = 0.2 # Spread of the tanh range
tmp = pd.read_csv("stats.csv").reset_index().values.tolist()
mean_features = {} # arrrgh >:[  he mean

for a, b, c, d in tmp:
    mean_features[b] = [c, d]

def compute_coefficient_deviation(mean, sigma, value):
    # Because the dataset is limited, we'll have to have a special exception for very low variances
    if sigma == 0:
        return  (1/(sigma+0.1)) * (mean - value) ** 2
    else:
        return  (1/sigma) * (mean - value) ** 2


def compute_sketch_factor(url):
    extractions = []
    features = feature_extraction.feature_extract_url(url)

    for i in features:
        if i not in mean_features:
            #print("Skipping feature: " + i)
            continue

        a, b =  mean_features[i]
        extractions.append(compute_coefficient_deviation(features[i], a, b))

    return math.tanh(alpha*sum(extractions)/len(extractions))
