from tkinter import *
import joblib
import numpy as np

# Load the binary classification model
model = joblib.load("ML/binaryclassification/Binary_model.joblib")

def predict():
    input_value = age_entry.get()
    age = float(input_value)  
    data = np.array([[age]])
    prediction = model.predict(data)
    if prediction == 1:
        result = "Likely to Buy Insurance"
    else:
        result = "Unlikely to Buy Insurance"
    output_label.config(text=f"Prediction: {result}")



# GUI setup
app = Tk()
app.geometry("600x300")
app.config(bg="#f7e2c7")
app.title("Binary Classification Predictor")
app.resizable(False, False)

# Heading
heading = Label(app, text="Binary Classification Predictor", font="Corbel 24 bold", fg="#e7491a", bg="#f7e2c7")
heading.pack(pady=20)

# Input Label and Entry
age_label = Label(app, text="Enter Age:", font="Calibri 18 bold", fg="#e7491a", bg="#f7e2c7")
age_label.place(x=50, y=100)
age_entry = Entry(app, font="arial 16", width=20, fg="#e7491a")
age_entry.place(x=200, y=100)

# Predict Button
predict_button = Button(app, text="Predict", font="arial 18 bold", width=15, fg="#f7e2c7", bg="#e7491a",
                        command=predict, cursor='hand2', activebackground="#ec8751", activeforeground='#f7e2c7')
predict_button.place(x=200, y=170)

# Output Label
output_label = Label(app, text="", font="Calibri 18", fg="#e7491a", bg="#f7e2c7")
output_label.place(x=155, y=240)

app.mainloop()
