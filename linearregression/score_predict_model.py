from tkinter import * 
import joblib


model = joblib.load("ML/score_predictor.joblib")


def predit():
    hours = float(hr_entry.get())
    print(type(hours))
    predicted_value = model.predict([[hours]])
    out_put.config(text = f"Your Predicted Scores: {str(predicted_value)[1:7]}")


app = Tk()
app.geometry("700x380")
app.config(bg = "black")
app.title("score_predictor")
app.resizable(False,False)




heading = Label(app, text = "Score Predictor", font = "Corbel 30 bold", fg = "#fe2b5f", bg = "black")
heading.pack(fill = "x", pady=20)


text1 = Label(app, text = "Study Hour : ", font = "Calibri 18 bold", fg = "#fe2b5f", bg = "black")
text1.place(x=100, y=130)
hr_entry = Entry(app, font = "arial 16", width=25,fg = "#fe2b5f")
hr_entry.place(x=250, y=130)

predict_btn = Button(app, text = "Predictor", font = "arial 18 bold",width="20",fg = "black", bg = "#fe2b5f", command = predit,cursor='hand2',activebackground="pink",activeforeground='black')
predict_btn.place(x=250, y=180)


out_put = Label(app, font = "Calibri 18", fg = "#fe2b5f", bg = "black")
out_put.place(x=190, y=260)



app.mainloop()

