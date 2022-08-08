from tkinter import *
import data
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=275, height=600, padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg = "white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.question_text = self.canvas.create_text((150, 125), width=280, text="Text", fill=THEME_COLOR,
                                                     font=("Arial", 12, "italic"))

        self.true_img = PhotoImage(file="images/images_true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.false_response)
        self.true_button.grid(column=0, row=2)

        self.false_img = PhotoImage(file="images/images_false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.true_response)
        self.false_button.grid(column=1, row=2)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=1, sticky=N)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_response(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_response(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
