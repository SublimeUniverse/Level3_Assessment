import csv, random
from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter


class StartGame:

    def __init__(self, level):
        self.start_frame = tkinter.Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        # Strings for buttons
        first_level_string = "Level 1(Addition & Subtraction)"
        second_level_string = "Level 2(Multiplication)"
        third_level_string = "Level 3(Division)"

        start_labels_list = [
            [level, ("Arial", "15", "bold"), "#000000", "#87CBE8"],
            ["Please select a level to play below", ("Arial", "11", "bold"), None, "#D5E8D4"]

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
                                   text=first_level_string, bg="#82B366",
                                   fg="#FFFFFF", font=("Arial", "9", "bold"), command=lambda: self.get_level("1"))
        self.first_button.grid(row=3, column=0)

        # Create second button
        self.second_button = Button(self.start_frame, width=30, height=2,
                                    text=second_level_string, bg="#F0A30A", fg="#FFFFFF",
                                    font=("Arial", "9", "bold"), command=lambda: self.get_level("2"))
        self.second_button.grid(row=4, column=0, padx=20, pady=20)

        # Create third button
        self.third_button = Button(self.start_frame, width=30, height=2,
                                   text=third_level_string, bg="#E51400", fg="#FFFFFF",
                                   font=("Arial", "9", "bold"), command=lambda: self.get_level("3"))
        self.third_button.grid(row=5, column=0)
