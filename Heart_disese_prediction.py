# Description : classifies a person having heart disease or not
import numpy as np
import pandas as pd
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

df = pd.read_csv('Hrt_ds.csv')
df.dropna(axis=0 , inplace= True)

# create a years column
df['years'] = (df['age']).round()
df['years'] = pd.to_numeric(df['years'] , downcast= 'integer')

# sb.countplot(x= 'age' , hue= 'TenYearCHD' , data= df , palette= 'colorblind' , egdecolor= sb.color_palette('dark' , n_colors= 1))
plt.figure(figsize= (7,7))
sb.heatmap(df.corr() , annot= True , fmt= '.0%')
# plt.show()

# split the data into feature data and target data
X = df.iloc[: , :-1].values
y = df.iloc[: ,-1].values

# split the data
X_train , X_test , y_train , y_test = train_test_split(X , y , test_size= 0.25 , random_state= 42)

# scale the data
sc = StandardScaler()
X_train = sc.fit_transform(X_train) 
X_test = sc.transform(X_test)

# Use the random forest classifier
forest = RandomForestClassifier(n_estimators= 50 , criterion= 'entropy' , random_state= 42)
forest.fit(X_train , y_train)

# Test the model accuracy
model = forest
y_pred = model.predict(X_test)
cf = confusion_matrix(y_test , y_pred)
print(cf)