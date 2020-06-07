import tkinter

def onClick(event):
    global activePiece, activeLocation, valid, board
    #print(event.x+" "+event.y)
    x=int(event.x//drawScale)
    y=int((winSize-event.y)//drawScale)
    print(board[x][y])
    if(board[x][y]//16 ==  activePlayer):
        activePiece = board[x][y]
        activeLocation = [x, y]
        print("selected piece")
        updateValidMoves()
        print(valid)
    elif [x,y] in valid:
        board[x][y] = activePiece
        board[activeLocation[0]][activeLocation[1]] = -1
        activeLocation = [x, y]
        valid = []
        print("moved piece")
    draw()

def draw():
    c.delete("ALL")
    for x in range(boardSize):
        for y in range(boardSize):
            if(board[x][y]==-2):
                c.create_rectangle(x*drawScale, winSize-y*drawScale, (x+1)*drawScale, winSize-(y+1)*drawScale, fill = "#777777")
            else:
                c.create_rectangle(x*drawScale, winSize-y*drawScale, (x+1)*drawScale, winSize-(y+1)*drawScale, fill = boardcols[(x+y)%2])
                if(activePiece == board[x][y]):
                    c.create_rectangle(x*drawScale, winSize-y*drawScale, (x+1)*drawScale, winSize-(y+1)*drawScale, fill = highlightcol)
                elif([x,y] in valid):
                    c.create_rectangle(x*drawScale, winSize-y*drawScale, (x+1)*drawScale, winSize-(y+1)*drawScale, fill = validMovescol)
                else:
                    c.create_rectangle(x*drawScale, winSize-y*drawScale, (x+1)*drawScale, winSize-(y+1)*drawScale, fill = boardcols[(x+y)%2])
                if(board[x][y]!=-1):
                    c.create_text((x+0.5)*drawScale, winSize-(y+0.5)*drawScale, text = pieceMap[board[x][y]%16], fill = cols[board[x][y]//16], font = ("helvetica", 24))
        
def updateValidMoves():
    global valid
    piece = activePiece%16
    valid = []
    if piece == 0 or piece == 14 or piece == 6:#rooks
        print("Checing valid rook")
        notFinnished = True
        c = 1
        while notFinnished:
            #print(board[activeLocation[0]][activeLocation[1]+c])
            if activeLocation[0]+c<boardSize and board[activeLocation[0]+c][activeLocation[1]]==-1:
                valid.append([activeLocation[0]+c,activeLocation[1]])
                c+=1
            else:
                notFinnished = False
        notFinnished = True
        c = 1
        while notFinnished:
            if activeLocation[0]-c>=0 and board[activeLocation[0]-c][activeLocation[1]]==-1:
                valid.append([activeLocation[0]-c,activeLocation[1]])
                c+=1
            else:
                notFinnished = False
        notFinnished = True
        c = 1
        while notFinnished:
            if activeLocation[1]+c<boardSize and board[activeLocation[0]][activeLocation[1]+c]==-1:
                valid.append([activeLocation[0],activeLocation[1]+c])
                c+=1
            else:
                notFinnished = False
        notFinnished = True
        c = 1
        while notFinnished:
            if activeLocation[1]-c>=0 and board[activeLocation[0]][activeLocation[1]-c]==-1:
                valid.append([activeLocation[0],activeLocation[1]-c])
                c+=1
            else:
                notFinnished = False
    if piece == 4 or piece == 10 or piece == 6:#bishops
        notFinnished = True
        c = 1
        while notFinnished:
            if activeLocation[0]+c>=0 and activeLocation[1]+c<boardSize and board[activeLocation[0]+c][activeLocation[1]+c]==-1:
                valid.append([activeLocation[0]+c,activeLocation[1]+c])
                c+=1
            else:
                notFinnished = False
        notFinnished = True
        c = 1
        while notFinnished:
            if activeLocation[0]-c>=0 and activeLocation[1]+c<boardSize and board[activeLocation[0]-c][activeLocation[1]+c]==-1:
                valid.append([activeLocation[0]-c,activeLocation[1]+c])
                c+=1
            else:
                notFinnished = False
        notFinnished = True
        c = 1
        while notFinnished:
            if activeLocation[0]+c>=0 and activeLocation[1]-c<boardSize and board[activeLocation[0]+c][activeLocation[1]-c]==-1:
                valid.append([activeLocation[0]+c,activeLocation[1]-c])
                c+=1
            else:
                notFinnished = False
        notFinnished = True
        c = 1
        while notFinnished:
            if activeLocation[1]-c>=0 and activeLocation[1]-c>=0 and board[activeLocation[0]-c][activeLocation[1]-c]==-1:
                valid.append([activeLocation[0]-c,activeLocation[1]-c])
                c+=1
            else:
                notFinnished = False
    elif piece%2 == 1:
        if activePlayer == 0:
            valid.append([activeLocation[0], activeLocation[1]+1])
            if activeLocation[1] == 1:
                valid.append([activeLocation[0], activeLocation[1]+2])
        if activePlayer == 1:
            valid.append([activeLocation[0]+1, activeLocation[1]])
            if activeLocation[0] == 1:
                valid.append([activeLocation[0]+2, activeLocation[1]])
        if activePlayer == 2:
            valid.append([activeLocation[0], activeLocation[1]-1])
            if activeLocation[1] == 12:
                valid.append([activeLocation[0], activeLocation[1]-2])
        if activePlayer == 3:
            valid.append([activeLocation[0]-1, activeLocation[1]])
            if activeLocation[0] == 12:
                valid.append([activeLocation[0]-2, activeLocation[1]])
        
        

winSize = 700

innerSize = 8
wingSize = 3#min 2
boardSize = innerSize + 2 * wingSize

drawScale = winSize/boardSize

boardcols = ["#fffdd0", "#654321"]
highlightcol = "#0099ff"
validMovescol = "#00ff99"
cols = ["#551111", "#115511", "#111155", "#000000"]

pieceMap = ["R", "P", "H", "P", "B", "P", "Q", "P", "K", "P", "B", "P", "H", "P", "R", "P"]

board = []
valid = []

activePlayer = 0
activePiece = 0
activeLocation = [3,0]

for x in range(boardSize):
    board.append([])
    for y in range(boardSize):
        board[x].append(-1)
for x in range(wingSize):
    for y in range(wingSize):
        board[x][y] = -2
        board[boardSize-1-x][y] = -2
        board[boardSize-1-x][boardSize-1-y] = -2
        board[x][boardSize-1-y] = -2

for x in range(8):
    for y in range(2):
        board[wingSize+x][y] = 2*x+y
        board[y][boardSize-1-(wingSize+x)] = 2*x+y+16
        board[boardSize-x-1-wingSize][boardSize-y-1] = 2*x+y+32
        board[boardSize-y-1][x+wingSize] = 2*x+y+48

for i in board:
    print(i)

tk = tkinter.Tk()
tk.bind("<Button-1>", onClick)
c = tkinter.Canvas(tk, width = winSize, height = winSize)
c.pack()
draw()
tk.mainloop()
