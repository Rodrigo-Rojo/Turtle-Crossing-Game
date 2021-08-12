from turtle import Turtle
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-210, y=250)
        self.level = 1
        self.color("black")
        self.create_scoreboard()
        
    def user_score(self):
        self.clear()
        self.level += 1
        self.create_scoreboard()
        
    def create_scoreboard(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
