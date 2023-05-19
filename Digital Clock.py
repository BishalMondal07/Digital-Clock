import tkinter as tk
import time
from datetime import datetime

def update_clock():
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%A, %B %d, %Y')
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    clock_label.after(1000, update_clock)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.configure(bg="black")

# Create a label for the clock
clock_label = tk.Label(window, font=("Roboto", 80), bg="black", fg="white")
clock_label.pack(pady=50)

# Create a label for the date
date_label = tk.Label(window, font=("Roboto", 24), bg="black", fg="white")
date_label.pack(pady=10)

# Start updating the clock
update_clock()

# Run the main event loop
window.mainloop()




