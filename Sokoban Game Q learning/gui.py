from tkinter import *
import threading
from time import sleep
from base_implementation import *


class Graph(threading.Thread):
    def __init__(self, board):
        threading.Thread.__init__(self)
        self.boxes = []
        self.blues = []
        self.zoom = 50
        self.playersize = 30
        self.boxsize = 50
        self.width = 10 * self.zoom
        self.height = 10 * self.zoom
        self.board = board
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = Tk()
        self.root.title("271 final")
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        l = Label(self.root, text="    1   2   3   4   5   6   7   8   9", font=("Courier", 16, "bold"))
        l.pack()
        self.create_bad()

        for box in self.board.boxes:
            self.boxes.append(self.create_box(box))

        for wall in self.board.walls:
            self.create_wall(wall)

        for storage in self.board.storages:
            self.create_goal(storage)

        self.player = self.create_player(self.board.get_player())

        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.mainloop()

    def create_bad(self):
        for cood in self.board.state_value_table:
            x = self.zoom * cood[1]
            y = self.zoom * cood[0]
            self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="green", outline="#d3d3d3")

    def create_player(self, player):
        x = self.zoom * player[1]
        y = self.zoom * player[0]
        return self.canvas.create_oval(x + 10, y + 10, x + self.playersize + 10, y + self.playersize + 10, fill="red",
                                       outline="")

    def create_wall(self, wall):
        x = self.zoom * wall[1]
        y = self.zoom * wall[0]
        return self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="black", outline="#d3d3d3")

    def create_box(self, box):
        x = self.zoom * box[1]
        y = self.zoom * box[0]
        return self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="#a52b2a", outline="#d3d3d3",
                                            width=3)

    def create_goal(self, storage):
        x = self.zoom * storage[1]
        y = self.zoom * storage[0]
        return self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="#fea500", outline="#d3d3d3")

    def update(self):
        sleep(1)
        x = self.zoom * self.board.player_col
        y = self.zoom * self.board.player_row

        self.canvas.coords(self.player, x + 10, y + 10, x + self.playersize + 10, y + self.playersize + 10)

        for i in range(len(self.board.boxes)):
            x = self.zoom * self.board.boxes[i][1]
            y = self.zoom * self.board.boxes[i][0]
            self.canvas.coords(self.boxes[i], x, y, x + self.boxsize, y + self.boxsize)