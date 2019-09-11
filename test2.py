import numpy as np
import random as rm

''' Declarando os estados (Exemplo do artigo "Model based Testing for Software Systems: An
Application of Markov Modulated Markov Process"''' 

states = ["Start","Withdraw","Check","Deposit","End"]

# Possible sequences of events
transitionName = [["SS","SW","SC","SD","SE"],["WS","WW","WC","WD","WE"],["CS","CW","CC","CD","CE"],["DS","DW","DC","DD","DE"],["ES","EW","EC","ED","EE"]]

# Probabilities matrix (transition matrix)
transitionMatrix = [[0,0.2,0.3,0.5,0.0],[0.2,0.0,0.4,0.0,0.4],[0.0,0.6,0.0,0.2,0.2],[0.5,0.0,0.1,0.0,0.4],[0.6,0.0,0.4,0.0,0.0]]

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[2])+sum(transitionMatrix[3])+sum(transitionMatrix[4]) != 5:
    print("Distribuicao de probabilidade incorreta!!")

'''Calculando as probabilidades limites'''

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

print probLimit(transitionMatrix)

def process(initial):
  
    activityToday = initial
    transitionWay = []
    activityList = [activityToday]
    gambir = 1
    prob = 1

    while (True):
        if activityToday == "Start":
            change = np.random.choice(transitionName[0],replace=True,p=transitionMatrix[0])
            transitionWay.append(change)
            if change == "SS":
                prob = prob * 0.0
                activityToday = "Start"
                activityList.append("Start")
            elif change == "SW":
                prob = prob * 0.2
                activityToday = "Withdraw"
                activityList.append("Withdraw")

            elif change == "SC":
                prob = prob * 0.3
                activityToday = "Check"
                activityList.append("Check")                
            elif change == "SD":
                prob = prob * 0.5
                activityToday = "Deposit"
                activityList.append("Deposit")
            else:
                prob = prob * 0.0
                activityToday = "End"
                activityList.append("End")

        elif activityToday == "Withdraw":
            change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
            transitionWay.append(change)
            if change == "WS":
                prob = prob * 0.2
                activityToday = "Start"		
                activityList.append("Start")
            elif change == "WW":
                prob = prob * 0.0
                activityToday = "Withdraw"
                activityList.append("Withdraw")

            elif change == "WC":
                prob = prob * 0.4
                activityToday = "Check"
                activityList.append("Check")                
            elif change == "WD":
                prob = prob * 0.0
                activityToday = "Deposit"
                activityList.append("Deposit")
            else:
                prob = prob * 0.4
                activityToday = "End"
                activityList.append("End")

        elif activityToday == "Check":
            change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
            transitionWay.append(change)
            if change == "CS":
                prob = prob * 0.0
                activityToday = "Start"
                activityList.append("Start")
            elif change == "CW":
                prob = prob * 0.6
                activityToday = "Withdraw"
                activityList.append("Withdraw")

            elif change == "CC":
                prob = prob * 0.0
                activityToday = "Check"
                activityList.append("Check")                
            elif change == "CD":
                prob = prob * 0.2
                activityToday = "Deposit"
                activityList.append("Deposit")
            else:
                prob = prob * 0.2
                activityToday = "End"
                activityList.append("End")

        elif activityToday == "Deposit":
            change = np.random.choice(transitionName[3],replace=True,p=transitionMatrix[3])
            transitionWay.append(change)
            if change == "DS":
                prob = prob * 0.5
                activityToday = "Start"
                activityList.append("Start")
            elif change == "DW":
                prob = prob * 0.0
                activityToday = "Withdraw"
                activityList.append("Withdraw")

            elif change == "DC":
                prob = prob * 0.1
                activityToday = "Check"
                activityList.append("Check")                
            elif change == "DD":
                prob = prob * 0.0
                activityToday = "Deposit"
                activityList.append("Deposit")
            else:
                prob = prob * 0.4
                activityToday = "End"
                activityList.append("End")
        
        else:
            change = np.random.choice(transitionName[4],replace=True,p=transitionMatrix[4])
            transitionWay.append(change)
            if change == "ES":
                prob = prob * 0.6
                activityToday = "Start"
                activityList.append("Start")
            elif change == "EW":
                prob = prob * 0.0
                activityToday = "Withdraw"
                activityList.append("Withdraw")

            elif change == "EC":
                prob = prob * 0.4
                activityToday = "Check"
                activityList.append("Check")                
            elif change == "ED":
                prob = prob * 0.0
                activityToday = "Deposit"
                activityList.append("Deposit")
            else:
                prob = prob * 0.0
                activityToday = "End"
                activityList.append("End")
        if activityToday == "Start":
            break
    return [transitionWay,prob]

List_activity = []
stop = 0.0
count = 0.0

i = 0
while stop<0.95:
	sequence = process("Start")
	if sequence in List_activity:
		count = count + 1
	else:
		List_activity.append(sequence) 
		stop = stop + sequence[1]
percent = stop*100
print percent,"% dos caminhos encontrados"
List_activity.sort(key=lambda x:x[1],reverse=True)

outF = open("myOutFile.txt", "w")
for line in List_activity:
  print >>outF, line
outF.close()






