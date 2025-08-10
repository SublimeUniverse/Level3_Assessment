import csv, random

from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows

# Num check function used to validate numbers in the program
def num_check(rounds_wanted, entry_box, limit):
    """
    Check users have entered 1 or more rounds
    """
    rounds_wanted = rounds_wanted.get()

    if rounds_wanted == "":
        return "infinite"

    else:
        try:
            rounds_wanted = int(rounds_wanted)

            if rounds_wanted < limit:
                raise ValueError
            return rounds_wanted  # Valid input
        except ValueError:
            entry_box.delete(0, END)
            return None




class Instructions:
    def __init__(self, partner):
        # Window to hold instructions
        self.instructions_box = Toplevel()

        # Frame placed within window for instructions
        self.start_frame = Frame(self.instructions_box, bg="#FAD7AC")
        self.start_frame.grid(padx=10, pady=10)

        self.partner = partner

        # disable instructions button while window is open
        partner.instructions_button.config(state=DISABLED)

        # Prevent duplicate windows
        self.instructions_box.protocol("WM_DELETE_WINDOW", self.close_instructions)

        # All instructions widgets
        instructions_widgets_list = [

            # Widget | text | font | command
            [Label, " Instructions ", ("Arial", 22, "bold")],
            [Label, f"{instructions_text.instructions}", ("Arial", 10, "bold")],
            [Button, "Proceed", ("Arial", 10, "bold")]

        ]

        # list to hold all the labels
        instructions_widgets_ref = []

        # Create labels and then add them to the reference list
        for count, item in enumerate(instructions_widgets_list):
            make_widget = item[0](self.start_frame, text=item[1], font=item[2], bg="#FAD7AC",
                                  justify="left", padx=20, pady=10)

            make_widget.grid(row=count)

            instructions_widgets_ref.append(make_widget)

        # Retrieve proceed button to configure background and command
        self.proceed_button = instructions_widgets_ref[2].config(bg="#FFA500", command=self.close_instructions)

    def close_instructions(self):
        '''###
        Once instructions is close, enable instructions button,
        destroy instructions window and allow to be reopened
        '''

        self.partner.instructions_button.config(state=NORMAL)
        self.instructions_box.destroy()
        self.partner.instructions_box = None


class Statistics:
    def __init__(self, questions_correct, questions_answered, partner):
        # Create stats box window and title
        self.stats_box = Toplevel()
        self.stats_box.title("Game Statistics")

        self.partner = partner

        # Prevent duplicate windows
        self.stats_box.protocol("WM_DELETE_WINDOW", self.close_stats)

        # Disable stats button while stats is open
        partner.stats_button.config(state=DISABLED)

        # Create stats frame and place it within stats window
        self.stats_frame = Frame(self.stats_box, bg="#DAE8FC")
        self.stats_frame.grid(padx=10, pady=10)

        # Calculate percentages
        percentage_correct = self.round_to_2dp((questions_correct / questions_answered) * 100)

        stats_widget_list = [

            # Text | Font | background
            ["    Statistics    ", ("Arial", "15", "bold"), "#87CBE8"],
            [f"Questions Answered: {questions_answered}", ("Arial", 11, "bold"), "#DAE8FC"],
            [f"Correct: {questions_correct}", ("Arial", 11, "bold"), "#DAE8FC"],
            [f"Incorrect: {questions_answered - questions_correct}", ("Arial", 11, "bold"), "#DAE8FC"],
            [f"You got {percentage_correct}% right", ("Arial", 11, "bold"), "#DAE8FC"],
            ["Proceed", ("Arial", 10, "bold"), "#0050EF"]
        ]

        stats_label_ref = []
        for count, item in enumerate(stats_widget_list):
            # Widget type is label except for proceed button
            widget_type = Label
            if item[0] == "Proceed":
                widget_type = Button


            make_widget = widget_type(self.stats_frame, text=item[0], font=item[1], bg=item[2],
                                      wraplength=350, justify="left",
                                      pady=10, padx=20)

            make_widget.grid(row=count)

            stats_label_ref.append(make_widget)

        self.proceed_stats_button = stats_label_ref[5]
        self.proceed_stats_button.config(command=self.close_stats, fg="#FFFFFF")

    def close_stats(self):
        # Re-enable stats button when stats window is closed
        self.partner.stats_button.config(state=NORMAL)  # Re-enable Stats button
        self.partner.stats_box = None
        self.stats_box.destroy()



    def round_to_2dp(self, value):
        return round(value, 2)


