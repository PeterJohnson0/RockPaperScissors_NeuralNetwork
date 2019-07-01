# Rock Paper Scissors - Neural Network
# RockPaperScissors_NeuralNetwork.py
# Peter Johnson

# This program uses a Neural network to try and beat a player in Rock Paper Scissors by
# Using the player's previous choices as inputs.
# Uses graphics.py

from NeurNet import *
from graphics import *
from random import *

WinH = 800
WinW = 600

win = GraphWin("Rock Paper Scissors - Neural Network", WinH, WinW)

#Initializes the neural network (may move)
NetI = 12
NetM = 20
NetO = 3
Net = NeurNet(NetI,NetM,NetO)
I_prev = [.5]*NetI

#Visualized NN components
I_prevtext = [0]*NetI
O_outtext = [0]*NetO
Line_IM = [[0]*NetM for i in range(NetI)]
Line_MO = [[0]*NetO for i in range(NetM)]
Tally_P1 = 0
Tally_P2 = 0
T_T1 = Text(Point(25, 400), Tally_P1)
T_T2 = Text(Point(775, 400), Tally_P2)

#Outcome Text
T_P1 = Text(Point(150, 400), "")
T_P1.setSize(20)
T_P2 = Text(Point(650, 400), "")
T_P2.setSize(20)
T_Res = Text(Point(400, 400), "")
T_Res.setSize(20)

#Function drawing the 3 main buttons.
def Button1_Draw(x1, y1, B_text):
    B = Rectangle(Point(x1, y1), Point(x1+150, y1+80))
    B.draw(win)
    
    T = Text(Point(x1+75, y1+40), B_text)
    T.setSize(20)
    T.draw(win)

def Button2_Draw(x1, y1, B_text):
    B = Rectangle(Point(x1, y1), Point(x1+100, y1+40))
    B.draw(win)
    
    T = Text(Point(x1+50, y1+20), B_text)
    T.setSize(12)
    T.draw(win)

# Draws the static graphics.
def Draw_Main():
    # Draw the windows
    W1 = Rectangle(Point(50, 50), Point(750, 350))
    W1.draw(win)
    
    W2 = Rectangle(Point(50, 375), Point(750, 425))
    W2.draw(win)
    
    T_T1.draw(win)
    T_T2.draw(win)
    
    # Draw the Buttons
    Button1_Draw(125, 450, "Rock")
    Button1_Draw(325, 450, "Paper")
    Button1_Draw(525, 450, "Scissors")
    Button2_Draw(50, 5, "Refresh")
    #Button2_Draw(250, 5, "tbd")
    #Button2_Draw(450, 5, "tbd")
    Button2_Draw(650, 5, "Quit")
    
    T_P1.draw(win)
    T_P2.draw(win)
    T_Res.draw(win)
    #Draw NN
    Draw_NN()

# Draws Neural Network
def Draw_NN():
    #Draw NN Headers
    T_Input = Text(Point(200, 60), "Prev Inputs")
    T_Input.setSize(10)
    T_Input.draw(win)
    T_Mid = Text(Point(400, 60), "Hidden Layer")
    T_Mid.setSize(10)
    T_Mid.draw(win)
    T_Output = Text(Point(600, 60), "Output")
    T_Output.setSize(10)
    T_Output.draw(win)
    T_Rock = Text(Point(700, 100), "Rock")
    T_Rock.setSize(12)
    T_Rock.draw(win)
    T_Paper = Text(Point(700, 200), "Paper")
    T_Paper.setSize(12)
    T_Paper.draw(win)
    T_Scissors = Text(Point(700, 300), "Scissors")
    T_Scissors.setSize(12)
    T_Scissors.draw(win)
    #Draw Node Circles
    NI_circ = [0]*NetI
    NM_circ = [0]*NetM
    NO_circ = [0]*NetO
    for i in range(NetI):
        NextNode = Point(200, 80+(240*i/(NetI-1)))
        NI_circ[i] = Circle(NextNode,10)
        NI_circ[i].draw(win)
        I_prevtext[i] = Text(NextNode, "-")
        I_prevtext[i].setSize(5)
        I_prevtext[i].draw(win)
    for i in range(NetM):
        NextNode = Point(400, 80+(240*i/(NetM-1)))
        NM_circ[i] = Circle(NextNode,5)
        NM_circ[i].draw(win)
    for i in range(NetO):
        NextNode = Point(600, 100+(200*i/(NetO-1)))
        NO_circ[i] = Circle(NextNode,20)
        NO_circ[i].draw(win)
        O_outtext[i] = Text(NextNode, "-")
        O_outtext[i].setSize(12)
        O_outtext[i].draw(win)
    #Draw Node Lines
    for i in range(NetI):
        for j in range(NetM):
            P1 = Point(210, 80+(240*i/(NetI-1)))
            P2 = Point(390, 80+(240*j/(NetM-1)))
            Line_IM[i][j] = Line(P1, P2)
            Line_IM[i][j].setWidth(1)
            Line_IM[i][j].draw(win)
    for i in range(NetM):
        for j in range(NetO):
            P1 = Point(410, 80+(240*i/(NetM-1)))
            P2 = Point(590, 100+(200*j/(NetO-1)))
            Line_MO[i][j] = Line(P1, P2)
            Line_MO[i][j].setWidth(1)
            Line_MO[i][j].draw(win)

