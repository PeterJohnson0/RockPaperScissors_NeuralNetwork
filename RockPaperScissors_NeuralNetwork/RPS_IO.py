# RPS_IO.py
# Module for determining outcome of RPS game.
# Peter Johnson

import random

#Set the GameMode using the menu.
def modeSet(GameMode, x):
	GameMode['GM'] = x
	return

# Returns the CPU move
def CPU_move(GameMode, P1_Hist, Net):
	if GameMode['GM'] == 1: #random pick
		Y = random.randint(0,2) 
	elif GameMode['GM'] == 2: #Neural Network
		Y = Net.getNetPick(P1_Hist)
	return Y

# Compare picks and returns the winner.
def PickWinner(P1, P2): #0 = rock, 1 = paper, 2 = scissors
	if P1 == 0:
		if P2 == 0:
			W = 0
		elif P2 == 1:
			W = 2
		elif P2 == 2:
			W = 1
	elif P1 == 1:
		if P2 == 0:
			W = 1
		elif P2 == 1:
			W = 0
		elif P2 == 2:
			W = 2
	elif P1 == 2:
		if P2 == 0:
			W = 2
		elif P2 == 1:
			W = 1
		elif P2 == 2:
			W = 0
	return W #0 = draw, 1 = P1, 2 = P2

def UpdateHist(P1, P1_Hist):
	for i in range (len(P1_Hist)-1, 2, -1):
		P1_Hist[i] = P1_Hist[i-3]
	for i in range(3):
		if P1 == i:
			P1_Hist[i] = 1
		else:
			P1_Hist[i] = 0
	return

def resetScore(Scores, L_S1, L_S2):
	Scores.update(S1 = 0, S2 = 0)
	L_S1['text'] = str(0)
	L_S2['text'] = str(0)
	return

#Play RPS after clicking Rock, Paper, or Scissors buttons.
def buttonPress(P1, GameMode, L_P1, L_P2, L_W, Scores, L_S1, L_S2, P1_Hist, Net, NNC):
	P2 = CPU_move(GameMode, P1_Hist, Net) #get the computer's move.
	#Update Player Pick.
	if P1 == 0:
		L_P1['text'] = 'Rock'
		Y_win = [0,1,0]
	elif P1 == 1:
		L_P1['text'] = 'Paper'
		Y_win = [0,0,1]
	elif P1 == 2:
		L_P1['text'] = 'Scissors'
		Y_win = [1,0,0]
	#Update CPU Pick
	if P2 == 0:
		L_P2['text'] = 'Rock'
	elif P2 == 1:
		L_P2['text'] = 'Paper'
	elif P2 == 2:
		L_P2['text'] = 'Scissors'
	W = PickWinner(P1, P2) #Determine Winner 
	#Update Canvas
	NNC.UpdateCanvas(P1_Hist, P2, Net)
	#Update Winner + scores
	if W == 0:
		L_W['text'] = '  Tie  '
	elif W == 1:
		L_W['text'] = 'You Win'
		s = Scores['S1']+1
		Scores.update(S1 = s)
		L_S1['text'] = str(s)
	elif W == 2:
		L_W['text'] = 'NN Wins'
		s = Scores['S2']+1
		Scores.update(S2 = s)
		L_S2['text'] = str(s)
	#update NN and P1_Hist
	Net.addTrainingData(P1_Hist, Y_win)
	Net.TrainNet(1000)
	UpdateHist(P1, P1_Hist)
	return