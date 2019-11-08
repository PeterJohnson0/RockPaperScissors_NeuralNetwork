# Rock Paper Scissors - Neural Network
# RockPaperScissors_NeuralNetwork.py
# Peter Johnson

# This program uses a Neural network to try and beat a player in Rock Paper Scissors by
# Using the player's previous choices as inputs.

from NeurNet import *
from RPS_IO import *
from tkinter import *

#Main Loop
def main():
	#Variable Setup.
	NetI = 12#12
	NetM = 20#20
	NetO = 3#3
	Net = NeurNet(NetI,NetM,NetO)
	Scores = {'S1': 0, 'S2': 0}
	GameMode = {'GM':2} #default game mode. 1 = rng, 2 = NN
	P1_Hist = [0]*NetI

	# window setup
	root = Tk()
	mainframe = Frame(root, width = 800, height = 600)
	mainframe.pack()
	#Menu
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Reset Neural Network", command=lambda: Net.resetData())
	filemenu.add_command(label="Reset Score", command=lambda: resetScore(Scores, L_YS, L_NS))
	filemenu.add_command(label="RNG Mode", command=lambda: modeSet(GameMode,1))
	filemenu.add_command(label="NN Mode", command=lambda: modeSet(GameMode,2))
	filemenu.add_command(label="Quit", command=root.quit)
	menubar.add_cascade(label="File", menu=filemenu)
	root.config(menu=menubar)
	#NN Canvas
	Canvasframe = Frame(mainframe, height=400)
	Canvasframe.pack(side = TOP)
	NNC = Canvas(Canvasframe, width=600, height=400)
	NNC.pack()
	#Circles on Canvas
	C_I = []
	for i in range(NetI):
		C_I.append(NNC.create_oval(95,45+(i+1)*(300/(NetI+1)),105,55+(i+1)*(300/(NetI+1))))
	C_M = []
	for i in range(NetM):
		C_M.append(NNC.create_oval(295,45+(i+1)*(300/(NetM+1)),305,55+(i+1)*(300/(NetM+1))))
	C_O = []
	for i in range(NetO):
		C_O.append(NNC.create_oval(495,45+(i+1)*(300/(NetO+1)),505,55+(i+1)*(300/(NetO+1))))
	
	#Scores
	Scoreframe = Frame(mainframe, height=50)
	Scoreframe.pack(side = TOP)
	L_YS = Label(Scoreframe, font=("Times", "36", "bold"), text = str(0), width=3)
	L_YS.pack(side = LEFT)
	L_YP = Label(Scoreframe, font=("Times", "36", "bold"), text = 'N/A', width=8)
	L_YP.pack(side = LEFT)
	L_W = Label(Scoreframe, font=("Times", "36", "bold"), text = '       ', width=7)
	L_W.pack(side = LEFT)
	L_NP = Label(Scoreframe, font=("Times", "36", "bold"), text = 'N/A', width=8)
	L_NP.pack(side = LEFT)
	L_NS = Label(Scoreframe, font=("Times", "36", "bold"), text = str(0), width=3)
	L_NS.pack(side = LEFT)
	
	#RPS buttons
	RPSframe = Frame(mainframe, height=50)
	RPSframe.pack(side = BOTTOM)
	RockButton = Button(RPSframe, font=("Times", "36", "bold"), text = "Rock", width=8)
	RockButton['command'] = lambda: buttonPress(0, GameMode, L_YP, L_NP, L_W, Scores, L_YS, L_NS, P1_Hist, Net)
	RockButton.pack(side = LEFT)
	PaperButton = Button(RPSframe, font=("Times", "36", "bold"), text = "Paper", width=8)
	PaperButton['command'] = lambda: buttonPress(1, GameMode, L_YP, L_NP, L_W, Scores, L_YS, L_NS, P1_Hist, Net)
	PaperButton.pack(side = LEFT)
	ScissorsButton = Button(RPSframe, font=("Times", "36", "bold"), text = "Scissors", width=8)
	ScissorsButton['command'] = lambda: buttonPress(2, GameMode, L_YP, L_NP, L_W, Scores, L_YS, L_NS, P1_Hist, Net)
	ScissorsButton.pack(side = LEFT)
	
	#draw window
	root.mainloop()

main()
