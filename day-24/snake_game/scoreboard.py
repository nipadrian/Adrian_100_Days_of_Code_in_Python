from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24 , 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.high_score = 0
        with open("data.txt", mode = "r") as file:
            high_score = file.read()
        self.high_score = high_score
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move= False, align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move= False, align = ALIGNMENT, font = FONT)

    def reset_scoreboard(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

