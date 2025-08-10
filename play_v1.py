import csv, random
from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows

class Play:
    def __init__(self):
        self.start_frame = Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()
        questions_answered = 0


        self.question_label = Label(self.start_frame,
                                    text=f" Question 2 "
                                         f"of 3 ",
                                     font=("Arial", 20, "bold"), bg="#F5F5F5")
        self.question_label.grid(row=0, pady=10, padx=10)

        self.ask_question = Label(self.start_frame, text=" What is 6 x 5 ",
                                  font=("Arial", 17, "bold"), bg="#DAE8FC")
        self.ask_question.grid(row=1, pady=20)

        self.enter_answer = Entry(self.start_frame, font=("Arial", 15, "bold"), width=15)
        self.enter_answer.grid(row=2, column=0)

        self.go_button = Button(self.start_frame, font=("Arial", 10, "bold"), width=7, height=2, text="GO")
        self.go_button.grid(row=2, column=1)

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Play()
    root.mainloop()