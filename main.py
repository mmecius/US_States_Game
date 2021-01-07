import turtle
import pandas

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image_shape = "blank_states_img.gif"
# screen.addshape(image_shape)
# turtle.shape(image_shape)
#
# answer = screen.textinput(title="Gues the state", prompt="What's another state?").lower()

data = pandas.read_csv("50_states.csv")

states = data["state"]
x_cor = data["x"]
y_cor = data["y"]

data_dict = {"States": states,
             "x_cor": [x_cor, y_cor]
}

print(data_dict)


# turtle.mainloop()
