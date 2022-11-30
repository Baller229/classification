import math
import random
import time
import numpy as np
import matplotlib.pyplot as chart

# ======================================================================================
# ARRAYS, NUMBER OF POINTS, KNN...
knn = 1
POINTS_COUNT = 500
r = 0
g = 0
b = 0
p = 0
red_count = 0
blue_count = 0
green_count = 0
purple_count = 0
x_coordinate = 0
y_coordinate = 0
last_assigned = ""
assigned = 0
fault = 0
number_of_training_data = 20

final_data = []
training_data = []
sorted_training_data = []
RED_ARR = []
GREEN_ARR = []
BLUE_ARR = []
PURPLE_ARR = []
RED_ARR_MISSPLACED = []
GREEN_ARR_MISSPLACED = []
BLUE_ARR_MISSPLACED = []
PURPLE_ARR_MISSPLACED = []


# ======================================================================================
# CONFIGURE CHART
chart.suptitle('Classification k-')
chart.yticks(np.arange(-5000, 6000, 1000))
chart.yticks(np.arange(-5000, 6000, 1000))
chart.xlim(-5000, 5000)
chart.ylim(-5000, 5000)
chart.xlabel("X")
chart.ylabel("Y")
# ======================================================================================

class POINT:
    def __init__(self, X, Y, color):
        self.X = X
        self.Y = Y
        self.color = color
        self.distance = -1

# ======================================================================================
#
# ======================================================================================

Red1 = POINT(-4500, -4400, "red")
Red2 = POINT(-4100, -3000, "red")
Red3 = POINT(-1800, -2400, "red")
Red4 = POINT(-2500, -3400, "red")
Red5 = POINT(-2000, -1400, "red")
Green1 = POINT(+4500, -4400, "green")
Green2 = POINT(+4100, -3000, "green")
Green3 = POINT(+1800, -2400, "green")
Green4 = POINT(+2500, -3400, "green")
Green5 = POINT(+2000, -1400, "green")
Blue1 = POINT(-4500, +4400, "blue")
Blue2 = POINT(-4100, +3000, "blue")
Blue3 = POINT(-1800, +2400, "blue")
Blue4 = POINT(-2500, +3400, "blue")
Blue5 = POINT(-2000, +1400, "blue")
Purple1 = POINT(+4500, +4400, "purple")
Purple2 = POINT(+4100, +3000, "purple")
Purple3 = POINT(+1800, +2400, "purple")
Purple4 = POINT(+2500, +3400, "purple")
Purple5 = POINT(+2000, +1400, "purple")

# ======================================================================================
#
# ======================================================================================

def generate_points(count, col_arr, color, xStart, xEnd, yStart, yEnd):
    for i in range(count):
        x = random.randint(xStart, xEnd)
        y = random.randint(yStart, yEnd)
        point = POINT(x, y, color)
        while point in col_arr:
            x = random.randint(xStart, xEnd)
            y = random.randint(yStart, yEnd)
            point = POINT(x, y, color)
        col_arr.append(point)

# ======================================================================================
#
# ======================================================================================

def generate_missplaced_points(count, col_arr, color, x_border, y_border):
    for i in range(count):
        while True:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
            if x > x_border and y > y_border:
                col_arr.append(POINT(x, y, color))
                break

# ======================================================================================
#
# ======================================================================================

def classification(X, Y, K):
    global final_data

    for j in range(number_of_training_data):
        training_data[j].distance = math.sqrt(((X-training_data[j].X) ** 2) + ((Y-training_data[j].Y) ** 2))
    # calculates distances

    sorted_training_data = sorted(training_data, key=lambda z: z.distance)
    # sort data by distance from lowest to highest

    r_count = 0
    g_count = 0
    b_count = 0
    p_count = 0

    for j in range(K):
        if sorted_training_data[j].color == "red":
            r_count += 1
        elif sorted_training_data[j].color == "green":
            g_count += 1
        elif sorted_training_data[j].color == "blue":
            b_count += 1
        elif sorted_training_data[j].color == "purple":
            p_count += 1

    final_colour = max(r_count, g_count, b_count, p_count)

    if final_colour == r_count:
        final_data.append(POINT(X, Y, "red"))
        training_data.append(POINT(X, Y, "red"))
        return "red"

    elif final_colour == g_count:
        final_data.append(POINT(X, Y, "green"))
        training_data.append(POINT(X, Y, "green"))
        return "green"

    elif final_colour == b_count:
        final_data.append(POINT(X, Y, "blue"))
        training_data.append(POINT(X, Y, "blue"))
        return "blue"

    elif final_colour == p_count:
        final_data.append(POINT(X, Y, "purple"))
        training_data.append(POINT(X, Y, "purple"))
        return "purple"

