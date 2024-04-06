import tkinter as tk
from tkinter import messagebox, filedialog, Entry, Label, Button
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

'''
TODO:
Add a GUI title
Show the gradient figure
Can we stream data in?
What about logic to monitor the gradient and only start saving data when the gradient is above a certain value?
Add a waring if the data is not in the correct format in the CSV file
'''

def calculate_gradient(points):
    coefficients = np.polyfit([point[0] for point in points], [point[1] for point in points], 1)
    return coefficients[0]

def load_csv():
    filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filename:
        df = pd.read_csv(filename,encoding='latin1', header=None,  on_bad_lines='skip')
        global pressure_samples
        pressure_samples = df[0].tolist()
        pressure_samples = [float(sample) for sample in pressure_samples]
        print("wait")

def predict():
    print("In Predict")
    global pressure_samples
    global target_entry
    # get the pressure samples from the entry fields
    points = list(enumerate(pressure_samples, start=1))

    # calculate the gradient and y-intercept
    gradient = calculate_gradient(points)
    y_intercept = points[0][1] - gradient * points[0][0]

    # predict when the pressure will reach the target
    # get the target pressure
    target_pressure_str = target_entry.get()
    # check if the target pressure string is not empty
    if target_pressure_str:
        pressure_target = float(target_pressure_str)
        # rest of your code...
        # else:
        #    print("Please enter a target pressure.")
        # pressure_target = float(target_entry.get())
        sample_number = (pressure_target - y_intercept) / gradient

        # calculate the number of samples already taken
        samples_taken = len(points)

        # calculate the number of samples until the pressure reaches the target
        samples_until_target = sample_number - samples_taken

        # calculate the time until the pressure reaches the target
        time_until_target = samples_until_target * 20  # multiply by the time interval between samples

        # plot the line of best fit
        fig.clear()
        ax = fig.add_subplot(111)
        x_values = np.array([point[0] for point in points])
        y_values = gradient * x_values + y_intercept
        ax.plot(x_values, y_values, color='blue')
        ax.scatter(*zip(*points), color='red')
        canvas.draw()

        # messagebox.showinfo("Prediction", f"The pressure will reach {pressure_target} at sample number {int(sample_number)}, which is in {int(time_until_target)} seconds.")
        messagebox.showinfo("Prediction", f"The pressure will reach {pressure_target} in {int(time_until_target)} seconds.")

    else:
        messagebox.showwarning("Warning", "Please enter a target pressure, and the press Predict.")
# create the main window
root = tk.Tk()

# create a title label with larger text
title_label = Label(root, text="Sensata Low Pressure Predictor Tool", font=("Arial", 18),fg="blue")
title_label.grid(row=0, column=0, columnspan=2)

explain_label = Label(root, text="This tool will predict when the pressure will reach the target pressure.")
explain_label.grid(row=1, column=0, columnspan=2)
explain_label1 = Label(root, text="Please enter a target pressure and load a CSV file with the pressure samples.")
explain_label1.grid(row=2, column=0, columnspan=2)


# create an Entry for the target pressure
target_label = Label(root, text="Target Pressure")
target_label.grid(row=3, column=0, pady=(10, 0), sticky='e')
target_entry = Entry(root)
target_entry.grid(row=3, column=1, sticky='w')  # adjust the row and column as needed

# create a button to load the csv file
load_button = Button(root, text="Load CSV", command=load_csv)
load_button.grid(row=5, column=0, columnspan=2)

# create a button to make the prediction
predict_button = Button(root, text="Predict", command=predict)
predict_button.grid(row=6, column=0, columnspan=2)

# Create a Figure and a Canvas after creating root
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)  # create an Axes object in the Figure
ax.set_title("Data Plotting Area")  # set the title of the plot

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

pressure_samples = []

# start the main loop
root.mainloop()