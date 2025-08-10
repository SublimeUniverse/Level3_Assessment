import csv, random
from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter


class BootUp:

    def __init__(self):
        self.start_frame = tkinter.Frame(padx=10, pady=10, bg="#7BD517")
        self.start_frame.grid()

        # Strings for buttons
        first_level_string = "Level 1(Addition & Subtraction)"
        second_level_string = "Level 2(Multiplication)"
        third_level_string = "Level 3(Division)"

        start_labels_list = [
            ["Welcome to the Maths Game!", ("Arial", "15", "bold"), "#FFFFFF", "#0033CB"],
            ["Please select a level to play below", ("Arial", "11", "bold"), None, "#7BD517"]

        ]

        start_label_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1], fg=item[2], bg=item[3],
                               wraplength=350, justify="left",
                               pady=10, padx=20)

            make_label.grid(row=count)

            start_label_ref.append(make_label)

        # Create first button
        self.first_button = Button(self.start_frame, width=30, height=2,
                                   text="Level 1(Addition & Subtraction)", bg="#82B366",
                                   fg="#FFFFFF", command=self.first_button_clicked)
        self.first_button.grid(row=3, column=0)

        # Create second button
        self.second_button = Button(self.start_frame, width=30, height=2,
                                    text="Level 2(Multiplication)", bg="#F0A30A", fg="#FFFFFF",
                                    command=self.second_button_clicked)
        self.second_button.grid(row=4, column=0, padx=20, pady=20)

        # Create third button
        self.third_button = Button(self.start_frame, width=30, height=2,
                                   text="Level 3(Division)", bg="#E51400", fg="#FFFFFF",
                                   command=self.third_button_clicked)
        self.third_button.grid(row=5, column=0)

    def first_button_clicked(self):
        # This function will be called when the first button is clicked

        print("First button has been clicked")

    def second_button_clicked(self):
        # This function will be called when the second button is clicked

        print("Second button has been clicked")

    def third_button_clicked(self):
        # This function will be called when the third button is clicked

        print("Third button has been clicked")


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    BootUp()
    root.mainloop()
