# RockPaperScissors_NeuralNetwork
v1.3 Programmed by Peter Johnson as of Nov 13, 2019

Summary of Program:
This program lets the user play the game of Rock Paper Scissors against a Neural Network. The purpose was to practice programming a neural network. In theory, a person should be randomly picking between the 3 outcomes.

The Neural Network works by taking the last few user inputs (placed in groups of 3) and attempts to predict what the user will pick next based on this history. The program displays the outcome of the match, trains the network with the result, and then if there is a winner, the result is tallied.


Installation Guide:
1. Ensure Python is installed (v3.7.3).

2. Download prerequisite packages (numpy.py, tkinter.py) vai pip or equivalent:
	pip install numpy
	pip install tkinter
	
3. Double-click RockPaperScissors_NeuralNetwork.py to run the program.

Instructions:

To run the program, double-click Run.bat

Click "Rock", "Paper", or "Scissors" to play against the Neural Network
In the menu:
- 'Reset Neural Network' randomizes the synapses and resets NN data
- 'Reset Score' resets the score to 0-0
- 'RNG Mode' sets the game to be normal Rock-paper-scissors (while still training the Net)
- 'NN Mode' sets the game to be against a Neural Net (default), which in theory should win more the more you play.
- 'Quit' quits
