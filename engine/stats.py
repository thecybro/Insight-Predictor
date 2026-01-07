import pandas as pd

from storage.formulae import mean, std_dev, variance, covariance, correlation_coefficient
from storage.formulae import findX, findY, bxy, byx

file = "data/sample.csv"
file2 = "data/outputs.csv"
file3 = "storage/changes.csv"
file4 = "storage/getaway.csv"

def mean_displayer(X):
    return mean(X)

def std_dev_displayer(X):
    return std_dev(X)

def variance_displayer(X):
    return variance(X)

def covariance_displayer(X, Y):
    return covariance(X, Y)

def correlation_coefficient_displayer(X, Y):
    return correlation_coefficient(X, Y)

def Xfinder(X, Y, y):
    return findX(X, Y, y)

def Yfinder(X, Y, x):
    return findY(X, Y, x)

def interpreter(r):
        if r == -1:
            return "Perfect negative correlation"
        
        elif -1<r<-0.3:
            return "Weak negative correlation"
        
        elif -0.3<r<-0.5:
            return "Weak-moderate negative correlation"
        
        elif -0.5<r<-0.7:
            return "Moderate negative correlation"
        
        elif -0.7<r<-0:
            return "Strong negative correlation"
        
        elif 0:
            return "No correlation"
        
        elif 0<r<0.3:
            return "Weak positive correlation"
        
        elif 0.3<r<0.5:
            return "Weak-moderate positive correlation"
        
        elif 0.5<r<0.7:
            return "Moderate positive correlation"
        
        elif 0.7<r<1:
            return "Strong positive correlation"
        
        elif r == 1:
            return "Perfect positive correlation"
        
def validity_checker(X, Y, predict_value=None):
    r = abs(correlation_coefficient(X, Y)) #correlation coefficient(r)
    current_n = len(X)
    converged_n = None
    converged_case = None
    threshold = 0.005
    k = 5 #Stability window

    if r == 0:
        return {"validity": "0%"}
    
    #Initial validity based on correlation
    validity = 100*r

    #For distance outside observed range (extrapolation)
    if predict_value not in [min(Y), max(Y)]:
        if predict_value < min(Y):
            distance_from_range = abs(predict_value - min(Y))

        elif predict_value > max(Y):
            distance_from_range = predict_value - max(Y)

        else:
            distance_from_range = 0

        if distance_from_range > 0:
            penalty = 1 + distance_from_range / max(Y)
            validity /= penalty

        '''
        Example if the validity is 90%, and predict_value is 116,
        validity = 90 / (1 + (116-58)/58)
        = 90/2
        = 45%
        ''' #Couldn't find a reliable formula, so made one up.

        
    #For data sufficiency
    df = pd.read_csv(file3)  #changes.csv
    total_n = len(df) + 5 #Cuz starting form 6
    i = 0

    for result in df["result"].values.tolist():
        if result < threshold:
            i += 1

        else:
            i = 0
        
    if i >= k:
        converged_case = True
        converged_n = total_n - i

    else:
        converged_case = False
        converged_n = None
        
    if converged_case == False:
        validity *= 0.7

        
    #After finishing all
    return {
        "validity": f"{validity:.2f}%",
        "r": r,
        "converged": converged_case,
        "current n": current_n,
        "converged n": converged_n if converged_n else "N/A"
        }


def train_model(X, Y):
    n = len(X)
    xmean = mean(X)
    ymean = mean(Y)
    Bxy = bxy(X, Y)
    Byx = byx(X, Y)
    r = correlation_coefficient(X, Y)
    XVariance = variance(X)
    YVariance = variance(Y)
    Covariance = covariance(X, Y)

    return {
    "n": n,
    "xmean": xmean,
    "ymean": ymean,
    "bxy": Bxy,
    "byx": Byx,
    "r": r,
    "xvariance": XVariance,
    "yvariance": YVariance,
    "covariance": Covariance
    }

def predict_x(model, y_value):
    return model["xmean"] + model["bxy"] * (y_value - model["ymean"])