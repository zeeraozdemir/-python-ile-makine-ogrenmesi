import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler = pd.read_csv("C:/Users/ZEHRA\Desktop/python-ile-makine-ogrenmesi/python-ile-makine-ogrenmesi/2.bölüm/veriler.csv")

boy = veriler[['boy']]
print(boy)
boykilo = veriler[['boy','kilo']]
print(boykilo)

