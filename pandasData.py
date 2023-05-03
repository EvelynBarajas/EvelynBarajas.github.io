import pandas as pd
import numpy as np

csv_link= 'iris.csv'
iris= pd.read_csv(csv_link, header= None)
print(iris)

col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Species']
iris =  pd.read_csv(csv_link, names = col_names)
print(iris)

#new columns, petal_ratio and sepal_ratio
iris["petal_ratio"]= iris["Petal_Length"]/iris["Petal_Width"]
iris["sepal_ratio"]= iris["Sepal_Length"]/iris["Sepal_Width"]
print(iris)

df = pd.DataFrame(iris)
df.to_csv('Desktop\Python2\datsci\export_iris.csv', index=False, header=True)
print(df)

df.median()
df.min()
df.max()
df.std()

import matplotlib.pyplot as plt

transposed_iris= iris.transpose()
labels= list(iris.columns)
ticks= range(1, len(iris.columns)+1)
plt.boxplot(transposed_iris)
plt.xticks(ticks, labels)


