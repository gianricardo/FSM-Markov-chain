##############################
##Gerson de Oliveira Barbosa##
##  Doutorando - CAP/INPE   ##
##  email:giirso@gmail.com  ##
##############################
import numpy as np
import random as rm

'''Declaring possible states:'''
states = ["Start","Withdraw","Check","Deposit","End"]

'''Arc's names'''
arcsName = [["SS","SW","SC","SD","SE"],["WS","WW","WC","WD","WE"],["CS","CW","CC","CD","CE"],["DS","DW","DC","DD","DE"],["ES","EW","EC","ED","EE"]]

'''Probabilities matrix (transition matrix).'''
transitionMatrix = [[0,0.2,0.3,0.5,0.0],[0.2,0.0,0.4,0.0,0.4],[0.0,0.6,0.0,0.2,0.2],[0.5,0.0,0.1,0.0,0.4],[0.6,0.0,0.4,0.0,0.0]]

'''Checking if the transition matrix is correct, that is, the sum of the lines is equal to 1.'''
if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[2])+sum(transitionMatrix[3])+sum(transitionMatrix[4]) != 5:
    print("Incorrect distribution!!")

'''Function that calculates the limit probability of the transition matrix.'''
def probLimit(matrix):
	i = 0
        epsilon  = 1e-8
        matrixAux = matrix
	while(True):
		C = np.dot(matrix,matrixAux)
		D = matrixAux[0][0] - C[0][0]
		if (abs(D)<epsilon):		
			break		
		matrixAux = C	
		i = i+1	
	return C

'''Main program.'''
def process(initial):
  
    arcNow = initial
    transitionWay = []
    arcLista = [arcNow]
    gambir = 1
    prob = 1

    while (True):
        if arcNow == "Start":
            arc = np.random.choice(arcsName[0],replace=True,p=transitionMatrix[0])
            transitionWay.append(arc)
            if arc == "SS":
                prob = prob * 0.0
                arcNow = "Start"
                arcLista.append("Start")
            elif arc == "SW":
                prob = prob * 0.2
                arcNow = "Withdraw"
                arcLista.append("Withdraw")

            elif arc == "SC":
                prob = prob * 0.3
                arcNow = "Check"
                arcLista.append("Check")                
            elif arc == "SD":
                prob = prob * 0.5
                arcNow = "Deposit"
                arcLista.append("Deposit")
            else:
                prob = prob * 0.0
                arcNow = "End"
                arcLista.append("End")

        elif arcNow == "Withdraw":
            arc = np.random.choice(arcsName[1],replace=True,p=transitionMatrix[1])
            transitionWay.append(arc)
            if arc == "WS":
                prob = prob * 0.2
                arcNow = "Start"		
                arcLista.append("Start")
            elif arc == "WW":
                prob = prob * 0.0
                arcNow = "Withdraw"
                arcLista.append("Withdraw")

            elif arc == "WC":
                prob = prob * 0.4
                arcNow = "Check"
                arcLista.append("Check")                
            elif arc == "WD":
                prob = prob * 0.0
                arcNow = "Deposit"
                arcLista.append("Deposit")
            else:
                prob = prob * 0.4
                arcNow = "End"
                arcLista.append("End")

        elif arcNow == "Check":
            arc = np.random.choice(arcsName[2],replace=True,p=transitionMatrix[2])
            transitionWay.append(arc)
            if arc == "CS":
                prob = prob * 0.0
                arcNow = "Start"
                arcLista.append("Start")
            elif arc == "CW":
                prob = prob * 0.6
                arcNow = "Withdraw"
                arcLista.append("Withdraw")

            elif arc == "CC":
                prob = prob * 0.0
                arcNow = "Check"
                arcLista.append("Check")                
            elif arc == "CD":
                prob = prob * 0.2
                arcNow = "Deposit"
                arcLista.append("Deposit")
            else:
                prob = prob * 0.2
                arcNow = "End"
                arcLista.append("End")

        elif arcNow == "Deposit":
            arc = np.random.choice(arcsName[3],replace=True,p=transitionMatrix[3])
            transitionWay.append(arc)
            if arc == "DS":
                prob = prob * 0.5
                arcNow = "Start"
                arcLista.append("Start")
            elif arc == "DW":
                prob = prob * 0.0
                arcNow = "Withdraw"
                arcLista.append("Withdraw")

            elif arc == "DC":
                prob = prob * 0.1
                arcNow = "Check"
                arcLista.append("Check")                
            elif arc == "DD":
                prob = prob * 0.0
                arcNow = "Deposit"
                arcLista.append("Deposit")
            else:
                prob = prob * 0.4
                arcNow = "End"
                arcLista.append("End")
        
        else:
            arc = np.random.choice(arcsName[4],replace=True,p=transitionMatrix[4])
            transitionWay.append(arc)
            if arc == "ES":
                prob = prob * 0.6
                arcNow = "Start"
                arcLista.append("Start")
            elif arc == "EW":
                prob = prob * 0.0
                arcNow = "Withdraw"
                arcLista.append("Withdraw")

            elif arc == "EC":
                prob = prob * 0.4
                arcNow = "Check"
                arcLista.append("Check")                
            elif arc == "ED":
                prob = prob * 0.0
                arcNow = "Deposit"
                arcLista.append("Deposit")
            else:
                prob = prob * 0.0
                arcNow = "End"
                arcLista.append("End")
        if arcNow == "Start":
            break
    return [transitionWay,prob],[arcLista,prob]

List_transitions = []
List_states = []
stop = 0.0
count = 0.0

i = 0

'''Writing the test cases.'''
while stop<0.95:
	sequence_arc,sequence_state = process("Start")
	if sequence_arc in List_transitions:
		pass
	else:
		List_transitions.append(sequence_arc)
		List_states.append(sequence_state) 
		stop = stop + sequence_arc[1]

percent = stop*100

print percent,"% of test cases found."
List_transitions.sort(key=lambda x:x[1],reverse=True)
List_states.sort(key=lambda x:x[1],reverse=True)

outF = open("arcs.txt", "w")
print >>outF, "Test cases showing the arcs traveled with their respective probabilities:\n"
for line in List_transitions:
  print >>outF, line
outF.close()

outFF = open("states.txt", "w")
print >>outFF, "Test cases showing the states traveled with their respective probabilities:\n"
for line in List_states:
  print >>outFF, line
outF.close()


