"""
Author: Franco Nepomuceno
Date: November 21, 2023
Description: Practicing Turtle module with OOP
"""



from turtle import Turtle, Screen

ninja_turtle = Turtle()
ninja_turtle.shape("turtle")
ninja_turtle.color("blue")

# Below code is to make the screen stay and exit manually
screen = Screen()
screen.exitonclick()
