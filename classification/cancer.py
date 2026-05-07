import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow for image handling
import joblib
import numpy as np

# Load the trained model
model = joblib.load("ML/classification/cancer1.joblib")

def predict_cancer():
    try:
        inputs = [float(entry.get()) for entry in entries]
        print(f"Number of inputs: {len(inputs)}")
        prediction_input = np.array([inputs])
        result = model.predict(prediction_input)[0]

        result_text = "Positive for Cancer" if result == 1 else "Not Cancer"
        print(result_text)  # Print result in the console
        output_label.config(text=f"Prediction: {result_text}")  # Display result in GUI

    except ValueError:
        print("Error: Please enter valid numeric values")
        output_label.config(text="Error: Invalid Input")

# Initialize Tkinter window
root = tk.Tk()
root.title("Cancer Prediction")
root.geometry("1000x500") 
root.config(bg="#fdfcf2")
root.resizable(False, False) # Increased width for the image

# Add a Heading at the Top
heading = tk.Label(root, text="Cancer Prediction", font=("Arial", 20, "bold"), fg="purple")
heading.grid(row=0, column=0, columnspan=4, pady=10)

# Load and Display Image (Ensure image path is correct)
image_path = "ML/classification/doctor.png"  # Replace with the actual image file path
try:
    image = Image.open(image_path)
    image = image.resize((200, 200))  # Resize image to fit
    photo = ImageTk.PhotoImage(image)
    
    image_label = tk.Label(root, image=photo)
    image_label.grid(row=1, column=4, rowspan=10, padx=30, pady=10)  # Placing it on the right side

except Exception as e:
    print("Error loading image:", e)

features = [
    "Age", "Number of sexual partners", "Num of pregnancies", "Smokes (years)", "Smokes (packs/year)",
    "Hormonal Contraceptives", "IUD", "IUD (years)","STDs: Condylomatosis", "STDs: Syphilis", "STDs: Pelvic inflammatory disease",
    "STDs: Genital herpes", "STDs: Molluscum contagiosum", "STDs: AIDS", "STDs: HIV", "STDs: Hepatitis B", 
    "STDs: HPV", "STDs: Number of diagnoses", "Dx: Cancer"
]
#'Age', 'Number of sexual partners', 'Num of pregnancies',
    #    'Smokes (years)', 'Smokes (packs/year)', 'Hormonal Contraceptives',
    #    'IUD', 'IUD (years)', 'STDs:condylomatosis',
    #    'STDs:vaginal condylomatosis', 'STDs:vulvo-perineal condylomatosis',
    #    'STDs:syphilis', 'STDs:pelvic inflammatory disease',
    #    'STDs:genital herpes', 'STDs:molluscum contagiosum', 'STDs:AIDS',
    #    'STDs:HIV', 'STDs:Hepatitis B', 'STDs:HPV', 'STDs: Number of diagnosis',
    #    'Dx:Cancer'
entries = []
for i in range(9):
    tk.Label(root, text=features[i]).grid(row=i+1, column=0, padx=5, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=5, pady=5)
    entries.append(entry)

for i in range(9, len(features)):
    tk.Label(root, text=features[i]).grid(row=i-8, column=2, padx=5, pady=5, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i-8, column=3, padx=5, pady=5)
    entries.append(entry)

# Predict button
tk.Button(root, text="Predict", command=predict_cancer, font=("Arial", 12), bg="lightblue").grid(row=max(len(features)//2, 9)+1, column=1, columnspan=2, pady=10)

# Label to display prediction output
output_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
output_label.grid(row=max(len(features)//2, 10)+1, column=1, columnspan=2, pady=10)

root.mainloop()
