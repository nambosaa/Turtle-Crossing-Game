from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, 250)
        self.score = 0
        self._write(f"Your score is: {self.score}.", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self._write(f"Your score is: {self.score}.", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)



