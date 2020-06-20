import pygame
import sys
import time
print("hello game")

GREEN = (100, 25,30)

# initiate the game
(width, height) = (700, 500)
screen = pygame.display.set_mode((width, height))
pygame.init()
screen.fill(GREEN)
pygame.display.set_caption("Sudoku")
pygame.display.update()
running = True

# draw any grid (9X9)
def drawgrid(k,l,m,n):
    i = k
    while i <= m:
        j = l
        while j <= n:
            x = 1
            y = 1
            if j in [l, l + 90, l + 180, l + 270]: x = 5
            pygame.draw.line(screen, (255, 255, 255), (i, j), (m, j), x)
            if i in [k, k + 90, k + 180, k + 270]: y = 5
            pygame.draw.line(screen, (255, 255, 255), (i, j), (i, n), y)
            pygame.display.update()
            # time.sleep(0.01)
            j = j + 30
        i = i + 30

# get list of numbers for drawing numbers
def getgrid(grid1):
    nlist = []
    for c1 in range(0,9):
        for r1 in range(0,9):
            nlist.append(grid1[c1][r1])
    return nlist

# get list of coordinates for drawing numbers
def getcoord(k,l):
    cordlist = []
    i = k
    while i < k+270:
        j = l
        while j < l+270:
            (xcord, ycord) = (j+7,i+7)
            cordlist.append((xcord,ycord))
            pygame.display.update()
            time.sleep(0.01)
            j = j + 30
        i = i + 30
    return cordlist

#draw a grid with numbers
def printgrid(numlist, cordlist):
    for counting in range(0,81):
        font = pygame.font.Font('freesansbold.ttf', 20)
        str1 = str(numlist[counting])
        if numlist[counting] == 0: str1 = " "
        text = font.render(str1, True, (0,255,255))
        screen.blit(text, (cordlist[counting]))
        pygame.display.update()

def printgrid2(numlist, cordlist):
    for counting in range(0,81):
        font = pygame.font.Font('freesansbold.ttf', 20)
        str1 = str(numlist[counting])
        if numlist[counting] == 0: str1 = " "
        text = font.render(str1, True, (0,255,0))
        screen.blit(text, (cordlist[counting]))
        pygame.display.update()


def getrowitems(i,j):
    #get and return array of unique numbers in the row
    numarray = []
    numarray = endgrid[i]
    return numarray

def getcolitems(i,j):
    #get and return array of unique numbers in the columns
    numtemp = []
    numarray = []
    for m in range(0, 9):
        numtemp.append(endgrid[m][j])
    numarray = numtemp
    return numarray


def getminigriditems(i,j):
    if i in [0, 1, 2]: rowval = [0, 1, 2]
    if i in [3, 4, 5]: rowval = [3, 4, 5]
    if i in [6, 7, 8]: rowval = [6, 7, 8]
    if j in [0, 1, 2]: colval = [0, 1, 2]
    if j in [3, 4, 5]: colval = [3, 4, 5]
    if j in [6, 7, 8]: colval = [6, 7, 8]
    numtemp = []
    numarray = []
    for row in rowval:
        for col in colval:
            numtemp.append(endgrid[row][col])
    for item in numtemp:
        if item not in numarray:
            numarray.append(item)
    return numarray

def getsuperset(num1, num2, num3, num4, num5):
    superarray = []
    for item in num1:
        if item not in superarray:
            superarray.append(item)
    for item in num2:
        if item not in superarray:
            superarray.append(item)
    for item in num3:
        if item not in superarray:
            superarray.append(item)
    for item in num4:
        if item not in superarray:
            superarray.append(item)
    for item in num5:
        if item not in superarray:
            superarray.append(item)
    return superarray


def getsolutionsuperset(array1):
    solutionset = []
    for m in range (1,10):
        if m not in array1:
            solutionset.append(m)
    return solutionset

def SolveByElimination(numarray):
    solutionarray = []
    solutionarray = numarray
    # solutionarray = getsolutionfromsuperset(getsuperset(getrowitems(i,j), getcolitems(i,j), getminigriditems(i,j), [], []))
    solutionval = 0
    if len(solutionarray) == 1:
        solutionval = solutionarray[0]
    return solutionval

def getcolgriditems(i,j):
    if j in [0, 1, 2]: colval = [0, 1, 2]
    if j in [3, 4, 5]: colval = [3, 4, 5]
    if j in [6, 7, 8]: colval = [6, 7, 8]
    numarray1 = []
    numarray2 = []
    numarray3 = []
    numarray1 = (getcolitems(i,colval[0]))
    numarray2 = (getcolitems(i,colval[1]))
    numarray3 = (getcolitems(i,colval[2]))
    for m in range(1,10):
        presentinfirstarray = False
        presentinsecondarray = False
        presentinthirdarray = False
        if m in numarray1: presentinfirstarray = True
        if m in numarray2: presentinsecondarray = True
        if m in numarray3: presentinthirdarray = True
        # print(numarray1, numarray2, numarray3, m, presentinfirstarray, presentinsecondarray, presentinthirdarray)

    return


