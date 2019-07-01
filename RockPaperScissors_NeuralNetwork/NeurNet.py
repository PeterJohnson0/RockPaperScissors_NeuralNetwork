# NeurNet.py
# Module for making simple Neural Networks
# Peter Johnson

import math

class NeurNet:
    
    NC_I = 0
    NC_M = 0
    NC_O = 0
    W1 = [[]]
    W2 = [[]]
    B1 = 0.35
    B2 = 0.6
    n = 0.5 #learning function
    
    #Initializes the Neural Network
    def __init__(self, R1, R2, R3):
        self.NC_I = R1
        self.NC_M = R2
        self.NC_O = R3
        
        self.W1 = [[0.5]*self.NC_I for i in range(self.NC_M)]
        self.W2 = [[0.5]*self.NC_M for i in range(self.NC_O)]
    
    #Get W1
    def get_W1(self):
        return self.W1
    
    #Get W2
    def get_W2(self):
        return self.W2
    
    #First Layer
    def Layer1(self, I_Arr):
        NetM = [0]*self.NC_M
        OutM = [0]*self.NC_M
        # Net value for middle
        for i in range(self.NC_M): #Sums up weighted inputs plus biases.
            for j in range(self.NC_I):
                NetM[i] = NetM[i] + I_Arr[j]*self.W1[i][j]
            NetM[i] = NetM[i] + self.B1
        
        #Output value for middle
        for i in range(self.NC_M): #Applies logistic function to squash output
            OutM[i] = 1/(1+math.exp(-NetM[i]))
        return OutM
    
    #Second Layer
    def Layer2(self, M_Arr):
        NetO = [0]*self.NC_O
        OutO = [0]*self.NC_O
        
        # Net value for Output
        for i in range(self.NC_O):
            for j in range(self.NC_M):
                NetO[i] = NetO[i] + M_Arr[j]*self.W2[i][j]
            NetO[i] = NetO[i] + self.B2
        
        #Output value for Output
        for i in range(self.NC_O):
            OutO[i] = 1/(1+math.exp(-NetO[i]))
        return OutO
    
    #Takes an input array, returns output
    def Forward(self, I_Arr):
        OutM = self.Layer1(I_Arr)
        OutO = self.Layer2(OutM)
        return OutO
    
    #Uses input, output and desired output to refine the neural network
    def BackProp(self, I_Arr, O_tar):
        # Forward Pass
        OutM = self.Layer1(I_Arr)
        OutO = self.Layer2(OutM)
        # Update W1
        for i in range(self.NC_M):
            for j in range(self.NC_I):
                ChainRuleVar1 = I_Arr[j]*OutM[i]*(1-OutM[i])
                ChainRuleVar2 = 0
                for k in range(self.NC_O):
                    ChainRuleVar2 = ChainRuleVar2 + (OutO[k]-O_tar[k])*(OutO[k])*(1-OutO[k])*self.W2[k][i]
                self.W1[i][j] = self.W1[i][j]-self.n*(ChainRuleVar1*ChainRuleVar2)
        # Update W2
        for i in range(self.NC_O):
            for j in range(self.NC_M):
                self.W2[i][j] = self.W2[i][j] - self.n*OutM[j]*(OutO[i]-O_tar[i])*OutO[i]*(1-OutO[i])
        
