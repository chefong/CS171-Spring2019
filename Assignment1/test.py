import numpy as np
import pandas as pd
import random as rand

data_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'label']
data = pd.read_csv('iris.data', 
                   names = data_names)

boxplot = data.boxplot(column=data_names[0:4])
print(boxplot)