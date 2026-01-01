from storage.formulae import mean, std_dev, variance, covariance, correlation_coefficient, findX, findY, bxy, byx

from storage.manager import storer

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
        
def validity_checker(X, Y):
    r = correlation_coefficient(X, Y) #correlation coefficient(r)
    validity = 100
    n = len(X)

    #For |r|:
    r = abs(r) #abs for absolute value

    distance_from_r = 1-r

    #For distance outside observed range
    if n not in [min(X), max(X)]:
        distance_from_range = min(X) - n if n < min(X) else n - max(X)
    
    #For data sufficiency


def train_model(X, Y):
    n = len(X)
    xmean = mean(X)
    ymean = mean(Y)
    Bxy = bxy(X, Y)
    Byx = byx(X, Y)
    r = correlation_coefficient(X, Y)
    Variance = variance(X)
    Covariance = covariance(X, Y)

    return {
    "n": n,
    "xmean": xmean,
    "ymean": ymean,
    "bxy": Bxy,
    "byx": Byx,
    "r": r,
    "variance": Variance,
    "covariance": Covariance
    }

def predict_x(model, y_value):
    return model["xmean"] + model["bxy"] * (y_value - model["ymean"])