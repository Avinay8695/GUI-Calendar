from tkinter import *
from tkcalendar import Calendar

def fetch_date():
    selected_date = cal.get_date()
    date_label.config(text="Selected Date: " + selected_date)

# Create the Tkinter window
root = Tk()
root.title("Avinay GUI Calendar Project")  # Added project name
root.geometry("400x400")

# Set the background color to yellow
root.config(bg="yellow")

# Create the Calendar widget
cal = Calendar(root, selectmode="day", year=2023, month=7, date=28)
cal.pack(pady=20)

# Create a button to trigger date selection
select_button = Button(root, text="Select Date", command=fetch_date)
select_button.pack(pady=10)

# Create a label to display the selected date
date_label = Label(root, text="Selected Date: ", font=("Helvetica", 12))
date_label.pack(pady=20)

# Start the Tkinter main event loop
root.mainloop()
