from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 240)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def final_score(self):
        self.goto(0, 30)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        if self.l_score > self.r_score:
            self.goto(0, -5)
            self.write("Player 1 is winner.", align=ALIGNMENT, font=FONT)
        else:
            self.goto(0, -5)
            self.write("Player 2 is winner.", align=ALIGNMENT, font=FONT)


