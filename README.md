# FSM-Markov-chain
This project aims from a FSM (Finite State Machine), representing a Markov chain, to generate and rank the test cases. The test cases are ranked according to the sequence probability, i.e., the product of the probabilities of the arcs traversed. It is important to remember that, Markov chain describes a process in which the transition to a state at time t + 1 depends only on the state at time t.

## Main Program

The main program is fsm-mc.py and is written in python 3. The imported packages are:
- numpy
- random
- progressbar

In the main program, in addition to the functions, we inserted a test case. This test case is a Markov chain represented by an FSM, which can be seen in the image below:

![alt text](https://github.com/giirso/FSM-Markov-chain/blob/master/FSM-example.jpg)

## Input 
In this version, the setup of test case prioritization is done in the configuration file called input.yaml. Where is past:

- The path of the transition matrix;
- The file path with the states;
- The final node;
- The final node;
- Stop criterion.

There is an example of each of these external files in the repository to make it easier for you to configure your own. 
The above examples also refer to the figure cited.

## Run

To run the program, just type in the terminal:

python3 fsm-mc.py input.yaml

## Output

Outputs are given in two .txt files. One of them (*states.txt*) shows the states travelled and the resulting probability of this path. In the other (*arcs.txt*) we have the arcs traversed along with their probability.

