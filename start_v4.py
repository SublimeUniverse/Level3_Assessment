import csv, random
from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows



class Instructions:
    def __init__(self):
        # Make frame to hold instructions
        self.start_frame = Frame(padx=10, pady=10, bg="#FAD7AC")
        self.start_frame.grid()

        # Instructions heading
        self.instruction_heading = Label(self.start_frame, text="  Instructions  ",
                                         font=("Arial", 20, "bold"), bg="#FFFF88")
        self.instruction_heading.grid(row=0)

        # display instructions text
        self.instruction_text = Label(self.start_frame, text=instructions_text.instructions,
                                      font=("Arial", 10, "bold"), width=50)
        self.instruction_text.grid(row=1, pady=10)

        # proceed button after user has finished reading instructions
        self.proceed_button = Button(self.start_frame, font=("Arial", 10, "bold"), width=9, text="Proceed",
                                     bg="#FFA500", command=self.proceed)
        self.proceed_button.grid(row=2, column=0)

    def proceed(self):
        Start()
        root.destroy()


class Statistics:
    def __init__(self):
        print("you are in stats class")


class Start:
    def __init__(self):

        self.start_frame = Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        self.num_rounds_entry = Entry(self.start_frame, font=("Arial", 20, "bold"), width=9)

        self.num_rounds_entry.grid(row=3, column=0)

        # Text Strings
        first_level_string = "Level 1(Addition & Subtraction)"
        second_level_string = "Level 2(Multiplication)"
        third_level_string = "Level 3(Division)"
        self.label = "Please enter number of rounds"

        start_labels_list = [
            ["Welcome to the Maths Game!", ("Arial", "15", "bold"), "#000000", "#87CBE8"],
            [self.label, ("Arial", "11", "bold"), None, "#D5E8D4"]

        ]

        start_label_ref = []
        for count, item in enumerate(start_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1], fg=item[2], bg=item[3],
                               wraplength=350, justify="left",
                               pady=10, padx=20)

            make_label.grid(row=count)

            start_label_ref.append(make_label)

        # Extract choice label so it can be change if theres an error in users input
        self.choose_label = start_label_ref[1]


        # Create first level button
        self.first_button = Button(self.start_frame, width=30, height=2,
                                   text=first_level_string, bg="#82B366",
                                   fg="#FFFFFF", font=("Arial", 9, "bold"), command=lambda: self.check_rounds(1))
        self.first_button.grid(row=4, pady=10)

        # Create second level button
        self.second_button = Button(self.start_frame, width=30, height=2,
                                    text=second_level_string, bg="#F0A30A", fg="#FFFFFF",
                                    font=("Arial", 9, "bold"), command=lambda: self.check_rounds(2))
        self.second_button.grid(row=5)

        # Create third level button
        self.third_button = Button(self.start_frame, width=30, height=2,
                                   text=third_level_string, bg="#E51400", fg="#FFFFFF",
                                   font=("Arial", 9, "bold"), command=lambda: self.check_rounds(3))
        self.third_button.grid(row=6, pady=10)


        # Instructions Button
        self.instructions_button = Button(self.start_frame, width=20, height=1,
                                          text="Instructions", bg="#E3C800", fg="#FFFFFF",
                                          font=("Arial", 15, "bold"), command=Instructions)
        self.instructions_button.grid(row=7, pady=1)

        # Statistics Button
        self.statistics_button = Button(self.start_frame, width=20, height=1,
                                          text="Statistics", bg="#1BA1E2", fg="#FFFFFF",
                                          font=("Arial", 15, "bold"), command=Statistics)
        self.statistics_button.grid(row=8, pady=10)

    def check_rounds(self, level):


        """
        Check users have entered 1 or more rounds
        """

        # Get rounds wanted
        rounds_wanted = self.num_rounds_entry.get()

        error = "Please enter a number more than 0"
        has_errors = "no"


        try:
            rounds_wanted = int(rounds_wanted)
            if rounds_wanted > 0:
                self.num_rounds_entry.delete(0, END)
                self.choose_label.config(text=self.label, fg="#000000")
                Play(rounds_wanted, level)
                root.withdraw()


            else:
                has_errors = "yes"
        except ValueError:
            has_errors = "yes"

        # Display error message
        if has_errors == "yes":
            self.choose_label.config(text=error, fg="#990000", font=("Arial", "11", "bold"))
            self.num_rounds_entry.config(bg="#F4CCCC")
            self.num_rounds_entry.delete(0, END)
class Play:
    def __init__(self, how_many, level):
        print(f"{how_many} questions")
        print(f"level: {level}")


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start()
    root.mainloop()
