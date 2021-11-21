from tkinter import *


class graph:
    def __init__(self):
        self.root = Tk()
        self.root.title("271 final")
        self.root.bind("<KeyPress-Left>", self.left)
        self.root.bind("<KeyPress-Right>", self.right)
        self.root.bind("<KeyPress-Up>", self.up)
        self.root.bind("<KeyPress-Down>", self.down)
        self.zoom = 50
        self.width = 10 * self.zoom
        self.height = 10 * self.zoom
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        l = Label(self.root, text="    1   2   3   4   5   6   7   8   9", font=("Courier", 16, "bold"))
        l.pack()

        f = open("sokoban01.txt", "r")
        numRows = f.readline().split()
        nWallSquares = f.readline().split()
        nBoxes = f.readline().split()
        nStorageLocations = f.readline().split()
        player = f.readline().split()
        walls = []
        boxes = []
        goals = []
        for i in range(1,int(nWallSquares[0])*2,2):
            walls.append((int(nWallSquares[i]),int(nWallSquares[i+1])))

        for i in range(1,int(nBoxes[0])*2,2):
            boxes.append((int(nBoxes[i]),int(nBoxes[i+1])))

        for i in range(1,int(nStorageLocations[0])*2,2):
            goals.append((int(nStorageLocations[i]),int(nStorageLocations[i+1])))

        for wall in walls:
            self.create_wall(wall[0], wall[1])

        for box in boxes:
            self.create_box(box[0], box[1])

        for goal in goals:
            self.create_goal(goal[0], goal[1])

        self.player = self.create_player(int(player[0]), int(player[1]))

    def create_player(self, x, y):
        r = 30
        x = self.zoom * x
        y = self.zoom * y
        return self.canvas.create_oval(x+10, y+10, x + r+10, y + r+10, fill="red", outline="")

    def create_wall(self, x, y):
        r = 50
        x = self.zoom * x
        y = self.zoom * y
        return self.canvas.create_rectangle(x, y, x + r, y + r, fill="black", outline="#d3d3d3")

    def create_box(self, x, y):
        r = 50
        x = self.zoom * x
        y = self.zoom * y
        return self.canvas.create_rectangle(x, y, x + r, y + r, fill="#a52b2a", outline="#d3d3d3", width=3)

    def create_goal(self, x, y):
        r = 50
        x = self.zoom * x
        y = self.zoom * y
        return self.canvas.create_rectangle(x, y, x + r, y + r, fill="#fea500", outline="#d3d3d3")

    def left(self, event):
        # isvalidMove?
        self.canvas.move(self.player, -self.zoom, 0)
        cord = self.canvas.coords(self.player)
        x = int(cord[0] / self.zoom)
        y = int(cord[1] / self.zoom)
        print((x, y))

    def right(self, event):
        self.canvas.move(self.player, self.zoom, 0)
        cord = self.canvas.coords(self.player)
        x = int(cord[0] / self.zoom)
        y = int(cord[1] / self.zoom)
        print((x, y))

    def up(self, event):
        self.canvas.move(self.player, 0, -self.zoom)
        cord = self.canvas.coords(self.player)
        x = int(cord[0] / self.zoom)
        y = int(cord[1] / self.zoom)
        print((x, y))

    def down(self, event):
        self.canvas.move(self.player, 0, self.zoom)
        cord = self.canvas.coords(self.player)
        x = int(cord[0] / self.zoom)
        y = int(cord[1] / self.zoom)
        print((x, y))


g = graph()
mainloop()
