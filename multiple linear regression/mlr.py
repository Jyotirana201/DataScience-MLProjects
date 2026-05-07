from tkinter import * 
import joblib


model = joblib.load("ML/multiple linear regression/MLR.joblib")


def predit():
    hs = float(hs_entry.get())
    ps=float(ps_entry.get())
    Ea=float(ea_entry.get())
    sh=float(sh_entry.get())
    pyq=float(pyq_entry.get())

    data=[[hs,ps,Ea,sh,pyq]]
    predicted_value = model.predict(data)
    out_put.config(text = f" Predicted Performance Index: {str(predicted_value)[1:5]}")


app = Tk()
app.geometry("1030x450")
app.config(bg = "#e7d8c3")
app.title("PI_predictor")
app.resizable(False,False)




heading = Label(app, text = "Student Performance", font = "Corbel 30 bold", fg = "#6a2931", bg = "#e7d8c3")
heading.pack(fill = "x", pady=20)


text1 = Label(app, text = "Hours Studied : ", font = "Calibri 18 bold", fg = "#6a2931", bg = "#e7d8c3")
text1.place(x=100, y=130)
hs_entry = Entry(app, font = "arial 16", width=20,fg = "#6a2931")
hs_entry.place(x=270, y=130)

text2 = Label(app, text = "Previous Score : ", font = "Calibri 18 bold", fg = "#6a2931", bg = "#e7d8c3")
text2.place(x=550, y=130)
ps_entry = Entry(app, font = "arial 16", width=20,fg = "#6a2931")
ps_entry.place(x=720, y=130)

text3 = Label(app, text = "Extra Activities : ", font = "Calibri 18 bold", fg = "#6a2931", bg = "#e7d8c3")
text3.place(x=100, y=200)
ea_entry = Entry(app, font = "arial 16", width=20,fg = "#6a2931")
ea_entry.place(x=270, y=200)

text4 = Label(app, text = "Sleep Hours : ", font = "Calibri 18 bold", fg = "#6a2931", bg = "#e7d8c3")
text4.place(x=550, y=200)
sh_entry = Entry(app, font = "arial 16", width=20,fg = "#6a2931")
sh_entry.place(x=720, y=200)

text5 = Label(app, text = "PYQ Practiced : ", font = "Calibri 18 bold", fg = "#6a2931", bg = "#e7d8c3")
text5.place(x=100, y=270)
pyq_entry = Entry(app, font = "arial 16", width=20,fg = "#6a2931")
pyq_entry.place(x=270, y=270)

predict_btn = Button(app, text = "Predictor", font = "arial 18 bold",width="20",fg = "#e7d8c3", bg = "#6a2931", command = predit,cursor='hand2',activebackground="brown",activeforeground='#e7d8c3')
predict_btn.place(x=650, y=270)


out_put = Label(app, font = "Calibri 18", fg = "#6a2931", bg = "#e7d8c3")
out_put.place(x=300, y=350)



app.mainloop()