#Redraw Neural Network
def Redraw_NN():
    W1 = Net.get_W1()
    W2 = Net.get_W2()
    #Node Line weights
    for i in range(NetI):
        for j in range(NetM):
            NewWidth = 2*W1[j][i]
            print("W1[%(a)d][%(b)d]=%(c)f" %{"a": i, "b": j, "c": W1[j][i]})
            if NewWidth < 0.5:
                Line_IM[i][j].setWidth(0)
            elif NewWidth < 1.5:
                Line_IM[i][j].setWidth(1)
            else:
                Line_IM[i][j].setWidth(2)
            
    for i in range(NetM):
        for j in range(NetO):
            NewWidth = 2*W2[j][i]
            print("W2[%(a)d][%(b)d]=%(c)f" %{"a": i, "b": j, "c": W2[j][i]})
            if NewWidth < 0.5:
                Line_MO[i][j].setWidth(0)
            elif NewWidth < 1.5:
                Line_MO[i][j].setWidth(1)
            else:
                Line_MO[i][j].setWidth(2)

# Determines Button Pressed
def ButtonCheck(MousePos):
    PressChoice = 0
    MX = MousePos.getX()
    MY = MousePos.getY()
    if MX >= 125 and MX <= 275 and MY >= 450 and MY <= 530:
        PressChoice = 1
    elif MX >= 325 and MX <= 475 and MY >= 450 and MY <= 530:
        PressChoice = 2
    elif MX >= 525 and MX <= 675 and MY >= 450 and MY <= 530:
        PressChoice = 3
    elif MX >= 50 and MX <= 150 and MY >= 5 and MY <= 45:
        PressChoice = 4
    elif MX >= 650 and MX <= 750 and MY >= 5 and MY <= 45:
        PressChoice = 7
    return PressChoice

#Decide Winner
def RPS_Game(P1_Choice):
    global Tally_P1
    global Tally_P2
    OutO = Net.Forward(I_prev)
    I_Cur = [0,0,0]
    O_Tar = [0,0,0]
    P2_Choice = 0
    for i in range(NetO):
        if OutO[i] > OutO[P2_Choice]:
            P2_Choice = i
    if P1_Choice == 0:
        I_Cur = [1,0,0]
        O_Tar = [0,1,0]
        T_P1.setText("Rock")
        if P2_Choice == 0:
            T_P2.setText("Rock")
            T_Res.setText("Draw")
        elif P2_Choice == 1:
            T_P2.setText("Paper")
            T_Res.setText("P2 Wins")
            Tally_P2 = Tally_P2 + 1
            T_T2.setText(Tally_P2)
        elif P2_Choice == 2:
            T_P2.setText("Scissors")
            T_Res.setText("P1 Wins")
            Tally_P1 = Tally_P1 + 1
            T_T1.setText(Tally_P1)
    elif P1_Choice == 1:
        I_Cur = [0,1,0]
        O_Tar = [0,0,1]
        T_P1.setText("Paper")
        if P2_Choice == 0:
            T_P2.setText("Rock")
            T_Res.setText("P1 Wins")
            Tally_P1 = Tally_P1 + 1
            T_T1.setText(Tally_P1)
        elif P2_Choice == 1:
            T_P2.setText("Paper")
            T_Res.setText("Draw")
        elif P2_Choice == 2:
            T_P2.setText("Scissors")
            T_Res.setText("P2 Wins")
            Tally_P2 = Tally_P2 + 1
            T_T2.setText(Tally_P2)
    elif P1_Choice == 2:
        I_Cur = [0,0,1]
        O_Tar = [1,0,0]
        T_P1.setText("Scissors")
        if P2_Choice == 0:
            T_P2.setText("Rock")
            T_Res.setText("P2 Wins")
            Tally_P2 = Tally_P2 + 1
            T_T2.setText(Tally_P2)
        elif P2_Choice == 1:
            T_P2.setText("Paper")
            T_Res.setText("P1 Wins")
            Tally_P1 = Tally_P1 + 1
            T_T1.setText(Tally_P1)
        elif P2_Choice == 2:
            T_P2.setText("Scissors")
            T_Res.setText("Draw")
    #Text results
    for i in range(NetI):
        I_prevtext[i].setText(round(I_prev[i], 1))
    for i in range(NetO):
        O_outtext[i].setText(round(OutO[i], 2))
    
    #Update Neural Net
    Net.BackProp(I_prev, O_Tar)
    Icopy1 = [0,0,0]
    for i in range(len(I_prev)):
        Icopy2 = I_prev[i]
        if i < 3:
            I_prev[i] = I_Cur[i]
        else:
            I_prev[i] = Icopy1[i%3]
        Icopy1[i%3] = Icopy2
    

#The Main Function
def main():
    
    Draw_Main() #Draw the main Static Info
    
    mainloop = True
    while mainloop:
        ButtonChoice = ButtonCheck(win.getMouse()) # Pause to view result
        
        if ButtonChoice != 0:
            if ButtonChoice == 1:
                RPS_Game(0)
                print("Rock")
            elif ButtonChoice == 2:
                RPS_Game(1)
                print("Paper")
            elif ButtonChoice == 3:
                RPS_Game(2)
                print("Scissors")
            elif ButtonChoice == 4:
                print("Refresh")
                Redraw_NN()
            elif ButtonChoice == 5:
                print("5")
            elif ButtonChoice == 6:
                print("6")
            elif ButtonChoice == 7:
                print("Quit")
                win.close()
                mainloop = False


main()
