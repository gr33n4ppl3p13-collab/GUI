from tkinter import *
from datetime import datetime


def update_date():
    # Format current date as "%B %d, %Y" (e.g., "December 25, 2024")
    formatted_date = datetime.now().strftime("%B %d, %Y")

    # Update the text on the label widget
    date_label.config(text=formatted_date)

    # Schedule the update_date function to run again after 1000ms (1 second)
    SCREEN.after(1000, update_date)


# 1. Initialize the main application window
SCREEN = Tk()
SCREEN.title("Calendar Widget")
SCREEN.geometry("350x120")

# 2. Add a label to display the formatted date
date_label = Label(SCREEN, font=("Arial", 22, "bold"), fg="#1E293B")
date_label.place(x=100,y=50)

# Start updating the date logic
update_date()

# Run the application loop
mainloop()