class Start:
    def __init__(self):

        # Make start frame
        self.start_frame = Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        self.instructions_box = None

        # Text Strings for first, second and third levels and information label
        first_level_string = "Level 1(Addition & Subtraction)"
        second_level_string = "Level 2(Multiplication)"
        third_level_string = "Level 3(Division)"
        self.info_label = "Enter number of rounds or leave blank for infinite mode"

        # Make buttons for start class

        start_widgets_list = [
            # Widget | Text | Font | Background | command | padx | height | Row | Pady
            [Label, "      Welcome to the Maths Game!      ", ("Arial", 23, "bold"), "#87CBE8", None, None, 2, 1, 10],
            [Label, self.info_label, ("Arial", 13, "bold"), "#D5E8D4", None, 30, None, 2, 10, 350],
            [Button, f"{first_level_string}", ("Consolas", 11, "bold"), "#82B366", lambda: self.validate_rounds(1),
             28, 2, 4, 10],
            [Button, f"{second_level_string}", ("Consolas", 11, "bold"), "#F0A30A", lambda: self.validate_rounds(2),
             60, 2, 5, None],
            [Button, f"{third_level_string}", ("Consolas", 11, "bold"), "#E51400", lambda: self.validate_rounds(3),
             83, 2, 6, 10],
            [Label, "Need Instructions?", ("Arial", 10, "bold"), "#D5E8D4", None, None, None, 7, 15],
            [Button, f"Instructions", ("Courier New", 19, "bold"), "#E3C800", self.to_instructions, 63, 1, 8, 0],
        ]

        start_widget_ref = []
        for item in start_widgets_list:
            # Set foreground white, if widget is label, set foreground black
            foreground = "#FFFFFF"
            if item[0] == Label:
                foreground = None

            make_widget = item[0](self.start_frame, text=item[1], font=item[2], bg=item[3],
                                  command=item[4], fg=foreground, padx=item[5], height=item[6])

            make_widget.grid(row=item[7], pady=item[8])

            start_widget_ref.append(make_widget)

        # Make entry box for number of rounds
        self.num_rounds_entry = Entry(self.start_frame, font=("Arial", 20, "bold"), width=9)
        self.num_rounds_entry.grid(row=3, column=0)

        # Extract choose label so it can be change if theres an error in users input
        # Extract instructions button so we can enable / disable
        self.info_label = start_widget_ref[1]
        self.instructions_button = start_widget_ref[6]

    def validate_rounds(self, level):

        """
        Validates user had entered a valid number of rounds using num_check
        Proceeds to play and withdraws if input is valid
        """

        rounds_wanted = num_check(self.num_rounds_entry, self.num_rounds_entry, 1)

        # if rounds wanted is none, then error has occured so dont let rounds wanted pass
        if rounds_wanted is None:
            self.info_label.config(fg="red")
            return

        Play(rounds_wanted, level)
        root.withdraw()

    def to_instructions(self):
        if not self.instructions_box:
            self.instructions_box = Instructions(self)


