import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

eksik_veriler = pd.read_csv("C:/Users/ZEHRA\Desktop/python-ile-makine-ogrenmesi/python-ile-makine-ogrenmesi/2.bölüm/eksikveriler.csv")

boy = eksik_veriler[['boy']]
print(boy)
boykilo = eksik_veriler[['boy','kilo']]
print(boykilo)
print(eksik_veriler)