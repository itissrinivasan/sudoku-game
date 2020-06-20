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


startgrid = [[7,0,3,0,0,0,2,0,4],
        [2,0,8,0,4,5,0,0,6],
        [4,9,0,8,0,0,1,5,7],
        [0,0,0,3,7,0,0,0,5],
        [0,7,0,5,0,1,9,0,0],
        [0,0,5,0,2,9,7,0,0],
        [5,0,1,9,0,0,6,7,0],
        [0,0,9,2,0,0,0,0,1],
        [0,0,0,6,1,3,0,4,9],
        ]


endgrid = startgrid

# def getrowandCol(i,j):
#     num1 = []
#     num1 = endgrid[i]
#     # print(num1)
#     # text1 = input("say ok: ")
#     num2 = []
#     for m in range(0,9):
#         num2.append(endgrid[m][j])
#     # print(num2)
#     # text1 = input("say ok: ")
#     colrange = []
#     rowrange = []
#     if i in [0,1,2]: rowrange = [0,1,2]
#     if i in [3,4,5]: rowrange = [3,4,5]
#     if i in [6,7,8]: rowrange = [6,7,8]
#     if j in [0, 1, 2]: colrange = [0, 1, 2]
#     if j in [3, 4, 5]: colrange = [3, 4, 5]
#     if j in [6, 7, 8]: colrange = [6, 7, 8]
#     num3 = []
#     for col in colrange:
#         for row in rowrange:
#             num3.append(endgrid[row][col])
#     uniquenums = []
#     # print(num3)
#     for item in num1:
#         if item not in uniquenums:
#             uniquenums.append(item)
#     for item in num2:
#         if item not in uniquenums:
#             uniquenums.append(item)
#     for item in num3:
#         if item not in uniquenums:
#             uniquenums.append(item)
#     print(uniquenums)
#     possiblevals = []
#     for vals in range(1,10):
#         if vals not in uniquenums:
#             possiblevals.append(vals)
#     solutionvalue = 0
#     print(possiblevals)
#     if len(possiblevals) == 1:
#         solutionvalue = int(possiblevals[0])
#     print(solutionvalue)
#     return solutionvalue



# def solvefor(i,j):
#     return_val = (endgrid[i][j])
#     print(return_val)
#     if return_val == 0:
#         return_val = getrowandCol(i,j)
#     # print("ret", return_val)
#     # print(endgrid)
#     return return_val
#


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
iterations = 0
while solved == False and iterations < 10:
        for i in range(0,9):
            for j in range(0,9):
                if endgrid[i][j] == 0:
                    num1 = endgrid[i]
                    num2 = []
                    for m in range(0,9):
                        num2.append(endgrid[m][j])
                    num3 = []
                    if i in [0,1,2]: rowval = [0,1,2]
                    if i in [3,4,5]: rowval = [3,4,5]
                    if i in [6, 7, 8]: rowval = [6, 7, 8]
                    if j in [0, 1, 2]: colval = [0, 1, 2]
                    if j in [3, 4, 5]: colval = [3, 4, 5]
                    if j in [6, 7, 8]: colval = [6, 7, 8]
                    for row in rowval:
                        for col in colval:
                            num3.append(endgrid[row][col])
                    possiblevalues1 = []
                    for item in num1:
                        if item not in possiblevalues1:
                            possiblevalues1.append(item)
                    for item in num2:
                        if item not in possiblevalues1:
                            possiblevalues1.append(item)
                    for item in num3:
                        if item not in possiblevalues1:
                            possiblevalues1.append(item)
                    solutionvalues = []
                    for vals in range(1,10):
                        if vals not in possiblevalues1:
                            solutionvalues.append(vals)
                    newvalue = 0
                    print(num1, num2, num3, possiblevalues1, solutionvalues, newvalue)
                    if len(solutionvalues) == 1:
                        newvalue = solutionvalues[0]
                    endgrid[i][j]= newvalue
        refreshgrid()
        endlist = getgrid(endgrid)
        if 0 in endlist:
            print("0 still there", iterations)
            solved = False
            iterations = iterations+ 1
        if 0 not in endlist:
            print("solved")
            solved = True

print("i tried")


print(endgrid)
refreshgrid()





# print(endlist)
print(endgrid)
refreshgrid()

refreshgrid()


#### keep game live

while running == True:
    pygame.mouse.get_cursor()
    for event in pygame.event.get():
        if event.type == 12:
            pygame.quit()
            sys.exit()
            running = False

