import pandas as pd

from engine.stats import mean_displayer, std_dev_displayer, variance_displayer
from engine.stats import covariance_displayer, correlation_coefficient_displayer
from engine.stats import Xfinder, Yfinder
from engine.stats import interpreter, validity_checker

from engine.stats import train_model, predict_x

from data.manager import data_manager, storer

from storage.formulae import bxy, byx
from storage.manager import calculator

file = "data/sample.csv"
file2 = "storage/changes.csv"

df = pd.read_csv(file)

X = df["X"].values.tolist()
Y = df["Y"].values.tolist()

prediction_validity = validity_checker(X, Y, 59)

print(prediction_validity)