#***********************************************************************************************
# Bioinformatics final project
# programming assignment: Option A, project 2
#
# Write a program that finds the optimal pairwise
# alignment between two sequences specified by the user.
#
# Project by: Derek Manierre and Brandon Klett
#***********************************************************************************************
import re

def reverse(list1=[],*args):
    reverseList=[]
    for each in range(len(list1),1,-1):
        reverseList.append(list1[each])

    return reverseList
def inputType():
#This function will determine if the user wants to input their own sequences or read in from a file
    initialInput = 0
    check = False

    while(check == False):

        initialInput = input("Would you like to: \n 1:Enter your own sequences \n 2:Read sequences from a file\n")
        initialInput = int(initialInput)

        if(initialInput == 1 or initialInput == 2):
            check = True

    return initialInput

def toList(string):
#This function splits a string into an individual character array
    temp = []

    for c in string:
        temp.append(c)

    return temp

def checkLength(seq1 = [], seq2 = [], *args):
#Checks the lengths of the sequences to see how they need to be adjusted
    if len(seq1) == len(seq2):
        return 0
    elif(len(seq1) > len(seq2)):
        return (len(seq1)-len(seq2))
    else:
        return (len(seq2)-len(seq1))

def isMatch(x,y):
#Checks if sequence items match
    if(x == y):
        return True
    else:
        return False

def makeMatrix(x,y):
    #creates empty matrix
    matrix = [[0 for z in range(x+2)]for w in range(y+2)]

    return matrix

def setMatix(x,y,seq1, seq2, matrix,*args):
    #fills empty matrix with incoming sequences and sets gap penalties


    for a in range(x):
        matrix[a+2][1] = (matrix[a+1][1])-4

    for b in range(y):
        matrix[1][b+2] = (matrix[1][b+1])-4

    for c in range(x):
        matrix[c+2][0] =seq1[c]

    for d in range(y):
        matrix[0][d+2] = seq2[d]
    return matrix


def fillMatrix(x,y,matrix, *args):
    # preforms the calculations for the matrix
        #checks for matches
        for row in range(2, x+2):
            for col in range(2, y+2):
                if(matrix[row][0] == matrix[0][col]):
                    top = int(matrix[row-1][col]) + 3
                    diag = int(matrix[row-1][col-1]) + 3
                    side = int(matrix[row][col-1]) + 3
                    #Preforms comparisons
                    if top > diag and top > side:
                        matrix[row][col] = '{:>3}'.format(str(top))
                    elif top >= diag and top >= side:
                        matrix[row][col] = '{:>3}'.format(str(top))
                    elif diag > top and diag > side:
                        matrix[row][col] = '{:>3}'.format(str(diag))
                    elif diag >= top and diag >= side:
                        matrix[row][col] = '{:>3}'.format(str(diag))
                    else:
                        matrix[row][col] = '{:>3}'.format(str(side))
                        #takes care of appended array
                elif (matrix[row][0] == '-' or matrix[0][col] == '-'):
                    matrix[row][col] = '-'
            #checks for mismatches/ gaps
                elif(matrix[row][0] != matrix[0][col]):
                    top = int(matrix[row-1][col]) - 4
                    diag = int(matrix[row-1][col-1]) -1
                    side = int(matrix[row][col-1]) - 4
            #preforms comparisons
                    if top > diag and top > side:
                        matrix[row][col] = '{:>3}'.format(str(top))
                    elif top >= diag and top >= side:
                        matrix[row][col] = '{:>3}'.format(str(top))
                    elif diag > top and diag > side:
                        matrix[row][col] = '{:>3}'.format(str(diag))
                    elif diag >= top and diag >= side:
                        matrix[row][col] = '{:>3}'.format(str(diag))
                    else:
                        matrix[row][col] = '{:>3}'.format(str(side))
            #matrix[x + 1][y - 1] = matrix[x + 1][y + 1]
        return matrix

def traceBack(x,y,a,b,matrix,*args):
#Find the optimal allignemnt and score
    alignmentTop = ""
    alignmentBottom = ""
    score  = matrix[a+1][b+1]
    row = a+1
    col = b+1


    while row + col != 2:
        while (matrix[row][col] == '-'):
            if (matrix[row][0] == '-'):
                row -=1
            if (matrix[0][col] == '-'):
                col -=1
        if(int(matrix[row][col]) + 4 == int(matrix[row-1][col])): #added in the "row -1 != 0 to stop it from calculating letter
            alignmentTop = alignmentTop + matrix[row][0]
            alignmentBottom = alignmentBottom + "-"
            row = row - 1

        elif (int(matrix[row][col]) + 4 == int(matrix[row][col-1])): #added in the "row -1 != 0 to stop it from calculating letter
            alignmentTop = alignmentTop + "-"
            alignmentBottom = alignmentBottom + matrix[0][col]
            col = col - 1
        else:
            alignmentBottom = alignmentBottom + str(matrix[0][col])
            alignmentTop = alignmentTop + str(matrix[row][0])
            row = row-1
            col = col-1


    print("The optimal alignment score is: ", score)
    print("The optimal alignment is: ")
    print(alignmentTop[::-1])
    print(alignmentBottom[::-1])

def findScore(a,b,seq1 = [], seq2 = [], *args):
#Finds and outputs the optimal alignment score and alignment for the two sequences
    matchScore = 0

    matrix = makeMatrix(len(seq1),len(seq2))
    matrix = setMatix(len(seq1),len(seq2),seq1,seq2,matrix)

    matrix = fillMatrix(len(seq1),len(seq2),matrix)


    for each in matrix:
        print(each)


    traceBack(len(seq1),len(seq2),a,b,matrix)


#Start of the Program
print("Welcome to the pairwise alignment program!")

choice = inputType()
while(choice != 1 and choice != 2):

        choice = inputType()

if(choice == 1):

    #Get the sequences from the user and set all to capital letters

    seq_string1 = input("Please enter your first sequence (Up to 100 bases):\n")
    seq_string2 = input("Please enter your second sequence (Up to 100 bases):\n")

    seq_string1 = seq_string1.upper()
    seq_string2 = seq_string2.upper()

   #Separate the sequences into their own lists
    seq1 = toList(seq_string1)
    seq2 = toList(seq_string2)

    a = len(seq1)
    b = len(seq2)

    #Make the sequences the same length to avoid out of bound errors
    adjust = checkLength(seq1,seq2)
    if(adjust != 0):
        if(len(seq1) > len(seq2)):
            for x in range(0,adjust):
                seq2.append("-")
        else:
            for x in range(0,adjust):
                seq1.append("-")

    findScore(a,b,seq1,seq2)
else:
#Get the name of the file containing the sequences and read them in
    fileName = input("Please enter the file name: ")

    f = open(fileName)

    fileInput = f.read()

#Make sure the sequences in the file are split by a | with no spaces and they will be split to separate arrays
    sequences = re.split(r'\|',fileInput)

    sequences[0] = sequences[0].upper()
    sequences[1] = sequences[1].upper()
    seq1 = toList(sequences[0])
    seq2 = toList(sequences[1])

    a = len(seq1)
    b = len(seq2)
    adjust = checkLength(seq1,seq2)
    if(adjust != 0):
        if(len(seq1) > len(seq2)):
            for x in range(0,adjust):
                seq2.append(" ")
        else:
            for x in range(0,adjust):
                seq1.append(" ")

    findScore(a,b,seq1,seq2)