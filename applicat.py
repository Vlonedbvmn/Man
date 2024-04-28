import tensorflow as tf
import numpy as np
from tkinter import filedialog
from pyexcel_xlsx import get_data
import json
from matplotlib import pyplot as plt
from matplotlib import pylab
import tkinter as tk
from joblib import load
from tkinter import messagebox
import webbrowser
import random
from tkinter import *

fig = pylab.gcf()


fig.canvas.manager.set_window_title('Граф')

model = tf.keras.models.load_model('man_practic.h5')

knn = load('knn.joblib')

boosting = load('gradient_boosting_classifier.joblib')

plt.bar(x=[0], height=[0])

def show_popup():
    messagebox.showinfo("Детальніше", "Класифікатор 1 - це класифікатор з застосуванням методу лінійної регресії\n\n"
                                      "Класифікатор 2 - це класифікатор з застосуванням методу k-найблищих сусідів\n\n"
                                      "Класифікатор 3 - це класифікатор з застосуванням методу градієнтного бустінгу\n\n"
                                      "_______________________________________________________________\n\n"
                                      "При показі графіку на вісі класів: 0 - високий економічний рівень розвитку, "
                                      "1 - низький економічний рівень розвитку, "
                                      "2 - економічний рівень розвитку нище середнього, "
                                      "3 - економічний рівень розвитку вище середнього\n\n"
                                      "Графік відповідей працює лише для класифікатора 1")

def predict_regression():
    values = [entry.get() for entry in entries]
    print("Collected values:", values)

    values[2] = str(float(values[2])/float(values[14]))
    values = values[0:14]

    b = np.array(values)
    print(b)
    b = b.reshape(1, -1)
    b = np.asarray(b).astype('float32')
    print(b)
    predictions = model.predict(tf.convert_to_tensor(b), verbose=None)


    predicted_labels = np.argmax(predictions, axis=1)
    print(predicted_labels)
    print(predicted_labels.tolist()[0])
    res = ''
    if predicted_labels.tolist()[0] == 1:
        res = 'Низький'
    if predicted_labels.tolist()[0] == 2:
        res = 'Нище середнього'
    if predicted_labels.tolist()[0] == 3:
        res = 'Вище середнього'

    if predicted_labels.tolist()[0] == 0:
        res = 'Високий'
    result_label.config(text=f"Клас: {res}")
    print(predictions[0])
    print(predictions[0]*10)

    plt.bar(x=[0, 1, 2, 3], height=predictions[0], color="green")

def predict_knn():
    values = [entry.get() for entry in entries]
    print("Collected values:", values)

    values[2] = str(float(values[2])/float(values[14]))
    values = values[0:14]

    b = np.array(values)
    print(b)
    b = b.reshape(1, -1)
    b = np.asarray(b).astype('float32')
    # b = np.asarray(b).astype('float32')
    # print(b)
    # predictions = model.predict(tf.convert_to_tensor(b))
    #
    #
    # predicted_labels = np.argmax(predictions, axis=1)
    # print(predicted_labels)
    # print(predicted_labels.tolist()[0])
    prediction = knn.predict(b)
    res = ''
    if prediction.tolist()[0] == 1:
        res = 'Низький'
    if prediction.tolist()[0] == 2:
        res = 'Нище середнього'
    if prediction.tolist()[0] == 3:
        res = 'Вище середнього'
    if prediction.tolist()[0] == 0:
        res = 'Високий'
    result_label.config(text=f"Клас: {res}")
    # print(predictions[0])
    # print(predictions[0]*10)

    # plt.bar(x=[0, 1, 2, 3], height=predictions[0], color="green")

def predict_boosting():
    values = [entry.get() for entry in entries]
    print("Collected values:", values)

    values[2] = str(float(values[2]) / float(values[14]))
    values = values[0:14]

    b = np.array(values)
    print(b)
    b = b.reshape(1, -1)
    b = np.asarray(b).astype('float32')
    # b = np.asarray(b).astype('float32')
    # print(b)
    # predictions = model.predict(tf.convert_to_tensor(b))
    #
    #
    # predicted_labels = np.argmax(predictions, axis=1)
    # print(predicted_labels)
    # print(predicted_labels.tolist()[0])
    prediction = boosting.predict(b)
    res = ''
    if prediction.tolist()[0] == 1:
        res = 'Низький'
    if prediction.tolist()[0] == 2:
        res = 'Нище середнього'
    if prediction.tolist()[0] == 3:
        res = 'Вище середнього'
    if prediction.tolist()[0] == 0:
        res = 'Високий'
    result_label.config(text=f"Клас: {res}")
    # print(predictions[0])
    # print(predictions[0]*10)

    # plt.bar(x=[0, 1, 2, 3], height=predictions[0], color="green")

