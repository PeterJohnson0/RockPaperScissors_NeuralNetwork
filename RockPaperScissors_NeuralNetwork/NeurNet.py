# NeurNet.py
# Module for making simple Neural Networks
# Peter Johnson

import numpy as np
import os

class NeurNet:
	
	
	#Initializes the Neural Network
	def __init__(self, R1, R2, R3):
		self.NC_I = R1
		self.NC_M = R2
		self.NC_O = R3
		np.random.seed(1)
		self.syn0 = 2*np.random.random((self.NC_I,self.NC_M)) - 1
		self.syn1 = 2*np.random.random((self.NC_M,self.NC_O)) - 1
		#get File paths
		full_path = os.path.realpath(__file__)
		path, filename = os.path.split(full_path)
		self.F_X = path + '\\NN_X.txt'
		self.F_Y = path + '\\NN_Y.txt'
		self.TrainNet(10000)
	
	#Sigmoid Function
	def nonlin(self, x, deriv):
		if(deriv==True):
			return x*(1-x)
		return 1/(1+np.exp(-x))
	
	#Use input array to guess output array.
	def getNetPick(self, X): #X is a list
		LI = np.asarray(X)
		LM = self.nonlin(np.dot(LI,self.syn0), False)
		LO = self.nonlin(np.dot(LM,self.syn1), False)
		LOmax = np.where(LO == LO.max())
		Y = LOmax[0]
		return Y
		
	#Add training data
	def addTrainingData(self, XL, YL): #XL and YL are lists
		F = open(self.F_X, 'a') 
		F.write(','.join([str(elem) for elem in XL]))
		F.write('\n')
		F.close 
		F = open(self.F_Y, 'a') 
		F.write(','.join([str(elem) for elem in YL]))
		F.write('\n')
		F.close 
	
	#Use training data to improve the Neural Network.
	def TrainNet(self, cycles):
		DatCount = 0
		X = []
		Y = []
		#Read data from files and convert them into arrays.
		Fx = open(self.F_X, 'r')
		Fy = open(self.F_Y, 'r')
		LineX = Fx.readline()
		LineY = Fy.readline()
		while LineX != '':
			DatCount += 1
			XL = eval(LineX)
			YL = eval(LineY)
			X.append(np.asarray(XL))
			Y.append(np.asarray(YL))
			LineX = Fx.readline()
			LineY = Fy.readline()
		Fx.close 
		Fy.close
		X = np.array(X)
		Y = np.array(Y)
		#If there is data, train with it.
		if DatCount > 0:
			for i in range(cycles):
				#Layers
				LI = X
				LM = self.nonlin(np.dot(LI,self.syn0), False)
				LO = self.nonlin(np.dot(LM,self.syn1), False)
				#Error + Correction
				LO_err = Y - LO
				LO_D = LO_err * self.nonlin(LO,deriv=True)
				LM_err = LO_D.dot(self.syn1.T)
				LM_D = LM_err * self.nonlin(LM,deriv=True)
				self.syn1 += LM.T.dot(LO_D)
				self.syn0 += LI.T.dot(LM_D)
	
	#Reset Training Data
	def resetData(self):
		F = open(self.F_X, 'w') 
		F.write('')
		F.close 
		F = open(self.F_Y, 'w') 
		F.write('')
		F.close
		np.random.seed(1)
		self.syn0 = 2*np.random.random((self.NC_I,self.NC_M)) - 1
		self.syn1 = 2*np.random.random((self.NC_M,self.NC_O)) - 1
	
	#Return Synopse Data
	def getSyn(self, row):
		if row == 0:
			S = self.syn0
		elif row == 1:
			S = self.syn1
		return S
	