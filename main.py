import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image_shape = "blank_states_img.gif"
screen.addshape(image_shape)
turtle.shape(image_shape)

answer = screen.textinput(title="Guess the state", prompt="What's another state?")

data = pandas.read_csv("50_states.csv")

states = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

data_dict = {"States": states,
             "x_cor": x_cor,
             "y_cor": y_cor}

game_is_on = True

while game_is_on:

    for answer in data_dict["States"]:
        turtle.goto(x_cor[0], y_cor[0])
    else:
        print("Not found")


print(data_dict["States"][answer])

turtle.mainloop()
# Convert the guess to Title letter
# Check if guess is among 50 states
# Write correct guess on to the map
# Use loop to allow user to keep guessing
# Record correct guess into the list
# Keep track of the score