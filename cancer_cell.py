from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score
import pandas as pd
import matplotlib.pyplot as plt

data = load_breast_cancer()

df = pd.DataFrame(data= data.data ,columns= data.feature_names) #normal data
df.sample(5)

df2 = pd.DataFrame(data= data.target , columns= ['target']) #target data
df2.sample(5)

class_counts = df2['target'].value_counts()
plt.pie(class_counts , labels= class_counts.index , autopct= '%1.2f%%' , colors= [ 'red' , 'green'])

# split the dataset
x_train , x_test , y_train , y_test = train_test_split(data.data , data.target , test_size= 0.33 , random_state= 42)
model = GaussianNB()
model.fit(x_train , y_train)

y_pred = model.predict(x_test)

print(y_pred)
accuracy = accuracy_score(y_test , y_pred)
print(f" Model Accuracy: {accuracy * 100: .2f}%")