class Play:
    def __init__(self, how_many, level):

        # Initially disable stats box
        self.stats_box = None

        # rounds played - start with zero
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        # questions correct - starts with 0
        self.questions_correct = IntVar()
        self.questions_correct.set(0)

        # If user doesnt choose infinite, set rounds wanted to how rounds user wants
        if how_many != "infinite":
            self.rounds_wanted = IntVar()
            self.rounds_wanted.set(how_many)
        else:
            self.rounds_wanted = None

        # Get level
        self.level = IntVar()
        self.level.set(level)

        # Make window for play class
        self.play_box = Toplevel()

        # Initial start frame
        self.start_frame = Frame(self.play_box, padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        # so that entry and go button are in the same line without too much gap
        self.entry_area_frame = Frame(self.start_frame, bg="#D5E8D4")
        self.entry_area_frame.grid(row=2, pady=10)

        # List for play widgets (Widget | Frame | text | font | background |row | command | width | pady)
        play_widget_list = [
            [Label, self.start_frame, "Question # of #", ("Arial", "25", "bold"), "#FAD7AC", 0, None, None, 10, None],
            [Label, self.start_frame, "Whats is x + y", ("Arial", 20, "bold"), '#D5E8D4', 1, None, None, 10, None],
            [Label, self.start_frame, None, ("Arial", 10, "bold"), "#D5E8D4", 3, None, 30, 10, None],
            [Button, self.entry_area_frame, "GO", ("Arial", 14, "bold"), "#60A917", 2, self.check_answer, 5, 5],
            [Button, self.start_frame, "Next Round", ("Arial", 15, "bold"), "#F5F5F5", 4, self.next_round, 20, 10],
            [Button, self.start_frame, "Statistics", ("Arial", 15, "bold"), '#1BA1E2', 5, lambda: self.to_stats(), 20,
             10],
            [Button, self.start_frame, "End Game", ("Arial", 15, "bold"), "#E51400", 6, self.end_game_screen, 20, None]

        ]

        play_widget_ref = []
        for item in play_widget_list:
            # If not a button set foreground colour to blacl / default
            fg_color = "#FFFFFF" if item[0] == Button else None

            # Make widget, add to grid and add to play_widget_ref for reference and accessing later
            self.make_widget = item[0](item[1], text=item[2], font=item[3]
                                       , bg=item[4], fg=fg_color, wraplength=300, justify="left", width=item[7],
                                       command=item[6])
            self.make_widget.grid(row=item[5], pady=item[8], padx=5)
            play_widget_ref.append(self.make_widget)

        # Create entry box to get answers
        self.enter_answer = Entry(self.entry_area_frame, font=("Arial", 22, "bold"), width=10, bg="#F5F5F5")
        self.enter_answer.grid(row=2, column=0, padx=10)

        # Retrieve all labels and buttons so we can configure later
        self.heading_label = play_widget_ref[0]
        self.question_label = play_widget_ref[1]
        self.display_area = play_widget_ref[2]
        self.display_area.config(height=2)
        self.go_button = play_widget_ref[3]
        self.go_button.grid(column=1, pady=5)
        self.next_round_button = play_widget_ref[4]
        self.next_round_button.config(state=DISABLED)
        self.stats_button = play_widget_ref[5]
        self.stats_button.config(state=DISABLED)
        self.end_game_button = play_widget_ref[6]

        # Start generating rounds
        self.generate_rounds()

    def generate_rounds(self):

        """
        Generates rounds for infinite and finite modes according to level.
        :return:
        """
        # Check whether user wants infinite rounds, otherwise get number of rounds
        # Increase number of rounds played by 1 as it starts at 0 and first question starts with 'Question 1 of ...'
        if self.rounds_wanted is None:
            self.heading_label.config(text=f"    Question {self.rounds_played.get() + 1}    ")
        else:

            # update heading label if not infinite
            self.heading_label.config(text=f"  Question {self.rounds_played.get() + 1} of {self.rounds_wanted.get()}  ")


        # check if we've already played all rounds
        if self.rounds_wanted is not None and self.rounds_played.get() + 1 > self.rounds_wanted.get():

            # Invoke end game screen
            self.end_game_screen()

            return

        # Get level chosen
        level = self.level.get()

        # Operations for level 1 to be chosen randomly
        operations_level_i = ["+", "-"]

        # Numbers for multiplication and division
        first_number = random.randint(1, 12)
        second_number = random.randint(1, 12)

        # Check which level user is playing and accordingly generate question & answer
        if level == 1:

            # Numbers for addition and subtraction
            first_number = random.randint(0, 30)
            second_number = random.randint(0, 30)

            operation = random.choice(operations_level_i)

            # Checks whether operation is plus or minus and generates accordingly
            if operation == "+":
                self.result = first_number + second_number
            else:
                if operation == "-":
                    self.result = abs(first_number - second_number)
                    if second_number >= first_number:
                        self.question_label.config(text=f"What is {second_number} {operation} {first_number}")
                        return

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

        '''### Proceeds to the next round by invoking generate
                round functions and configuring widgets back to the
                original attributes'''

        self.generate_rounds()
        self.enter_answer.configure(state="normal")
        self.enter_answer.delete(0, END)
        self.go_button.config(state=NORMAL)
        self.display_area.config(text="", bg="#D5E8D4")
        self.next_round_button.config(state=DISABLED)


    def end_game_screen(self):

        '''### Configure heading label, destroys next rounds button, configures display area,
        configured end game button to play again button, destroy entry frame, enter answer box and go button.
        '''

        self.heading_label.config(text=" End Of Game ", bg="#0050EF", fg="#FFFFFF")
        self.next_round_button.destroy()
        self.display_area.config(text="You may check your stats or play again", bg="#DAE8FC", fg="#000000")
        self.end_game_button.config(text="Play Again", bg="#60A917", command=self.close_play)
        self.entry_area_frame.destroy()
        self.question_label.config(text="")
        self.enter_answer.destroy()
        self.go_button.destroy()


    def check_answer(self):

        answer = num_check(self.enter_answer, self.enter_answer, 0)




        # Check if answer is correct, display correct and set green background
        if answer == self.result:
            text = " Correct "
            background = "#6D8764"
            try_again = False

            # get number of questions correct, increase by 1 and set number of questions correct to the correct value
            questions_correct = self.questions_correct.get()
            questions_correct += 1
            self.questions_correct.set(questions_correct)

        elif answer is None:
            # If answer is wrong, display incorrect and set red background
            text = "Please enter a valid integer"
            background = "#F8CECC"
            try_again = True

        else:
            # If answer has error dont let it pass
            text = f" Thats incorrect, the answer was {self.result} "
            background = "#E51400"
            try_again = False


        self.display_area.config(text=text, bg=background)

        if try_again:
            self.enter_answer.delete(0, END)
            return

        # retrieve number of rounds played, add one to it and configure heading
        rounds_played = self.rounds_played.get()
        rounds_played += 1
        self.rounds_played.set(rounds_played)

        # Enable stats button after 1 question has been answered
        self.stats_button.config(state=NORMAL)

        # Makes display area display correct or incorrect, adjusts background, enables next round button
        # and disables enter_answer entry and go button.
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
            self.stats_box = Statistics(self.questions_correct.get(), self.rounds_played.get(), self)


# Main Routine

if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz")
    Start()
    root.mainloop()
