#Peat Image Standard (.pis)

import turtle

name = ""
name = str(input("Enter the name of the .pis file you would like to view: "))

screen = turtle.Screen()
screen.setup(height=1000, width=1000)
screen.bgcolor('black')
screen.title('Square Grid')
screen.tracer(False)
screen.colormode(255)

def read_from_file():
    big_string = ""
    colour_values_f = [""] * 10000
    
    with open(name, "r") as file:
        big_string = file.read()

    for loop in range(10000):
        while big_string[0] != ";":
            colour_values_f[loop] = colour_values_f[loop] + big_string[0]
            big_string = big_string[1:]

        big_string = big_string[1:]

    return colour_values_f

colour_values = read_from_file()
#print(colour_values)

def colour_finder(string_f):
    r_f = ""
    g_f = ""
    b_f = ""
    
    while string_f[0] != ",":
        r_f = r_f + string_f[0]
        string_f = string_f[1:]

    string_f = string_f[1:]

    while string_f[0] != ",":
        g_f = g_f + string_f[0]
        string_f = string_f[1:]

    string_f = string_f[1:]

    b_f = string_f

    r_f = int(r_f)
    g_f = int(g_f)
    b_f = int(b_f)

    return r_f, g_f, b_f

array_of_lines = []

def trace_line(y_level_f, array_of_lines_f, counter_f, colour_values_f):
    line_of_turtles = [""] * 100
    
    x = -500

    for loop in range(100):
        r, g, b = colour_finder(colour_values_f[counter_f])
        #print(r, g, b)
        
        line_of_turtles[loop] = turtle.Turtle()
        line_of_turtles[loop].color(r, g, b)
        line_of_turtles[loop].shape('square')
        line_of_turtles[loop].shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        line_of_turtles[loop].penup()
        line_of_turtles[loop].goto(x, y_level_f)

        x = x + 10
        counter_f = counter_f + 1

    array_of_lines.append(line_of_turtles)

    return array_of_lines_f, counter_f

y_level = 500
counter = 0

for loop in range(100):
    array_of_lines, counter = trace_line(y_level, array_of_lines, counter, colour_values)
    screen.update()

    y_level = y_level - 10
