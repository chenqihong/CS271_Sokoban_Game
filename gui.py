from tkinter import *
import threading

class graph(threading.Thread):
    def __init__(self, board):
        threading.Thread.__init__(self)
        self.boxes = []
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
        self.root.bind("<KeyPress-Left>", self.left)
        self.root.bind("<KeyPress-Right>", self.right)
        self.root.bind("<KeyPress-Up>", self.up)
        self.root.bind("<KeyPress-Down>", self.down)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        l = Label(self.root, text="    1   2   3   4   5   6   7   8   9", font=("Courier", 16, "bold"))
        l.pack()

        for box in self.board.box_coordinate_list:
            self.boxes.append(self.create_box(box))

        for wall in self.board.wall_coordinate_list:
            self.create_wall(wall)

        for storage in self.board.storage_coordinate_list:
            self.create_goal(storage)

        self.create_bad(update_corner_state_value_table(self.board))

        self.player = self.create_player(self.board.get_current_player_coordinate())

        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.mainloop()

    def create_bad(self, bad):
        for cood in bad:
            x = self.zoom * cood[1]
            y = self.zoom * cood[0]
            self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="green", outline="#d3d3d3")

    def create_player(self, player):
        x = self.zoom * player[1]
        y = self.zoom * player[0]
        return self.canvas.create_oval(x + 10, y + 10, x + self.playersize + 10, y + self.playersize + 10, fill="red", outline="")

    def create_wall(self, wall):
        x = self.zoom * wall[1]
        y = self.zoom * wall[0]
        return self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="black", outline="#d3d3d3")

    def create_box(self, box):
        x = self.zoom * box[1]
        y = self.zoom * box[0]
        return self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="#a52b2a", outline="#d3d3d3", width=3)

    def create_goal(self, storage):
        x = self.zoom * storage[1]
        y = self.zoom * storage[0]
        return self.canvas.create_rectangle(x, y, x + self.boxsize, y + self.boxsize, fill="#fea500", outline="#d3d3d3")

    def move_player(self, coordinate):
        x = self.zoom * coordinate[1]
        y = self.zoom * coordinate[0]
        self.canvas.coords(self.player, x + 10, y + 10, x + self.playersize + 10, y + self.playersize + 10)

    def move_box(self, all_boxes_position):
        for i in range(len(all_boxes_position)):
            x = self.zoom * all_boxes_position[i][1]
            y = self.zoom * all_boxes_position[i][0]

            self.canvas.coords(self.boxes[i], x, y, x + self.boxsize, y + self.boxsize)

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
