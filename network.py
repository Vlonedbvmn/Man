import pandas as pd
import numpy as np

dataset = pd.read_excel('Завантажте свій датасет, зараз представлено excel', sheet_name='xxx')

# Опрацьовування датасету
print(dataset.isnull().sum())
dataset.dropna(inplace=True)
print(dataset.isnull().sum())

x = dataset.iloc[:,0:-1].values

print(x)
y= dataset.iloc[:, -1].values

print(y)

# Поділ даних на тестову та тренувальні вибірки
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
x= np.array(x)

print(x)

le = LabelEncoder()
y = le.fit_transform(y)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train)
print(x_test)
print(y_train)
print(y_test)


#Створення нейромережі та збереження
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(x_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(len(np.unique(y)), activation='softmax')
])

history = model.compile(optimizer=Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

import matplotlib.pyplot as plt
loss, accuracy = model.evaluate(x_test, y_test)

print(f"Точність: {accuracy * 100:.2f}%")
plt.plot(history.history['loss'])
plt.grid(True)
plt.show()
model.save('Збережіть модель куди потрібно')
