import csv, random

from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows


class Instructions:
    def __init__(self, partner):
        # Make frame to hold instructions
        self.instructions_box = Toplevel()
        self.start_frame = Frame(self.play_box, bg="#FAD7AC")
        self.start_frame.grid(padx=10, pady=10)

        self.partner = partner

        partner.instructions_button.config(state=DISABLED)

        # Prevent duplicate windows
        self.instructions_box.protocol("WM_DELETE_WINDOW", self.close_stats)



        instructions_labels_list = [
            [" Instructions ", ("Arial", 20, "bold"), "#000000", "#FFFF88"],
            [f"{instructions_text.instructions}", ("Arial", 10, "bold"), None, "#DAE8FC"],


        ]

        start_label_ref = []
        for count, item in enumerate(instructions_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1], fg=item[2], bg=item[3],
                               wraplength=350, justify="left",
                               pady=10, padx=20)

            make_label.grid(row=count)

            start_label_ref.append(make_label)


        # proceed button after user has finished reading instructions
        self.proceed_button = Button(self.start_frame, font=("Arial", 10, "bold"), width=9, text="Proceed",
                                     bg="#FFA500", command=self.close_instructions)
        self.proceed_button.grid(row=2, column=0)

    def close_instructions(self):
        # Close Instructions
        self.play_box.withdraw()


