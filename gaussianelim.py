import math
import numpy as np
import sys

def solveable(linearmatrix):   #using numpy to check discriminant of matrix
    #converting to a 2d array for numpy
    size = math.floor(len(linearmatrix)**0.5)
    matrix = [[(linearmatrix[((size+1)*row)+col])for col in range(size)] for row in range(size)]
    det = np.linalg.det(matrix)
    return (det != 0) #true if it can be solved
    
    
def clear(): #for display
    for i in range(50): print()

def fillmatrix(unknowns, variableNames):
    
    matrix = [0]*((unknowns+1)*unknowns) # creating empty matrix
    #printequation(matrix, variableNames)
    printequation(matrix, variableNames)
    for coordinate in range(unknowns*(unknowns+1)): #user filling it out every entry
        row = coordinate//unknowns
        column = coordinate%(unknowns+1)
        print("enter the next value for index ", column+1, " in row ", row)
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
                print(" - ", abs(currentvalue), variableNames[currentcol], end="")  #checking to see if we write + or - before the next entry
            if currentvalue==0:
                print(" + 0   ", end="")
        else:
            print(" = ", currentvalue)

def makezero(matrix, row1, row2, index):
    size = math.floor(len(matrix)**0.5)
    coefficient = -(matrix[(row2*(size+1))+index])/matrix[(row1*(size+1))+index]    #this is what we multiply the row by to cancel the required entry
    print()
    print("we will add ", coefficient, " times row ", row1+1, " to row ", row2+1)
    print("this gives us a 0 at column ", index+1, " in row ", row2+1)
    newrow = [(matrix[(row2*(size+1))+i] + coefficient*matrix[(row1*(size+1))+i]) for i in range(size+1)]
    for i in range(size+1):
        matrix[(row2*(size+1))+i] = newrow[i]
    return matrix

def backsubstitute(matrix, row, index, variableNames):
    size = math.floor(len(matrix)**0.5)
    print("row ", row+1, " gives us ", variableNames[index], " = ", matrix[(row*(size+1))+size]/matrix[(row*(size+1))+index])  #quick division to display the variable, we do not actually care about finding it now
    print("which we can substitute into the other rows")
    for i in range(row):
        coefficient = -(matrix[(i*(size+1))+index]/matrix[(row*(size+1))+index])
        matrix[((i*(size+1))+index)] += coefficient*matrix[(row*(size+1))+index]  #basically our row cancellation code but with less work
        matrix[((i*(size+1))+size)] += coefficient*matrix[(row*(size+1))+size]
    
    
    return matrix

def displayResults(matrix, variableNames):
    size = math.floor(len(matrix)**0.5)
    print()
    print("Hence") # hence
    for i in range(size):
        print(variableNames[i], " = ", matrix[(i*(size+1))+size]/matrix[(i*(size+1))+i]) #by this stage each row should only have one variable nonzero
    
    
    
    
variableNames = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"     #all the letters I can assign to variables
                                                                           #neater than unreadable unicode numbers
                                                                           #we could set this to other stuff like xyzabcpqrfghk, etc
                                                                         

print("how many unknowns do you want to solve for? (max 52 to label variables)") #only really limited by the amount of characters we can use to represent variables
unknowns = int(input())

system = fillmatrix(unknowns, variableNames)  #user inputs matrix here

if not solveable(system):
    print("this system of equations does not have a solution")
    sys.exit()

for i in range(unknowns-1):
    for j in range(i+1, (unknowns)):
        if system[((unknowns+1)*j)+i] != 0:
            system = makezero(system, i, j, i)
            printequation(system, variableNames)  #creates 0 under the leading diagonal, allowing for back substitution

for i in range(1, unknowns):
    system = backsubstitute(system, unknowns-i, unknowns-i, variableNames)  #back-substitutes variables starting with the last one, ends up with only one variable per row and ready for solving
    printequation(system, variableNames)

displayResults(system, variableNames)










