# "Stopwatch: The Game"

import simplegui
import random

# define global variables
time = 0          # global time
interval = 100    # timer interval
stops = 0         # stop counter
wins = 0          # wins counter
is_running = True # toggle

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = int(t / 600)
    seconds_1 = int(t / 100) % 6
    seconds_2 = int(t / 10) % 10
    tenths = t % 10
    return str(minutes) + ":" + str(seconds_1) + str(seconds_2) + "." + str(tenths)
    pass

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global is_running
    timer.start()
    is_running = True

def stop():
    global wins, stops, is_running
    if (is_running):
        timer.stop()
        is_running = False
        stops += 1
        if (time % 10) == 0:
            wins += 1

def reset():
    global time, wins, stops, is_running
    time = 0
    wins = 0
    stops = 0
    is_running = False
    timer.stop()

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
#def draw(canvas):
    #canvas.draw_text(format(time), [80, 174], 64, "White")
    #canvas.draw_text(str(wins) + "/" + str(stops), [200, 60], 32, "Red")

def draw(canvas):
    global stops
    global wins
    score = str(wins) + '/' + str(stops)
    # my list of colors
    colors = ["blue", "white", "red", "black"]

    # my stopwatch loopy thing
    canvas.draw_circle([150, 48], 20, 7, colors[0])
    canvas.draw_circle([150, 48], 19, 5, colors[1])
    canvas.draw_circle([150, 48], 18, 4, colors[0])

    # my stopwatch button
    canvas.draw_line((75, 100), (95, 85), 20, colors[0])
    canvas.draw_line((88, 95), (95, 90), 25, colors[1])

    # my stopwatch stem
    canvas.draw_line((140, 65), (160, 65), 30, colors[0])
    canvas.draw_line((150, 65), (155, 65), 30, colors[1])

    # my stopwatch face
    canvas.draw_circle([150, 170], 90, 12, colors[0])
    canvas.draw_circle([150, 170], 88, 2, colors[1])
    canvas.draw_circle([150, 170], 80, 10, colors[1])
    canvas.draw_circle([150, 170], 76, 2, colors[0], colors[3])

    # my stopwatch text
    canvas.draw_text(format(time), (107, 180), 36, colors[1])
    canvas.draw_text(score, (240, 40), 28, colors[2])

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)
frame.set_canvas_background("white")

# create timer
timer = simplegui.create_timer(interval, tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()