class Statistics:
    def __init__(self, questions_correct, questions_answered, close, partner):
        self.stats_box = Toplevel()
        self.stats_box.title("Game Statistics")

        partner.stats_button.config(state=DISABLED)

        self.start_frame = Frame(self.stats_box, bg="#DAE8FC")
        self.start_frame.grid(padx=10, pady=10)

        self.partner = partner

        # Prevent duplicate windows
        self.stats_box.protocol("WM_DELETE_WINDOW", self.close_stats)



        stats_labels_list = [
            [" Statistics ", ("Arial", "15", "bold"), "#000000", "#87CBE8"],
            [f"Questions Answered: {questions_answered}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            [f"Correct: {questions_correct}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            [f"Incorrect: {questions_answered - questions_correct}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            [f"Close: {close}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            ["Close is within 5 of the answer", ("Arial", "9", "bold"), None, "#DAE8FC"]

        ]

        start_label_ref = []
        for count, item in enumerate(stats_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1], fg=item[2], bg=item[3],
                               wraplength=350, justify="left",
                               pady=10, padx=20)

            make_label.grid(row=count)

            start_label_ref.append(make_label)

    def close_stats(self):
        self.partner.stats_box = None
        self.stats_box.destroy()


class Start:
    def __init__(self):

        self.start_frame = Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        self.instructions_box = None

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


        # Make buttons for start class

        start_buttons_list = [
            [f"{first_level_string}", ("Arial", 9, "bold"), "#FFFFFF", "#82B366", lambda: self.check_rounds(1), 30, 2, 4, 10],
            [f"{second_level_string}", ("Arial", 9, "bold"), "#FFFFFF", "#F0A30A", lambda: self.check_rounds(2), 30, 2, 5, None],
            [f"{third_level_string}", ("Arial", 9, "bold"), "#FFFFFF", "#E51400", lambda: self.check_rounds(3), 30, 2, 6, 10],
            [f"Instructions", ("Arial", 15, "bold"), "#FFFFFF", "#E3C800", self.to_instructions, 20, 1, 7, 1],
        ]

        start_button_ref = []
        for item in start_buttons_list:
            make_button = Button(self.start_frame, text=item[0], font=item[1], fg=item[2], bg=item[3],
                                 command=item[4], width=item[5], height=item[6],
                               wraplength=350, justify="left")

            make_button.grid(row=item[7], pady=item[8])

            start_button_ref.append(make_button)

        self.instructions_button = start_button_ref[3]




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
        Play(rounds_wanted, level)
        root.withdraw()

    def to_instructions(self):
        if not self.instructions_box:
            self.instructions_box = Statistics(self.questions_correct.get(), self.rounds_played.get(),
                                        self.close_answers.get(), self)


class Play:
    def __init__(self, how_many, level):

        self.stats_box = None

        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        # questions correct starts at 0
        self.questions_correct = IntVar()
        self.questions_correct.set(0)

        # number of close answers starts at 0
        self.close_answers = IntVar()
        self.close_answers.set(0)

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
            ["Question # of #", ("Arial", "25", "bold"), "#FAD7AC", 0, None, None],
            ["Whats is x + y", ("Arial", 20, "bold"), '#D5E8D4', 1, None, None],
            [None, ("Arial", 10, "bold"), "#D5E8D4", 3, 30, 2]

        ]

        play_labels_ref = []
        for item in play_labels_list:
            self.make_label = Label(self.start_frame, text=item[0], font=item[1]
                                    , bg=item[2], wraplength=300, justify="left", width=item[4], height=item[5])
            self.make_label.grid(row=item[3], pady=10, padx=10)

            play_labels_ref.append(self.make_label)

        # Retrieve Labels so they can be configured later
        self.heading_label = play_labels_ref[0]
        self.question_label = play_labels_ref[1]
        self.display_area = play_labels_ref[2]

        # so that entry and go button are in the same line without too much gap
        self.entry_area_frame = Frame(self.start_frame, bg="#D5E8D4")
        self.entry_area_frame.grid(row=2, pady=10)

        # Entry box
        self.enter_answer = Entry(self.entry_area_frame, font=("Arial", 22, "bold"), width=10, bg="#F5F5F5")
        self.enter_answer.grid(row=2, column=0, padx=10)

        self.generate_rounds()

        # Go button
        self.go_button = Button(self.entry_area_frame, font=("Arial", 14, "bold"),
                                width=5, text="GO", bg="#60A917", fg="#FFFFFF", command=self.check_answer)
        self.go_button.grid(row=2, column=1, pady=5)


        # List for labels details (text | font | background | foreground | row | command | width | state)
        play_buttons_list = [
            ["Next Round", ("Arial", 15, "bold"), "#F5F5F5",  "#FFFFFF", 4, self.next_round, 10, "disabled"],
            ["Statistics", ("Arial", 15, "bold"), '#1BA1E2', "#FFFFFF", 5, lambda: self.to_stats(), 10, "disabled"],
            ["End Game", ("Arial", 15, "bold"), "#E51400", "#FFFFFF", 6, self.close_play, None, "normal"]

        ]

        play_buttons_ref = []
        for item in play_buttons_list:
            self.make_button = Button(self.start_frame, text=item[0], font=item[1]
                                    , bg=item[2],fg=item[3], wraplength=300, justify="left", width=20,
                                      command=item[5], state=item[7])
            self.make_button.grid(row=item[4], pady=item[6])

            play_buttons_ref.append(self.make_button)

        self.stats_button = play_buttons_ref [1]
        self.next_round_button = play_buttons_ref[0]



    def generate_rounds(self):

        """
        Chooses four colours, works out median for score to beat. Configures
        buttons with chosen colours
        :return:
        """

        if self.rounds_wanted == "infinite":
            rounds_wanted = "infinite"
            self.heading_label.config(text=f"    Question {self.rounds_played.get() + 1}    ")
        else:
            rounds_wanted = self.rounds_wanted.get()
            # update heading and score to beat labels. "Hide" results label
            self.heading_label.config(text=f"Question {self.rounds_played.get() + 1} of {rounds_wanted}")

        # check if we've already played all rounds
        if rounds_wanted != "infinite" and self.rounds_played.get() + 1> rounds_wanted:
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
            first_number = random.randint(1, 12)
            second_number = random.randint(1, 12)

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
            self.display_area.config(bg="#F8CECC", text="Please enter a valid integer")
            return

        if answer == self.result:
            text = " Correct "
            background = "#6D8764"

            # get number of questions correct, increase by 1 and set number of questions correct to the correct value
            questions_correct = self.questions_correct.get()
            questions_correct += 1
            self.questions_correct.set(questions_correct)

        else:
            text = f" Thats incorrect, the answer was {self.result} "
            background = "#E51400"


        if abs(answer - self.result) <= 5 and answer != self.result:
            close = self.close_answers.get()
            close += 1
            self.close_answers.set(close)


        # retrieve number of rounds played, add one to it and configure heading
        rounds_played = self.rounds_played.get()
        rounds_played += 1
        self.rounds_played.set(rounds_played)

        # Enable stats button after 1 question has been answered
        self.stats_button.config(state=NORMAL)

        self.display_area.config(text=text, bg=background)
        self.next_round_button.config(state=NORMAL, fg="#000000")
        self.enter_answer.config(state=DISABLED)
        self.go_button.config(state=DISABLED)

    def close_play(self):
        # reshow root (ie: choose rounds) and end current
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()

    def to_stats(self):
        if not self.stats_box:
            self.stats_box = Statistics(self.questions_correct.get(), self.rounds_played.get(),
                                        self.close_answers.get(), self)


# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start()
    root.mainloop()