def download():
    url = 'https://drive.google.com/file/d/1xlQYdXPeGhXuH9jkotv7fX86zu-VuN6w/view?usp=sharing'
    # Open the URL in the default browser
    webbrowser.open(url)

def excel():
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                             filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")])
    print(file_path)
    records = get_data(file_path)
    print(list(json.loads(json.dumps(records)).values()))
    values = list(json.loads(json.dumps(records)).values())[0][0]
    print(values)
    counter = 0
    while counter != 15:
        entries[counter].delete(0, tk.END)
        counter += 1
    counter = 0
    while counter != 15:
        entries[counter].insert(0, values[counter])
        counter += 1

def generate():
    counter = 0
    while counter != 15:
        entries[counter].delete(0, tk.END)
        counter += 1
    counter = 0
    while counter != 15:
        if counter == 2:
            entries[counter].insert(0, str(random.randint(0, 10000000000)))
        elif counter == 4:
            entries[counter].insert(0, str(random.randint(0, 50000)))
        elif counter == 9:
            entries[counter].insert(0, str(random.randint(0, 90)))
        elif counter == 11:
            entries[counter].insert(0, str(random.randint(0, 400)))
        elif counter == 14:
            entries[counter].insert(0, str(random.randint(0, 600000000)))
        else:
            entries[counter].insert(0, str(round(random.random(), 3)))
        counter += 1

def graph():
    plt.xlabel('Класи', color="green")
    plt.ylabel('Шанс вибору', color="green")
    plt.title("Графік Класифікації", color="green")
    plt.show()


root = tk.Tk()
root.resizable(False, False)
root.title("Класифікатор країни за її економічним рівнем розвитку")


form_frame = tk.Frame(root)
form_frame.pack(padx=10, pady=10)


entries = []

labels = ['Сільське господарство, лісове господарство та рибальство, додана вартість (% ВВП)',
          'Експорт товарів і послуг (% ВВП)',
          'Прямі іноземні інвестиції, чистий приплив (ПБ, поточні долари США)',
          'Зростання ВВП (річний %)',
          'ВНД на душу населення, ПКС (долари)',
          'Валове накопичення капіталу (% ВВП)',
          'Експорт високотехнологічних товарів (% експорту промислової продукції)',
          'Імпорт товарів і послуг (% ВВП)',
          'Промисловість (включаючи будівництво), додана вартість (% ВВП)',
          'Очікувана тривалість життя при народженні, загальна (років)',
          'Торгівля товарами (% ВВП)',
          'Рівень смертності, до 5 років (на 1000 живонароджених)',
          'Дохід, за винятком грантів (% ВВП)',
          'Податкові надходження (% ВВП)',
          'Кількість населення',]

cou = 0

for i in range(1, 16):

    label = tk.Label(form_frame, text=f'{labels[cou]}:')
    label.grid(row=i, column=0, sticky='w', padx=5, pady=5)


    entry = tk.Entry(form_frame)
    entry.grid(row=i, column=1, padx=5, pady=5)


    entries.append(entry)
    cou += 1

form_frame2 = tk.Frame(root)
form_frame2.pack(padx=10, pady=10)

predict_button = tk.Button(form_frame2, text="Згенерувати випадкові значення", command=generate)
predict_button.grid(row=0, column=3, padx=10, pady=10)
predict_button = tk.Button(form_frame2, text="Класифікатор 1", command=predict_regression)
predict_button.grid(row=0, column=0, padx=10, pady=10)
predict_button = tk.Button(form_frame2, text="Класифікатор 2", command=predict_knn)
predict_button.grid(row=0, column=1, padx=10, pady=10)
predict_button = tk.Button(form_frame2, text="Класифікатор 3", command=predict_boosting)
predict_button.grid(row=0, column=2, padx=10, pady=10)

# form_frame2 = tk.Frame(root)
# form_frame2.pack(padx=10, pady=10)
predict_button = tk.Button(form_frame2, text="Export excel", command=excel)
predict_button.grid(row=1, column=0, padx=10, pady=10)
predict_button = tk.Button(form_frame2, text="Показати графік відповідей", command=graph)
predict_button.grid(row=1, column=1, padx=10, pady=10)
predict_button = tk.Button(form_frame2, text="Детальніше", command=show_popup)
predict_button.grid(row=1, column=2, padx=10, pady=10)
predict_button = tk.Button(form_frame2, text="Завантажити модель та модифікувати", command=download)
predict_button.grid(row=1, column=3, padx=10, pady=10)

result_label = tk.Label(root, fg='blue', text=f'')
result_label.pack(pady=20)

print(entries)
root.iconbitmap(r'we.ico')
root.mainloop()