def SolveByColGrid(i,j):
    solutionval = 0
    solutionval = endgrid[i][j]
    getcolgriditems(i,j)
    return solutionval

# startgrid = [[0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         ]

#
# startgrid = [[7,0,3,0,0,0,2,0,4],
#         [2,0,8,0,4,5,0,0,6],
#         [4,9,0,8,0,0,1,5,7],
#         [0,0,0,3,7,0,0,0,5],
#         [0,7,0,5,0,1,9,0,0],
#         [0,0,5,0,2,9,7,0,0],
#         [5,0,1,9,0,0,6,7,0],
#         [0,0,9,2,0,0,0,0,1],
#         [0,0,0,6,1,3,0,4,9],
#         ]


startgrid = [[0,8,5,3,1,9,0,0,0],
        [0,0,0,0,5,2,6,0,0],
        [4,0,3,0,0,0,9,0,0],
        [0,0,9,0,0,0,8,0,0],
        [0,0,0,0,2,7,0,0,0],
        [0,3,4,1,0,8,0,0,0],
        [8,0,6,0,0,4,0,3,0],
        [0,0,0,2,0,0,0,0,8],
        [0,9,0,8,3,5,7,0,0],
        ]


startgrid = [[2,0,0,7,0,0,8,0,0],
        [0,3,4,0,9,0,0,0,1],
        [6,0,0,0,0,0,0,0,0],
        [0,0,8,0,2,7,0,0,9],
        [0,0,2,9,0,5,0,0,6],
        [0,9,0,0,8,0,0,5,2],
        [9,0,0,0,0,0,0,0,0],
        [0,0,3,2,0,6,0,9,0],
        [0,0,1,0,4,0,6,0,0],
        ]


endgrid = startgrid



#starting grid

orgGrid = drawgrid(30, 30, 300, 300)
orglist = getgrid(startgrid)
startcoordlist = getcoord(30,30)
printgrid(orglist, startcoordlist)





#solution grid
def refreshgrid():
    sidegrid = drawgrid(330, 30, 600, 300)
    endlist = getgrid(endgrid)
    endcoordlist = getcoord(30,330)
    printgrid(endlist, endcoordlist)
    pygame.display.update()
    # time.sleep(0.05)

refreshgrid()

##testing solving

#
# def trysolving(a,b):
#         value = solvefor(a,b)
#         endgrid[a][b] = value
#
#
solved = False
endlist = getgrid(endgrid)
iterations = 1
countofzeroes = 0
if 0 in endlist:
    for item in endlist:
        if item == 0: countofzeroes = countofzeroes +1
    print("count of zeroes =", countofzeroes)
while solved == False and iterations < 10:
        for i in range(0,9):
            for j in range(0,9):
                if endgrid[i][j] == 0:
                    newvalue = SolveByElimination(getsolutionsuperset(getsuperset(getcolitems(i,j), getrowitems(i,j), getminigriditems(i,j),[],[])))
                    endgrid[i][j]= newvalue
        endlist = getgrid(endgrid)
        for i in range(0,9):
            for j in range(0,9):
                if endgrid[i][j] ==0:
                    newvalue = SolveByColGrid(i,j)
                    endgrid[i][j]= newvalue
        for i in range(0,9):
            for j in range(0,9):
                if endgrid[i][j] ==0:
                    minigridcount = []
                    minigridcount = getminigriditems(i,j)
                    count = 0
                    for items in minigridcount:
                        if item !=0:
                            count = count + 1
                        if count == 1:
                            newvalue = SolveByElimination(getsolutionsuperset(
                                getsuperset(getminigriditems(i, j), [],[], [], [])))
                            endgrid[i][j] = newvalue
        for i in range(0,9):
            for j in range(0,9):
                if endgrid[i][j] ==0:
                    colcount = []
                    colcount = getcolitems(i,j)
                    count = 0
                    for items in colcount:
                        if item !=0:
                            count = count + 1
                        if count == 1:
                            newvalue = SolveByElimination(getsolutionsuperset(
                                getsuperset(getcolitems(i, j), [],[], [], [])))
                            endgrid[i][j] = newvalue
        for i in range(0,9):
            for j in range(0,9):
                if endgrid[i][j] ==0:
                    rowcount = []
                    rowcount = getrowitems(i,j)
                    count = 0
                    for items in rowcount:
                        if item !=0:
                            count = count + 1
                        if count == 1:
                            newvalue = SolveByElimination(getsolutionsuperset(
                                getsuperset(getrowitems(i, j), [],[], [], [])))
                            endgrid[i][j] = newvalue
        if 0 in endlist:
            countofzeroes = 0
            for item in endlist:
                if item == 0: countofzeroes = countofzeroes+1
            print("count of zeroes =", countofzeroes, " iterations: ", iterations)
            solved = False
            iterations = iterations+ 1
            # refreshgrid()
        if 0 not in endlist:
            print("solved")
            solved = True

print("i tried")


print(endgrid)
refreshgrid()



#### keep game live

while running == True:
    pygame.mouse.get_cursor()
    for event in pygame.event.get():
        if event.type == 12:
            pygame.quit()
            sys.exit()
            running = False

