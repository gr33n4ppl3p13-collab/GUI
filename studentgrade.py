from tkinter import *

SCREEN = Tk()
SCREEN.title("Grade Calculator")
SCREEN.geometry("900x680")
SCREEN.config(background="#d9d9d9")


def calculate_grade():
        math = float(math_entry.get())
        science = float(science_entry.get())
        english = float(english_entry.get())
        average = (math + science + english) / 3

        if average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "F"

        student_name = name_entry.get()
        student_roll = roll_entry.get()

        result = (
            f"Name: {student_name}\n"
            f"Roll No: {student_roll}\n"
            f"Math: {math}\n"
            f"Science: {science}\n"
            f"English: {english}\n"
            f"Average: {average:.2f}\n"
            f"Grade: {grade}"
        )
        result_text.delete("1.0", END)
        result_text.insert(END, result)


def save_student():
    student_name = name_entry.get()
    student_roll = roll_entry.get()

    if student_name == "" or student_roll == "":
        result_text.delete("1.0", END)
        result_text.insert(END, "Name and Roll No cannot be empty.")
        return

    try:
        math = float(math_entry.get())
        science = float(science_entry.get())
        english = float(english_entry.get())
    except ValueError:
        result_text.delete("1.0", END)
        result_text.insert(END, "Please enter valid marks before saving.")
        return

    with open("student_records.txt", "a") as file:
        file.write(f"{student_name},{student_roll},{math},{science},{english}\n")

    result_text.delete("1.0", END)
    result_text.insert(END, f"Student saved successfully:\nName: {student_name}\nRoll No: {student_roll}")


heading = Label(SCREEN, text="Student Grading System", font=("Arial", 36, "bold"), bg="#d9d9d9")
heading.place(x=190, y=40)

name_label = Label(SCREEN, text="Name:", font=("Arial", 18), bg="#d9d9d9")
name_label.place(x=210, y=130)
name_entry = Entry(SCREEN, width=22, font=("Arial", 16))
name_entry.place(x=420, y=130)

roll_label = Label(SCREEN, text="Roll No:", font=("Arial", 18), bg="#d9d9d9")
roll_label.place(x=210, y=185)
roll_entry = Entry(SCREEN, width=22, font=("Arial", 16))
roll_entry.place(x=420, y=185)

math_label = Label(SCREEN, text="Math Marks:", font=("Arial", 18), bg="#d9d9d9")
math_label.place(x=210, y=240)
math_entry = Entry(SCREEN, width=22, font=("Arial", 16))
math_entry.place(x=420, y=240)

science_label = Label(SCREEN, text="Science Marks:", font=("Arial", 18), bg="#d9d9d9")
science_label.place(x=210, y=295)
science_entry = Entry(SCREEN, width=22, font=("Arial", 16))
science_entry.place(x=420, y=295)

english_label = Label(SCREEN, text="English Marks:", font=("Arial", 18), bg="#d9d9d9")
english_label.place(x=210, y=350)
english_entry = Entry(SCREEN, width=22, font=("Arial", 16))
english_entry.place(x=420, y=350)

calculate_button = Button(SCREEN,text="Calculate Grade",width=18,height=2,command=calculate_grade,bg="#f6d500",fg="black",font=("Arial", 18, "bold"),bd=2)
calculate_button.place(x=280, y=400)

save_button = Button(SCREEN,text="Save Student",width=18,height=2,command=save_student,bg="#36c4ff",fg="black",font=("Arial", 18, "bold"),bd=2)
save_button.place(x=280, y=470)

output_frame = Frame(SCREEN, width=740, height=120, bg="#d9d9d9", bd=0)
output_frame.place(x=80, y=540)

result_text = Text(output_frame, width=90, height=6, font=("Arial", 14), wrap=WORD, relief="flat", bd=0, bg="#d9d9d9")
result_text.place(x=10, y=10)

mainloop()
