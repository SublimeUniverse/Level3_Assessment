import csv, random
from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text

class Instructions:
    def __init__(self):

        # Make frame to hold instructions
        self.start_frame = tkinter.Frame(padx=10, pady=10, bg="#FAD7AC")
        self.start_frame.grid()

        # Instructions heading
        self.instruction_heading = Label(self.start_frame, text="  Instructions  ",
                                         font=("Arial", 20, "bold"), bg="#FFFF88")
        self.instruction_heading.grid(row=0)

        # display instructions text
        self.instruction_text = Label(self.start_frame, text=instructions_text.instructions,
                                      font=("Arial", 10, "bold"), width=50)
        self.instruction_text.grid(row=1, pady = 10)


        # proceed button after user has finished reading instructions
        self.proceed_button = Button(self.start_frame, font=("Arial", 10, "bold"), width=9, text="Proceed",
                                     bg="#FFA500", command=self.proceed)
        self.proceed_button.grid(row=2, column=0)


    def proceed(self):
        Start()
        root.withdraw()



class Start:
    def __init__(self):
        self.play_box = Toplevel()
        self.start_frame = Frame(self.play_box, padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()


        self.num_rounds_entry = Entry(self.start_frame, font=("Arial", 20, "bold"), width=9)

        self.num_rounds_entry.grid(row=3, column=0)

        # Text Strings
        first_level_string = "Level 1(Addition & Subtraction)"
        second_level_string = "Level 2(Multiplication)"
        third_level_string = "Level 3(Division)"

        start_labels_list = [
            ["Welcome to the Maths Game!", ("Arial", "15", "bold"), "#000000", "#87CBE8"],
            ["Please enter number of rounds", ("Arial", "11", "bold"), None, "#D5E8D4"]

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
                                   fg="#FFFFFF", font=("Arial", 9, "bold"))
        self.first_button.grid(row=4, pady=10)

        # Create second button
        self.second_button = Button(self.start_frame, width=30, height=2,
                                    text=second_level_string, bg="#F0A30A", fg="#FFFFFF",
                                    font=("Arial", 9, "bold"))
        self.second_button.grid(row=5)

        # Create third button
        self.third_button = Button(self.start_frame, width=30, height=2,
                                   text=third_level_string, bg="#E51400", fg="#FFFFFF",
                                   font=("Arial", 9, "bold"))
        self.third_button.grid(row=6, pady=10)

    




# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Instructions()
    root.mainloop()