# ======================================================================================
#
# ======================================================================================

def assign(color):
    
    global assigned
    if random.random() < 0.99:
        if color == "red":
            assigned = assign_color(r, red_count, RED_ARR, color)
        if color == "green":
            assigned = assign_color(g, green_count, GREEN_ARR, color)
        if color == "blue":
            assigned = assign_color(b, blue_count, BLUE_ARR, color)
        if color == "purple":
            assigned = assign_color(p, purple_count, PURPLE_ARR, color)

    else:
        if color == "red":
            assigned = assign_color(r, red_count, RED_ARR_MISSPLACED, color)
        if color == "green":
            assigned = assign_color(g, green_count, GREEN_ARR_MISSPLACED, color)
        if color == "blue":
            assigned = assign_color(b, blue_count, BLUE_ARR_MISSPLACED, color)
        if color == "purple":
            assigned = assign_color(p, purple_count, PURPLE_ARR_MISSPLACED, color)

# ======================================================================================
#
# ======================================================================================

def assign_color(col, col_count, col_arr, color):
    global red_count, green_count, blue_count, purple_count
    global r, g, b, p, number_of_training_data
    if col_count != POINTS_COUNT:
        col_pop = col_arr[col]
        x_coordinate = col_pop.X
        y_coordinate = col_pop.Y
        if color == "red":
            red_count += 1
            r += 1
        if color == "green":
            green_count += 1
            g += 1
        if color == "blue":
            blue_count += 1
            b += 1
        if color == "purple":
            purple_count += 1
            p += 1
        assign = classification(x_coordinate, y_coordinate, knn)
        number_of_training_data  += 1
        return assign

# ======================================================================================
#
# ======================================================================================

def start():
    print("*** Started Classification")
    # here starts the generation of points in the right range
    generate_points(POINTS_COUNT, RED_ARR, "red", -5000, 500, -5000, 500)
    generate_points(POINTS_COUNT, GREEN_ARR, "green", -500, 5000, -5000, 500)
    generate_points(POINTS_COUNT, BLUE_ARR, "blue", -5000, 500, -500, 5000)
    generate_points(POINTS_COUNT, PURPLE_ARR, "purple", -500, 5000, -500, 5000)

    # here starts the generation of points in the wrong range
    generate_missplaced_points(POINTS_COUNT, RED_ARR_MISSPLACED, "red", 500, 500)
    generate_missplaced_points(POINTS_COUNT, GREEN_ARR_MISSPLACED, "green", -500, 500)
    generate_missplaced_points(POINTS_COUNT, BLUE_ARR_MISSPLACED, "blue", 500, -500)
    generate_missplaced_points(POINTS_COUNT, PURPLE_ARR_MISSPLACED, "purple", 500, 500)
    
    color_list = ["red", "green", "blue", "purple"]
    global assigned, last_assigned, fault
    start = time.time()

    training_data.extend((Red1, Red2, Red3, Red4, Red5, 
                          Green1, Green2, Green3, Green4, Green5, 
                          Blue1, Blue2, Blue3, Blue4, Blue5, 
                          Purple1, Purple2, Purple3, Purple4, Purple5))
    
    final_data.extend((Red1, Red2, Red3, Red4, Red5, 
                       Green1, Green2, Green3, Green4, Green5, 
                       Blue1, Blue2, Blue3, Blue4, Blue5, 
                       Purple1, Purple2, Purple3, Purple4, Purple5))

    while True:
        if red_count == blue_count == green_count == purple_count == POINTS_COUNT:
            break

        while True:
            random_number = random.randint(0, 3)
            color = color_list[random_number]
            if red_count or blue_count or green_count or purple_count == 10000:
                break
            if color != last_assigned:
                break

        assign(color)                    

        if assigned != color:
            fault += 1
        last_assigned = assigned


    print("Pocet bodov je:", POINTS_COUNT * 4 + 20)
    print("pocet chyb je: ", fault)
    end = time.time()
    print("time elapsed:", end - start)

    for data in final_data:
        chart.plot(data.X, data.Y, marker="o", color=data.color)
    
    chart.show()

# ======================================================================================
# START
# ======================================================================================
start()
print("finished")
# ======================================================================================

