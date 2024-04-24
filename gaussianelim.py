import math
import numpy as np

def solveable(linearmatrix):
    #converting to an array for numpy
    size = math.floor(len(linearmatrix)**0.5)
    matrix = [[(linearmatrix[((size+1)*row)+col])for col in range(size)] for row in range(size)]
    det = np.linalg.det(matrix)
    
    
    
def clear():
    for i in range(50): print()

def fillmatrix(unknowns, variableNames):
    
    matrix = [0]*((unknowns+1)*unknowns)
    #printequation(matrix, variableNames)
    printequation(matrix, variableNames)
    for coordinate in range(unknowns*(unknowns+1)):
        row = coordinate//unknowns
        column = coordinate%(unknowns+1)
        print("enter the next value for index ", column+1, " in row ", row+1)
        matrix[coordinate] = int(input())
        clear()
        printequation(matrix, variableNames)
        #print(matrix)
    return matrix
            

            
def printequation(linearmatrix, variableNames):
    size = math.floor(len(linearmatrix)**0.5)
    print()
    for i in range(len(linearmatrix)):
        currentcol = i%(size+1)
        currentvalue = linearmatrix[i]
        if currentcol != size:
            if currentvalue>0:
                print(" + ", currentvalue, variableNames[currentcol], end="")
            if currentvalue<0:
                print(" - ", abs(currentvalue), variableNames[currentcol], end="")
            if currentvalue==0:
                print(" + 0   ", end="")
        else:
            print(" = ", currentvalue)

def makezero(matrix, row1, row2, index):
    size = math.floor(len(matrix)**0.5)
    coefficient = -(matrix[(row2*(size+1))+index])/matrix[(row1*(size+1))+index]
    print()
    print("we will add ", coefficient, " times row ", row1+1, " to row ", row2+1)
    print("this gives us a 0 at column ", index+1, " in row ", row2+1)
    newrow = [(matrix[(row2*(size+1))+i] + coefficient*matrix[(row1*(size+1))+i]) for i in range(size+1)]
    for i in range(size+1):
        matrix[(row2*(size+1))+i] = newrow[i]
    return matrix

def backsubstitute(matrix, row, index, variableNames):
    size = math.floor(len(matrix)**0.5)
    print("row ", row+1, " gives us ", variableNames[index], " = ", matrix[(row*(size+1))+size]/matrix[(row*(size+1))+index])
    print("which we can substitute into the other rows")
    for i in range(row):
        coefficient = -(matrix[(i*(size+1))+index]/matrix[(row*(size+1))+index])
        matrix[((i*(size+1))+index)] += coefficient*matrix[(row*(size+1))+index]
        matrix[((i*(size+1))+size)] += coefficient*matrix[(row*(size+1))+size]
    
    
    return matrix

def displayResults(matrix, variableNames):
    size = math.floor(len(matrix)**0.5)
    print()
    print("Hence")
    for i in range(size):
        print(variableNames[i], " = ", matrix[(i*(size+1))+size]/matrix[(i*(size+1))+i])
    
    
    
    
variableNames = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"     #all the letters I can assign to variables
                                                                           #neater than unreadable unicode numbers
                                                                         

print("how many unknowns do you want to solve for? (max 52 to label variables)")
unknowns = int(input())

system = fillmatrix(unknowns, variableNames)

for i in range(unknowns-1):
    for j in range(i+1, (unknowns)):
        if system[((unknowns+1)*j)+i] != 0:
            system = makezero(system, i, j, i)
            printequation(system, variableNames)

for i in range(1, unknowns):
    system = backsubstitute(system, unknowns-i, unknowns-i, variableNames)
    printequation(system, variableNames)

displayResults(system, variableNames)










