from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24 , 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_right = 0
        self.score_left = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(200,250)
        self.write(f"Score: {self.score_right}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(-200,250)
        self.write(f"Score: {self.score_left}", move= False, align = ALIGNMENT, font = FONT)
        #self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Score: {self.score_left}", move= False, align = ALIGNMENT, font = FONT)
        self.goto(200,250)
        self.write(f"Score: {self.score_right}", move= False, align = ALIGNMENT, font = FONT)

    def increase_score_right(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_left(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()

    def end_game(self,game_is_on):
        if self.score_left == 3:
            self.write(f"Left player wins! Score: {self.score_left}", move=False, align=ALIGNMENT, font=FONT)
            game_is_on = False
            return game_is_on
        elif self.score_right == 3:
            self.write(f"Right player wins! Score: {self.score_right}", move=False, align=ALIGNMENT, font=FONT)
            game_is_on = False
            return game_is_on
