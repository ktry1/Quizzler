import tkinter, sys
from tkinter import messagebox
THEME_COLOR = "#375362"
from data import question
from quiz_brain import new_question


class Ui:
    def __init__(self):
        self.score=0
        with open("Highscore.txt") as file:
            self.high_score=int(file.read())
        self.window=tkinter.Tk()
        self.window.iconbitmap('Images/favicon.ico')
        self.window.title("Quizzler")
        self.window.config(bg="#375362",padx=30,pady=30)
        self.true_image= tkinter.PhotoImage(file="./images/true.png")
        self.false_image=tkinter.PhotoImage(file="./images/false.png")

        self.canvas= tkinter.Canvas(height=400,width=400)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.yes_button = tkinter.Button(command=self.answer_true)
        self.yes_button.config(image=self.true_image,borderwidth=0,highlightthickness = 0)
        self.yes_button.grid(row=2,column=0)
        self.no_button = tkinter.Button(command=self.answer_false)
        self.no_button.config(image= self.false_image,borderwidth=0,highlightthickness = 0)
        self.no_button.grid(row=2, column=1)

        self.score_label = tkinter.Label(text="Score: 0",bg="#375362",fg="white", font=("Courier New",16,"bold"))
        self.score_label.grid(row=0,column=0)


        self.highscore_label = tkinter.Label(text=f"High Score:{self.high_score}",bg= "#375362",fg="white", font=("Courier New",16,"bold"))
        self.highscore_label.grid(row=0, column=1)

        self.screen_question = self.canvas.create_text(200, 200, text=question.text, width=400, font=("Courier New", 16, "normal"))

    def answer_true(self):
        answer = "True"
        if answer==question.answer:
            self.score+=1
            self.score_label.config(text=f"Score:{self.score}")
            if self.score >= self.high_score:
                self.high_score = self.score
                self.highscore_label.config(text=f"High Score: {self.high_score}")
            new_question()
            self.canvas.itemconfig(self.screen_question, text=question.text)
        else:
            if self.score>=self.high_score:
                with open("Highscore.txt", mode="w") as file:
                    file.write(str(self.score))
            tkinter.messagebox.showinfo(title="GAME OVER", message=f"Your High Score is {self.high_score}")
            sys.exit()

    def answer_false(self):
        answer = "False"
        if answer == question.answer:
            self.score += 1
            self.score_label.config(text=f"Score:{self.score}")
            if self.score >= self.high_score:
                self.high_score= self.score
                self.highscore_label.config(text=f"High Score: {self.high_score}")
            new_question()
            self.canvas.itemconfig(self.screen_question, text=question.text)
        else:
            if self.score>=self.high_score:
                with open("Highscore.txt", mode="w") as file:
                    file.write(str(self.score))
            tkinter.messagebox.showinfo(title="GAME OVER", message=f"Your High Score is {self.high_score}")
            sys.exit()