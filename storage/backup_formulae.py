#Default values finder
def values_finder(X, Y):
    if len(X) != len(Y):
        return "Lengths are not equal!"

    N = len(X)
    EX = EY = EX2 = EY2 = EXY = 0

    for (x,y) in zip(X,Y):
        EX += x
        EY += y
        EX2 += x**2
        EY2 += y**2
        EXY += x*y

    return N, EX, EY, EX2, EY2, EXY


#Mean:
def mean(X):
    EX = 0
    N = len(X)

    for x in X:
        EX += x

    return EX/N

#Standard Deviation:
def std_dev(X):
    N = len(X)
    Mean = mean(X)
    EX2 = 0

    for x2 in X:
        EX2 += x2**2

    return ( (EX2/N) - (Mean)**2 )**0.5
    
#Variance:
def variance(X):
    return (std_dev(X))**2

#Covariance:
def covariance(X, Y):
    return ( correlation_coefficient(X, Y) * std_dev(X) * std_dev(Y) )

#Correlation:
'''
Relationship between 2 or more than 2 variables.
'''
'''
Methods for finding correlation:

1) Karl Pearson's correlation coefficient(r):

'''

def correlation_coefficient(X, Y):
    N, EX, EY, EX2, EY2, EXY = values_finder(X, Y)

    return (N*EXY - EX*EY) / ( (N*EX2 - (EX)**2)**0.5 ) * ( (N*EY2 - (EY)**2)**0.5 )

def r_via_r_coefficients(X, Y):
    Bxy = bxy(X, Y)
    Byx = bxy(X, Y)

    r = ( Bxy*Byx )**0.5
    return r if r>0 else -r

#Regression:
'''
Prediction of one variable when another variable is given.
'''
'''
Regression Equation:
'''

def bxy(X, Y):
    N, EX, EY, EX2, EY2, EXY = values_finder(X, Y)

    return ( N*EXY - EX*EY ) / ( N*EY2 - (EY)**2 )

def byx(X, Y):
    N, EX, EY, EX2, EY2, EXY = values_finder(X, Y)

    return ( N*EXY - EX*EY ) / ( N*EX2 - (EX)**2 )

def findX(Y, xmean, ymean, bxy):
    return xmean + bxy * (Y - ymean)

def findY(X, xmean, ymean, byx):
    return xmean + byx * (X - ymean)