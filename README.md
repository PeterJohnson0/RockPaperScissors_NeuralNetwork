# RockPaperScissors_NeuralNetwork
v1. Programmed by Peter Johnson as of July 1, 2019

Summary of Program:
This program lets the user play the game of Rock Paper Scissors against a Neural Network. The purpose was to practice programming a neural network. In theory, a person should be randomly picking between the 3 outcomes.

The Neural Network works by taking the last few user inputs (placed in groups of 3) and attempts to predict what the user will pick next based on this history. The program displays the outcome of the match, trains the network with the result, and then if there is a winner, the result is tallied.

The network is displayed in the top half of the screen, and can be refreshed manually with the refresh button (refreshing after each game was found to be slow). Line width roughly indicates the weighting for each connection, with the pixel width being either 0, 1, or 2

Installation Guide:
1. Ensure Python is installed (v3.7.3).

2. Download graphics.py and save it in Python37\Lib\site-packages
- available for download at mcsp.wartburg.edu/zelle/python/graphics-py

3. Double-click RockPaperScissors_NeuralNetwork.py to run the program.

Instructions:

Run RockPaperScissors_NeuralNetwork.py by either running it through your python shell, command prompt, or by double-clicking the file. 

Click "Rock", "Paper", or "Scissors" to play against the Neural Network
Click "Quit" to exit.
Click "Refresh" to update the Neural Network image.

