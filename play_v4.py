import csv, random
from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows
import random


class Play:
    def __init__(self, how_many, level):

        questions_answered = 0

        while questions_answered < how_many:

            # Generate questions
            operations = ["+", "-", "/", "*"]

            first_number = random.randint(0, 100)
            second_number = random.randint(0, 100)

            if level == 1:
                operation = random.choice(operations[:2])
            elif level == 2:
                operation = "*"
            else:
                operation = "/"

            if operations == "+":
                answer = first_number + second_number
            elif operations == "-":
                answer = first_number - second_number
            elif operation == "/":
                answer = first_number / second_number
            else:
                answer = first_number * second_number

            questions_answered += 1


        # Initial start frame
        self.start_frame = Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        # First text label(Title)
        self.question_label = Label(self.start_frame,
                                    text=f" Question {questions_answered} "
                                         f"of {how_many} ",
                                    font=("Arial", 25, "bold"), bg="#F5F5F5", borderwidth=2, relief="solid")
        self.question_label.grid(row=0, pady=10, padx=10)

        # label for asking questions
        self.ask_question = Label(self.start_frame, text=f" What is {first_number} {operation} {second_number} ",
                                  font=("Arial", 20, "bold"), bg="#DAE8FC")
        self.ask_question.grid(row=1, pady=20)

        # so that entry and go button are in the same line without too much gap
        self.entry_area_frame = Frame(self.start_frame, bg="#D5E8D4")
        self.entry_area_frame.grid(row=2, pady=10)

        # Entry box
        self.enter_answer = Entry(self.entry_area_frame, font=("Arial", 22, "bold"), width=10, bg="#F5F5F5")
        self.enter_answer.grid(row=2, column=0, padx=10)

        # Go button
        self.go_button = Button(self.entry_area_frame, font=("Arial", 10, "bold"),
                                width=7, height=2, text="GO", bg="#60A917", fg="#FFFFFF")
        self.go_button.grid(row=2, column=1)

        # Stats button
        self.stats_button = Button(self.start_frame, font=("Arial", 15, "bold"),
                                   width=20, text="Statistics", bg="#1BA1E2", fg="#FFFFFF")
        self.stats_button.grid(row=3, pady=10)

        # End Game button
        self.end_game_button = Button(self.start_frame, font=("Arial", 15, "bold"),
                                      width=20, text="End Game", bg="#E51400", fg="#FFFFFF")
        self.end_game_button.grid(row=4)







# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Play(2, 1)
    root.mainloop()
