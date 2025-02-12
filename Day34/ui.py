from tkinter import *
from quiz_brain import QuizBrain

WHITE = "#FFFFFF"
THEME_COLOR = "#375362"
TICK_PATH = "Day34/images/true.png"
CROSS_PATH = "Day34/images/false.png"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = 0 

        self.tickimage = PhotoImage(file = TICK_PATH)
        self.tick_button = Button(image=self.tickimage, highlightthickness=0)
        self.tick_button.grid(row=2, column=0)
        self.crossimage = PhotoImage(file = CROSS_PATH)
        self.cross_button = Button(image=self.crossimage, highlightthickness=0)
        self.cross_button.grid(row=2, column=1)
        

        self.score_label = Label(text= f"Score: {self.score}", bg=THEME_COLOR, fg = WHITE)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150,125,width=280,text = "Some", fill = THEME_COLOR, font = ("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan =2, pady=50)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)