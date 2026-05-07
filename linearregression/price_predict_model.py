# from tkinter import * 
# import joblib


# model = joblib.load("ML/price_predictor.joblib")


# def predit():
#     area = float(hr_entry.get())
#     print(type(area))
#     predicted_value = model.predict([[area]])
#     out_put.config(text = f"Your Predicted Price: {str(predicted_value)[1:10]}")


# app = Tk()
# app.geometry("700x380")
# app.config(bg = "#e7d8c3")
# app.title("Price_predictor")
# app.resizable(False,False)




# heading = Label(app, text = "Price Predictor", font = "Corbel 30 bold", fg = "#6a2931", bg = "#e7d8c3")
# heading.pack(fill = "x", pady=20)


# text1 = Label(app, text = "House Area : ", font = "Calibri 18 bold", fg = "#6a2931", bg = "#e7d8c3")
# text1.place(x=100, y=130)
# hr_entry = Entry(app, font = "arial 16", width=25,fg = "#6a2931")
# hr_entry.place(x=250, y=130)

# predict_btn = Button(app, text = "Predictor", font = "arial 18 bold",width="20",fg = "#e7d8c3", bg = "#6a2931", command = predit,cursor='hand2',activebackground="brown",activeforeground='#e7d8c3')
# predict_btn.place(x=250, y=180)


# out_put = Label(app, font = "Calibri 18", fg = "#6a2931", bg = "#e7d8c3")
# out_put.place(x=190, y=260)



# app.mainloop()





