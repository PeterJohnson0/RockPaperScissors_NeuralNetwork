# NNCanvas.py
# Module for storing and editing the canvas
# Peter Johnson

from tkinter import *
import math
import numpy as np

#class for storing canvas objects.
class NNCanvas:
	#initialize the canvas drawings.
	def __init__(self, Canvasframe, NetI, NetM, NetO, Net):
		#Canvas initialization
		self.NNC = Canvas(Canvasframe, width=600, height=400)
		self.NNC.pack()
		self.NI = NetI
		self.NM = NetM
		self.NO = NetO
		#call init functions for canvas components
		self.initCircles()
		self.initLabels()
		self.initSyn(Net.getSyn(0), Net.getSyn(1))
		return
	# add Node Circles
	def initCircles(self):
		self.C_I = []
		for i in range(self.NI):
			self.C_I.append(self.NNC.create_oval(95,45+(i+1)*(300/(self.NI+1)),105,55+(i+1)*(300/(self.NI+1))))
		self.C_M = []
		for i in range(self.NM):
			self.C_M.append(self.NNC.create_oval(295,45+(i+1)*(300/(self.NM+1)),305,55+(i+1)*(300/(self.NM+1))))
		self.C_O = []
		for i in range(self.NO):
			self.C_O.append(self.NNC.create_oval(495,45+(i+1)*(300/(self.NO+1)),505,55+(i+1)*(300/(self.NO+1))))
		return
	# add canvas text
	def initLabels(self):
		#Right Side
		self.L_O_Rock = self.NNC.create_text(530, 50+1*(300/(self.NO+1)), anchor=W, font=("Times", "16"), text = "Rock")
		self.L_O_Paper = self.NNC.create_text(530, 50+2*(300/(self.NO+1)), anchor=W, font=("Times", "16"), text = "Paper")
		self.L_O_Scissors = self.NNC.create_text(530, 50+3*(300/(self.NO+1)), anchor=W, font=("Times", "16"), text = "Scissors")
		#Left Side Lines
		self.NNC.create_line(80,50+0.5*(300/(self.NI+1)),110,50+0.5*(300/(self.NI+1)))
		self.NNC.create_line(80,50+3.5*(300/(self.NI+1)),110,50+3.5*(300/(self.NI+1)))
		self.NNC.create_line(80,50+6.5*(300/(self.NI+1)),110,50+6.5*(300/(self.NI+1)))
		self.NNC.create_line(80,50+9.5*(300/(self.NI+1)),110,50+9.5*(300/(self.NI+1)))
		self.NNC.create_line(80,50+12.5*(300/(self.NI+1)),110,50+12.5*(300/(self.NI+1)))
		#Left Side
		self.NNC.create_text(20,50+2*(300/(self.NI+1)), anchor=W, font=("Times", "12"), text = "R=-1")
		self.NNC.create_text(20,50+5*(300/(self.NI+1)), anchor=W, font=("Times", "12"), text = "R=-2")
		self.NNC.create_text(20,50+8*(300/(self.NI+1)), anchor=W, font=("Times", "12"), text = "R=-3")
		self.NNC.create_text(20,50+11*(300/(self.NI+1)), anchor=W, font=("Times", "12"), text = "R=-4")
		for i in range(4):
			self.NNC.create_text(70,50+((i*3)+1)*(300/(self.NI+1)), anchor=W, font=("Times", "12"), text = "R")
			self.NNC.create_text(70,50+((i*3)+2)*(300/(self.NI+1)), anchor=W, font=("Times", "12"), text = "P")
			self.NNC.create_text(70,50+((i*3)+3)*(300/(self.NI+1)), anchor=W, font=("Times", "12"), text = "S")
		return
	# add Synapsis Lines
	def initSyn(self, Syn0, Syn1):
		self.S0 = [[0 for j in range(self.NM)] for i in range(self.NI)]
		self.S1 = [[0 for j in range(self.NO)] for i in range(self.NM)]
		for i in range(self.NI):
			for j in range(self.NM):
				self.S0[i][j] = self.NNC.create_line(105,50+(i+1)*(300/(self.NI+1)),295,50+(j+1)*(300/(self.NM+1)))
		for i in range(self.NM):
			for j in range(self.NO):
				self.S1[i][j] = self.NNC.create_line(305,50+(i+1)*(300/(self.NM+1)),495,50+(j+1)*(300/(self.NO+1)))
		self.UpdateSynLines(Syn0, Syn1)
		return
	#Update Syn Line colours.
	def UpdateSynLines(self, Syn0, Syn1):
		S0_Max = max(np.amax(Syn0), np.amin(Syn0))
		S1_Max = max(np.amax(Syn1), np.amin(Syn1))
		for i in range(self.NI):
			for j in range(self.NM):
				if S0_Max < abs(Syn0[i][j])*2:
					if Syn0[i][j] > 0:
						self.NNC.itemconfig(self.S0[i][j], fill='blue')
					else:
						self.NNC.itemconfig(self.S0[i][j], fill='red')
				else:
					self.NNC.itemconfig(self.S0[i][j], fill='')
		for i in range(self.NM):
			for j in range(self.NO):
				if S1_Max < abs(Syn1[i][j])*2:
					if Syn1[i][j] > 0:
						self.NNC.itemconfig(self.S1[i][j], fill='blue')
					else:
						self.NNC.itemconfig(self.S1[i][j], fill='red')
				else:
					self.NNC.itemconfig(self.S1[i][j], fill='')
		return
	# Update Canvas
	def UpdateCanvas(self, P1_Hist, P2, Net):
		for i in range(self.NI):
			if P1_Hist[i] == 1:
				self.NNC.itemconfig(self.C_I[i],fill='black')
			else:
				self.NNC.itemconfig(self.C_I[i],fill='')
		for i in range(self.NO):
			if i == P2:
				self.NNC.itemconfig(self.C_O[i],fill='black')
			else:
				self.NNC.itemconfig(self.C_O[i],fill='')
		self.UpdateSynLines(Net.getSyn(0), Net.getSyn(1))
		return
	
	