import csv, random

from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows


class Instructions:
    def __init__(self):
        # Make frame to hold instructions
        self.play_box = Toplevel()
        self.start_frame = Frame(self.play_box, bg="#FAD7AC")
        self.start_frame.grid(padx=10, pady=10)

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
                                     bg="#FFA500", command=self.close_instructions)
        self.proceed_button.grid(row=2, column=0)

    def close_instructions(self):
        # Close Instructions
        self.play_box.withdraw()


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
        self.label = "Enter number of rounds or blank for infinite mode"

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
                                        font=("Arial", 15, "bold"), command=Statistics, state=DISABLED)
        self.statistics_button.grid(row=8, pady=10)

    def check_rounds(self, level):

        """
        Check users have entered 1 or more rounds
        """

        # Get rounds wanted
        rounds_input = self.num_rounds_entry.get().strip()

        if rounds_input == "":
            rounds_wanted = "infinite"
        else:
            try:
                rounds_wanted = int(rounds_input)
                if rounds_wanted <= 0:
                    raise ValueError
            except ValueError:
                self.choose_label.config(fg="red")
                return

        self.num_rounds_entry.delete(0, END)
        self.choose_label.config(text=self.label, fg="#000000")
        Play(rounds_wanted, level)
        root.withdraw()


class Play:
    def __init__(self, how_many, level):

        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)


        if how_many != "infinite":
            self.rounds_wanted = IntVar()
            self.rounds_wanted.set(how_many)
        else:
            self.rounds_wanted = "infinite"

        self.level = IntVar()
        self.level.set(level)

        self.play_box = Toplevel()

        # Initial start frame
        self.start_frame = Frame(self.play_box, padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        # List for labels details (text | font | background | row)
        play_labels_list = [
            ["Question # of #", ("Arial", "25", "bold"), "#FAD7AC", 0],
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
        self.go_button = Button(self.entry_area_frame, font=("Arial", 14, "bold"),
                                width=5 , text="GO", bg="#60A917", fg="#FFFFFF", command=self.check_answer)
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
                                   width=20, text="Statistics", bg="#1BA1E2", fg="#FFFFFF", state=DISABLED)
        self.stats_button.grid(row=5, pady=10)

        # End Game button
        self.end_game_button = Button(self.start_frame, font=("Arial", 15, "bold"),
                                      width=20, text="End Game", bg="#E51400", fg="#FFFFFF", command=self.close_play)
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


        if self.rounds_wanted == "infinite":
            rounds_wanted = "infinite"
            self.heading_label.config(text=f"    Question {rounds_played}    ")
        else:
            rounds_wanted = self.rounds_wanted.get()
            # update heading and score to beat labels. "Hide" results label
            self.heading_label.config(text=f"Question {rounds_played} of {rounds_wanted}")


        # Enable stats button if more than 1 round is played
        if rounds_played > 1:
            self.stats_button.config(state=NORMAL)


        # check if we've already played all rounds
        if rounds_wanted != "infinite" and rounds_played > rounds_wanted:
            self.heading_label.config(text=" End Of Game ", bg="#0050EF", fg="#FFFFFF")
            self.next_round_button.destroy()
            self.display_area.config(text="You may check your stats or play again", bg="#DAE8FC", fg="#000000")
            self.end_game_button.config(text="Play Again", bg="#60A917")
            self.entry_area_frame.destroy()
            self.question_label.config(text="")
            self.enter_answer.destroy()
            self.go_button.destroy()

            return

        level = self.level.get()

        # Generate questions
        operations = ["+", "-"]

        # Numbers for addition and subtraction
        first_number = random.randint(0, 30)
        second_number = random.randint(0, 30)

        # Check if user is playing level 2 or 3
        if level != 1:
            # Numbers for multiplication and division
            first_number = random.randint(1,12)
            second_number = random.randint(1,12)


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
            operation = "÷"
            answer = first_number * second_number
            self.result = first_number
            first_number = answer


        self.question_label.config(text=f"What is {first_number} {operation} {second_number}")
        print(self.rounds_played, self.rounds_wanted)



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


    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()






# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start()
    root.mainloop()
