import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for image handling
import joblib
import numpy as np

# Load the trained model
model = joblib.load("ML/classification/cancer1.joblib")

def predict_cancer():
    try:
        # Collect input values from entry fields
        inputs = [float(entry.get()) if entry.get() else 0 for entry in entries]  
        prediction_input = np.array([inputs])
        result = model.predict(prediction_input)[0]

        result_text = "Positive for Cancer" if result == 1 else "Not Cancer"
        output_label.config(text=f"Prediction: {result_text}")  # Display result in GUI

    except ValueError:
        output_label.config(text="Error: Invalid Input (Enter numbers only)")

# Initialize Tkinter window
root = tk.Tk()
root.title("Cancer Prediction")
root.geometry("1200x600") 
root.config(bg="#e9e7e9")
root.resizable(False, False)  

# Add a Heading
heading = tk.Label(root, text="Cancer Prediction", font=("Arial", 28, "bold"), fg="#709eab", bg="#e9e7e9")
heading.place(x=400, y=20)

# Load and Display Image
image_path = "ML/classification/doctor.png"  
try:
    image = Image.open(image_path)
    image = image.resize((500, 500))  
    photo = ImageTk.PhotoImage(image)
    
    image_label = tk.Label(root, image=photo, bg="#e9e7e9")
    image_label.place(x=720, y=50)  

except Exception as e:
    print("Error loading image:", e)

# Define Features
features = [
    "Age", "No. of sexual partners", "No. of pregnancies", "Smokes (years)", "Smokes (packs/year)",
    "Hormonal Contraceptive", "IUD", "IUD (years)","STDs: Condylomatosis", "STDs: Syphilis", "STDs: PID",
    "STDs: Genital herpes", "STDs: MC", "STDs: AIDS", "STDs: HIV", "STDs: Hepatitis B", 
    "STDs: HPV", "STDs: No. of diagnoses", "Dx: Cancer"
]

# Create Entry Fields for Inputs
entries = []
x_offset = 60
y_offset = 100

for i in range(len(features)):
    row = i // 2  
    column = i % 2  
    x_position = x_offset + (column * 320)
    y_position = y_offset + (row * 40)

    label = tk.Label(root, text=features[i] + ":", font=("Calibri", 12, "bold"), bg="#e9e7e9", fg="#709eab")
    label.place(x=x_position, y=y_position)
    
    entry = tk.Entry(root, font=("Calibri", 12))
    entry.place(x=x_position + 200, y=y_position, width=100)
    
    entries.append(entry)

# Predict Button
tk.Button(root, text="Predict", command=predict_cancer, font=("Arial", 14), width="15",bg="lightblue",cursor='hand2', activebackground="#c2b4d0", activeforeground='#fdfcf2').place(x=450, y=460)

# Label to display prediction output
output_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#e9e7e9", fg="#709eab")
output_label.place(x=400, y=520)

root.mainloop()
