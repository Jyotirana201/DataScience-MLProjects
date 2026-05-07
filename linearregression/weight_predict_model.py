from tkinter import * 
import joblib


model = joblib.load("ML/weight_predictor.joblib")


def predit():
    height = float(hr_entry.get())
    print(type(height))
    predicted_value = model.predict([[height]])
    out_put.config(text = f"Your Predicted Weight: {str(predicted_value)[1:5]}")


app = Tk()
app.geometry("700x380")
app.config(bg = "#cbacd8")
app.title("Weight_predictor")
app.resizable(False,False)




heading = Label(app, text = "Weight Predictor", font = "Corbel 30 bold", fg = "#83749f", bg = "#cbacd8")
heading.pack(fill = "x", pady=20)


text1 = Label(app, text = "Height in cm : ", font = "Calibri 18 bold", fg = "#83749f", bg = "#cbacd8")
text1.place(x=100, y=130)
hr_entry = Entry(app, font = "arial 16", width=25,fg = "#cbacd8")
hr_entry.place(x=250, y=130)

predict_btn = Button(app, text = "Predictor", font = "arial 18 bold",width="20",fg = "#cbacd8", bg = "#83749f", command = predit,cursor='hand2',activebackground="#83749f",activeforeground='#cbacd8')
predict_btn.place(x=250, y=180)


out_put = Label(app, font = "Calibri 18", fg = "#83749f", bg = "#cbacd8")
out_put.place(x=190, y=260)



app.mainloop()

