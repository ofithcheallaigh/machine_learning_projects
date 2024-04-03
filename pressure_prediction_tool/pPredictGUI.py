import tkinter as tk
from tkinter import messagebox
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_gradient(points):
    coefficients = np.polyfit([point[0] for point in points], [point[1] for point in points], 1)
    return coefficients[0]

def predict():
    # get the pressure samples from the entry fields
    pressure_samples = [float(entry.get()) for entry in pressure_entries]
    points = list(enumerate(pressure_samples, start=1))

    # calculate the gradient and y-intercept
    gradient = calculate_gradient(points)
    y_intercept = points[0][1] - gradient * points[0][0]

    # predict when the pressure will reach the target
    pressure_target = float(target_entry.get())
    sample_number = (pressure_target - y_intercept) / gradient

    # show the prediction in a message box
    # messagebox.showinfo("Prediction", f"The pressure will reach {pressure_target} at sample number {sample_number}")

    # plot the line of best fit
    fig.clear()
    ax = fig.add_subplot(111)
    x_values = np.array([point[0] for point in points])
    y_values = gradient * x_values + y_intercept
    ax.plot(x_values, y_values, color='blue')
    ax.scatter(*zip(*points), color='red')
    canvas.draw()

    messagebox.showinfo("Prediction", f"The pressure will reach {pressure_target} at sample number {sample_number}")

# create the main window
root = tk.Tk()

# Create a Figure and a Canvas after creating root
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

# create entry fields for the pressure samples
pressure_entries = [tk.Entry(root) for _ in range(5)]
for i, entry in enumerate(pressure_entries, start=1):
    tk.Label(root, text=f"Pressure sample {i}:").grid(row=i-1, column=0)
    entry.grid(row=i-1, column=1)

# create an entry field for the target pressure
tk.Label(root, text="Target pressure:").grid(row=5, column=0)
target_entry = tk.Entry(root)
target_entry.grid(row=5, column=1)

# create a button to make the prediction
predict_button = tk.Button(root, text="Predict", command=predict)
predict_button.grid(row=6, column=0, columnspan=2)

# start the main loop
root.mainloop()