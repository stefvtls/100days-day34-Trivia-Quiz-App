import tkinter.messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.minsize(height=400, width=300)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreboard = tkinter.Label(text=f"Score: {0}", fg="white", font=("Arial", 12, "normal"), bg=THEME_COLOR)
        self.scoreboard.grid(row=0, column=1, pady=(20,0))

        self.box = tkinter.Canvas(width=300, height=250, bg="white", highlightthickness=5)
        self.textbox = self.box.create_text(150, 125, text="question", font=FONT, width= 230, fill=THEME_COLOR)
        self.box.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_button_image = tkinter.PhotoImage(file="images/true.png")
        self.wrong_button_image = tkinter.PhotoImage(file="images/false.png")
        self.right_button = tkinter.Button(image=self.right_button_image, highlightthickness=0, command=self.right)
        self.wrong_button = tkinter.Button(image=self.wrong_button_image, highlightthickness=0, command=self.wrong)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.box.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.box.itemconfig(self.textbox, text=q_text)
        else:
            self.box.itemconfig(self.textbox, text="end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right(self):
        self.check_answer("True")

    def wrong(self):
        self.check_answer("False")

    def check_answer(self, answer):
        if self.quiz.check_answer(answer):
            self.box.config(bg="green")
            self.scoreboard.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        else:
            self.box.config(bg="red")
            self.scoreboard.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(500, self.next_question)
