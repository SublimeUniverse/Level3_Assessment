import csv, random

from tkinter import *
from functools import partial  # to prevent unwanted windows
import tkinter
import instructions_text
from functools import partial  # to prevent unwanted windows


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

            # Widget | text | font
            [Label," Instructions ", ("Arial", 20, "bold")],
            [Label,f"{instructions_text.instructions}", ("Arial", 10, "bold")],
            [Button, "Proceed", ("Arial", 10, "bold")]


        ]

        # list to hold all the labels
        instructions_widgets_ref = []

        # Create labels and then add them to the reference list
        for count, item in enumerate(instructions_widgets_list):
            make_widget = item[0](self.start_frame, text=item[1], font=item[2],  bg="#FAD7AC",
                               wraplength=350, justify="left",
                               pady=10, padx=20)

            make_widget.grid(row=count)

            instructions_widgets_ref.append(make_widget)

        # Retrieve proceed button to configure background and command
        self.proceed_button = instructions_widgets_ref[2].config(bg="#FFA500", command=self.close_instructions)




    def close_instructions(self):
        # Close Instructions and re-enable the button
        self.partner.instructions_button.config(state=NORMAL)  # Re-enable Instructions button
        self.instructions_box.withdraw()


class Statistics:
    def __init__(self, questions_correct, questions_answered, close, partner):

        # Create stats box window and title
        self.stats_box = Toplevel()
        self.stats_box.title("Game Statistics")

        partner.stats_button.config(state=DISABLED)

        # Create stats frame and place it within stats window
        self.start_frame = Frame(self.stats_box, bg="#DAE8FC")
        self.start_frame.grid(padx=10, pady=10)

        self.partner = partner

        # Prevent duplicate windows
        self.stats_box.protocol("WM_DELETE_WINDOW", self.close_stats)



        stats_labels_list = [
            # Text | Font | foreground | background
            [" Statistics ", ("Arial", "15", "bold"), "#000000", "#87CBE8"],
            [f"Questions Answered: {questions_answered}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            [f"Correct: {questions_correct}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            [f"Incorrect: {questions_answered - questions_correct}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            [f"Close: {close}", ("Arial", "11", "bold"), None, "#DAE8FC"],
            ["Close is within 5 of the answer", ("Arial", "9", "bold"), None, "#DAE8FC"],
            ["Proceed", ("Arial", 10, "bold"), ]

        ]

        start_label_ref = []
        for count, item in enumerate(stats_labels_list):
            make_label = Label(self.start_frame, text=item[0], font=item[1], fg=item[2], bg=item[3],
                               wraplength=350, justify="left",
                               pady=10, padx=20)

            make_label.grid(row=count)

            start_label_ref.append(make_label)

    def close_stats(self):
        # Re-enable stats button when stats window is closed
        self.partner.stats_button.config(state=NORMAL)  # Re-enable Stats button
        self.partner.stats_box = None
        self.stats_box.destroy()


class Start:
    def __init__(self):

        # Make start frame
        self.start_frame = Frame(padx=10, pady=10, bg="#D5E8D4")
        self.start_frame.grid()

        self.instructions_box = None


        # Text Strings for first, second and third levels and error message
        first_level_string = "Level 1(Addition & Subtraction)"
        second_level_string = "Level 2(Multiplication)"
        third_level_string = "Level 3(Division)"
        self.error = "Enter number of rounds or blank for infinite mode"

        # Make buttons for start class

        start_widgets_list = [
            # Widget | Text | Font | foreground | Background | command | width | height | Row | Pady
            [Label, "Welcome to the Maths Game!", ("Arial", "15", "bold"), "#000000", "#87CBE8", None, None, None, 1, 10],
            [Label, self.error, ("Arial", "11", "bold"), None, "#D5E8D4", None, None, None, 2, 10, 350],
            [Entry, None, ("Arial", 20, "bold"), None, None, None, 9, None, 3, None],
            [Button, f"{first_level_string}", ("Arial", 9, "bold"), "#FFFFFF", "#82B366", lambda: self.check_rounds(1), 30, 2, 4, 10],
            [Button, f"{second_level_string}", ("Arial", 9, "bold"), "#FFFFFF", "#F0A30A", lambda: self.check_rounds(2), 30, 2, 5, None],
            [Button, f"{third_level_string}", ("Arial", 9, "bold"), "#FFFFFF", "#E51400", lambda: self.check_rounds(3), 30, 2, 6, 10],
            [Button, f"Instructions", ("Arial", 15, "bold"), "#FFFFFF", "#E3C800", self.to_instructions, 20, 1, 7, 1],
        ]

        start_widget_ref = []
        for item in start_widgets_list:


            make_widget = item[0](self.start_frame, text=item[1], font=item[2], fg=item[3], bg=item[4],
                                 command=item[5], width=item[6], height=item[7],
                                justify="left")

            make_widget.grid(row=item[8], pady=item[9])

            start_widget_ref.append(make_widget)


        # Extract choice label so it can be change if theres an error in users input
        self.choose_label = start_widget_ref[1]
        self.num_rounds_entry = start_widget_ref[2]
        self.instructions_button = start_widget_ref[3]


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

        # number of close answers - starts at 0
        self.close_answers = IntVar()
        self.close_answers.set(0)


        # If user doesnt choose infinite, set rounds wanted to how rounds user wants
        if how_many != "infinite":
            self.rounds_wanted = IntVar()
            self.rounds_wanted.set(how_many)
        else:
            self.rounds_wanted = "infinite"

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






        # List for labels details (Widget | Frame | text | font | background |foreground | row | command | width | pady | state | column)
        play_widget_list = [
            [Label,self.start_frame, "Question # of #", ("Arial", "25", "bold"), "#FAD7AC", None, 0, None, None, 10, None, None, None],
            [Label,self.start_frame,"Whats is x + y", ("Arial", 20, "bold"), '#D5E8D4', None, 1, None, None, 10, None, None, None],
            [Label, self.start_frame, None, ("Arial", 10, "bold"), "#D5E8D4", None, 3, None, 30, 10, None, None, None],
            [Entry, self.entry_area_frame, None,("Arial", 22, "bold"), "#F5F5F5", None, 2, None, 10, None, None, 0],
            [Button,self.entry_area_frame, "GO", ("Arial", 14, "bold"), "#60A917", "#FFFFFF",2, self.check_answer, 5, 5,"normal", 1],
            [Button,self.start_frame,"Next Round", ("Arial", 15, "bold"), "#F5F5F5",  "#FFFFFF", 4, self.next_round, 20,10 ,"disabled", None],
            [Button,self.start_frame,"Statistics", ("Arial", 15, "bold"), '#1BA1E2', "#FFFFFF", 5, lambda: self.to_stats(), 20,10, "disabled", None],
            [Button,self.start_frame,"End Game", ("Arial", 15, "bold"), "#E51400", "#FFFFFF", 6, self.close_play, 20, None, "normal", None]

        ]

        play_widget_ref = []
        for item in play_widget_list:
            if item[0] == Entry:
                self.make_widget = Entry(item[1], font=item[3], bg=item[4], width=item[8])

            else:

                self.make_widget = item[0](item[1], text=item[2], font=item[3]
                                        , bg=item[4],fg=item[5], wraplength=300, justify="left", width=item[8],
                                          command=item[7], state=item[10])
            self.make_widget.grid(row=item[6], pady=item[9], column=item[11], padx=5)
            play_widget_ref.append(self.make_widget)


        self.heading_label = play_widget_ref[0]
        self.question_label = play_widget_ref[1]
        self.display_area = play_widget_ref[2]
        self.enter_answer = play_widget_ref[3]
        self.go_button = play_widget_ref[4]
        self.next_round_button = play_widget_ref[5]
        self.stats_button = play_widget_ref [6]
        self.end_game_button = play_widget_ref[7]


        self.generate_rounds()





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
