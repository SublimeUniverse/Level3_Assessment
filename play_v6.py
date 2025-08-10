import csv, random
from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows
import random


class Play:
    def __init__(self, how_many, level):

        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        self.level = IntVar()
        self.level = 1

        # Initial start frame
        self.start_frame = Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        # List for labels details (text | font | background | row)
        play_labels_list = [
            ["Question # of #", ("Arial", "25", "bold"), "#F5F5F5", 0],
            ["Whats is x + y", ("Arial", 20, "bold"), '#D5E8D4', 1],

        ]

        play_labels_ref = []
        for item in play_labels_list:
            self.make_label = Label(self.start_frame, text=item[0], font=item[1]
                                    , bg=item[2], wraplength=300, justify="left")
            self.make_label.grid(row=item[3], pady=10, padx=10)

            play_labels_ref.append(self.make_label)

        # Retrieve Labels so they can be configured later
        self.heading_label = play_labels_ref[0]
        self.question_label = play_labels_ref[1]

        # so that entry and go button are in the same line without too much gap
        self.entry_area_frame = Frame(self.start_frame, bg="#D5E8D4")
        self.entry_area_frame.grid(row=2, pady=10)

        # Entry box
        self.enter_answer = Entry(self.entry_area_frame, font=("Arial", 22, "bold"), width=10, bg="#F5F5F5")
        self.enter_answer.grid(row=2, column=0, padx=10)

        self.generate_rounds()
        # Go button
        self.go_button = Button(self.entry_area_frame, font=("Arial", 10, "bold"),
                                width=7, height=2, text="GO", bg="#60A917", fg="#FFFFFF", command=self.check_answer)
        self.go_button.grid(row=2, column=1, pady=5)

        # Display right or wrong
        self.display_area = Label(self.start_frame, font=("Arial", 10, "bold"), width=30, height=2,
                                  bg="#D5E8D4", fg="#FFFFFF")
        self.display_area.grid(row=3, column=0, columnspan=2)

        # Next round button
        self.next_round_button = Button(self.start_frame, font=("Arial", 15, "bold"),
                                        width=20, text="Next Round", bg="#F5F5F5", fg="#FFFFFF",
                                        state=DISABLED, command=self.next_round)
        self.next_round_button.grid(row=4, pady=10)

        # Stats button
        self.stats_button = Button(self.start_frame, font=("Arial", 15, "bold"),
                                   width=20, text="Statistics", bg="#1BA1E2", fg="#FFFFFF")
        self.stats_button.grid(row=5, pady=10)

        # End Game button
        self.end_game_button = Button(self.start_frame, font=("Arial", 15, "bold"),
                                      width=20, text="End Game", bg="#E51400", fg="#FFFFFF")
        self.end_game_button.grid(row=6)

    def generate_rounds(self):

        """
        Chooses four colours, works out median for score to beat. Configures
        buttons with chosen colours
        :return:
        """

        # retrieve number of rounds played, add one to it and configure heading
        rounds_played = self.rounds_played.get()
        rounds_played += 1
        self.rounds_played.set(rounds_played)

        rounds_wanted = self.rounds_wanted.get()
        level = 1

        # Generate questions
        operations = ["+", "-"]

        first_number = random.randint(0, 30)
        second_number = random.randint(0, 30)

        if level == 1:
            operation = random.choice(operations)

            if operation == "+":
                self.result = first_number + second_number
            else:
                if operation == "-":
                    self.result = first_number - second_number

        elif level == 2:
            operation = "x"
            self.result = first_number * second_number

        else:
            operation = "/"
            self.result = first_number / second_number
        # update heading and score to beat labels. "Hide" results label
        self.heading_label.config(text=f"Question {rounds_played} of {rounds_wanted}")

        self.question_label.config(text=f"What is {first_number} {operation} {second_number}")
        print(self.rounds_played, self.rounds_wanted)

        if rounds_played > rounds_wanted:
            print("game over")
            self.next_round_button.config(state=DISABLED)
            root.withdraw()

    def next_round(self):
        self.generate_rounds()
        self.enter_answer.config(state=NORMAL)
        self.enter_answer.delete(0, END)
        self.go_button.config(state=NORMAL)
        self.display_area.config(text="", bg="#D5E8D4")
        self.next_round_button.config(state=DISABLED)

    def check_answer(self):

        # Retrieve answer inputted
        answer_str = self.enter_answer.get()

        try:
            answer = int(answer_str)
        except ValueError:
            return

        if answer == self.result:
            text = " Correct "
            background = "#6D8764"

        else:
            text = f" Thats incorrect, the answer was {self.result} "
            background = "#E51400"

        self.display_area.config(text=text, bg=background)
        self.next_round_button.config(state=NORMAL, fg="#000000")
        self.enter_answer.config(state=DISABLED)
        self.go_button.config(state=DISABLED)


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Play(2, 2)
    root.mainloop()
