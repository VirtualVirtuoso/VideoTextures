import Tkinter

import util.mathematics.colours as colours
import util.video.keyframes as keyframes
import gui.frame_compare as frame_compare
import config as config
import os

from definitions import ROOT_DIR

font = ("Arial", config.fontSize, "bold italic")

class LabelWidget(Tkinter.Entry):

    def __init__(self, master, x, y, text):
        self.text = Tkinter.StringVar()

        if text == 0:
            self.text.set("F#")
        else:
            self.text.set(text)

        Tkinter.Entry.__init__(self, master=master)

        self.config(relief="ridge",
                    font=font,
                    bg="#000000",
                    fg="#ffffff",
                    readonlybackground="#000000",
                    justify='center',
                    width=config.cellWidth,
                    textvariable=self.text,
                    state="readonly")
        self.grid(column=y, row=x)

class ButtonWidget(Tkinter.Button):

    def __init__(self, master, x, y, value, matrix):
        Tkinter.Button.__init__(self, master=master)
        self.value = Tkinter.StringVar()

        r, g, b = colours.rgb(0, 255, value)
        self.color = colours.rgb_to_hex(r, g, b)
        self.config(textvariable=self.value,
                    width=config.cellWidth,
                    relief="ridge",
                    font=font,
                    bg=self.color,
                    fg="#000000000",
                    justify='center')
        self.grid(column=y,
                  row=x)
        self.value.set("{0:.1f}".format(value))

class ButtonGrid(Tkinter.Tk):

    """ Dialog box with Entry widgets arranged in columns and rows."""
    def __init__(self, data_matrix, title):

        # Set some data points
        self.matrix = data_matrix
        (self.no_rows, self.no_cols) = data_matrix.shape
        self.no_cols -= 1

        Tkinter.Tk.__init__(self)
        self.title(title)

        self.mainFrame = Tkinter.Frame(self)
        self.mainFrame.config(padx='3.0m', pady='3.0m')
        self.mainFrame.grid()

        # Create the wrapping header
        self.make_header()

        self.gridDict = {}

        # Create the grid
        for i in range(1, self.no_cols + 1):
            for j in range(1, self.no_rows + 1):
                w = ButtonWidget(self.mainFrame, i, j, self.matrix.item((i - 1, j - 1)), self.matrix)
                self.gridDict[(i - 1, j)] = w.value

                def handler(event, col=i, row=j):
                    return self.__entryhandler(col, row)

                w.bind(sequence="<Button>", func=handler)
        self.mainloop()

    def __entryhandler(self, col, row):
        print "Clicked X: ", col, "Y: ", row

        inputFile = os.path.join(ROOT_DIR, config.inputPath)

        frame_1 = keyframes.get_frame(inputFile, col)
        frame_2 = keyframes.get_frame(inputFile, row)
        frame_compare.compare_frames(frame_1, frame_2)

    def make_header(self):

        self.hdrDict = {}

        for i in range(0, self.no_cols + 1):
            w = LabelWidget(self.mainFrame, i, 0, i)
            self.hdrDict[(i, 0)] = w

        for i in range(1, self.no_cols + 2):
            w = LabelWidget(self.mainFrame, 0, i, i)
            self.hdrDict[(0, i + 1)] = w

def create_matrix_visualization(matrix, title):
    demo_matrix = matrix
    app = ButtonGrid(demo_matrix, title)
