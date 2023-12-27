import turtle
import random
import time

window = turtle.Screen()

side = 900
X = -450
Y = 450

window.setup(side, side)
window.title("Tic,Tac, Toe")
window.bgcolor("black")

tr=turtle.Turtle()
tr.color('white')
tr.pensize(10)
tr.speed(0)
tr.hideturtle()

table = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
        ]

turn = random.choice(['X', 'O'])


#net

space = int(side/3)

for a in [1,2]:
    tr.penup()
    tr.goto(X + a*space, Y)
    tr.pendown()
    tr.goto(X + a*space, -Y)

    tr.penup()
    tr.goto(X, Y - a*space)    
    tr.pendown()
    tr.goto(-X, Y-a*space)


def check():
    
    
    if table[0][0] == table[1][1] == table[2][2]: return table[2][2]
    if table[0][2] == table[1][1] == table[2][0]: return table[2][0]

    for w in range(2):
        if table[w][0] == table[w][1] == table[w][2]: return table[w][2]

    for k in range(2):
        if table[0][k] == table[1][k] == table[2][k]: return table[2][k]


def click(x,y):

    global turn

    column=0
    row=0

    if x < X + space: column=0
    elif x > X + 2*space: column=2
    else: column=1

    if y < Y - 2*space: row=2
    elif y > Y - space: row=0 
    else: row=1

    

    if table[row][column] != None: return

    centerOfColumn = (column*space + space/2) - side/2
    centerOfRow = (-row*space - space/2) + side/2

    tr.penup()
    tr.goto(centerOfColumn-25, centerOfRow-25)

    if turn == 'X' : tr.write('X', font=('Arial', 50))
    else: tr.write('O', font=('Arial', 50))

    table[row][column] = turn

    if turn == 'O': turn = 'X'
    else: turn = 'O'

    if check() != None:
        tr.penup()
        tr.goto(-150,0)
        time.sleep(1)
        tr.clear()
        tr.write("Win: " + check(), font = ('Arial', 50))
     
   




window.onclick(click)




window.listen()
window.mainloop() 