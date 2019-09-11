# FSM-Markov-chain
This project aims from a FSM (Finite State Machine), representing a Markov chain, to generate and rank the test cases. The test cases are ranked according to the sequence probability, ie the product of the probabilities of the arcs traversed. It is important to remember that, Markov chain describes a process in which the transition to a state at time t + 1 depends only on the state at time t.

## Main Program

The main program is test2.py and is written in python 2. The imported packages are:
- numpy
- random

In the main program, in addition to the functions, we inserted a test case. This test case is a Markov chain represented by an FSM, which can be seen in the image below:

![alt text](https://github.com/giirso/FSM-Markov-chain/blob/master/FSM-example.jpg)

## Input 
In this version of the project, entries are made in the main program itself. In a next step, we will create an input file. The program requires 3 entries.
 
 - A list containing the states;
>Example:
```python
states = ["Start","Withdraw","Check","Deposit","End"]
```
-A transition matrix for the inserted states;
>Example:
```python
transitionMatrix = [[0,0.2,0.3,0.5,0.0],[0.2,0.0,0.4,0.0,0.4],[0.0,0.6,0.0,0.2,0.2],[0.5,0.0,0.1,0.0,0.4],[0.6,0.0,0.4,0.0,0.0]]
```
-And an array containing the names of the transitions.
>Example:
```python
arcsName = [["SS","SW","SC","SD","SE"],["WS","WW","WC","WD","WE"],["CS","CW","CC","CD","CE"],["DS","DW","DC","DD","DE"],["ES","EW","EC","ED","EE"]]
```
The above examples also refer to the figure cited.

## Output

Outputs are given in two .txt files. One of them (*states.txt*) shows the states traveled and the resulting probability of this path. In the other (*arcs.txt*) we have the arcs traversed along with their probability.

