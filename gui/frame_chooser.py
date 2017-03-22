import Tkinter
import os

import config as config
import gui.frame_compare as frame_compare
import gui.plot_row as plot
import util.mathematics.colours as colours
import util.video.keyframes as keyframes
from definitions import ROOT_DIR

font = ("Arial", config.fontSize, "bold")

"""
|-------------------------------------------------------------------------------
| Frame Chooser GUI Component
|-------------------------------------------------------------------------------
|
| This is the Matrix Visualiser. This generates a grid representing each of the
| possible frame transitions. Each of the grid cells is coloured based on the
| given metric, and clicking on one of these cells will show the two frames
| being compared. There are different colouring schemes, which can be found
| in util.mathematics.colour.
|
"""

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
                    width=config.cellWidth + 2,
                    textvariable=self.text,
                    state="readonly")
        self.grid(column=y, row=x)

class ButtonWidget(Tkinter.Button):

    def __init__(self, master, x, y, value, matrix):
        Tkinter.Button.__init__(self, master=master)
        self.value = Tkinter.StringVar()

        if config.colouringType == "Island":
            r, g, b = colours.island_rgb(0, 255, value)
        elif config.colouringType == "Rainbow":
            r, g, b = colours.rgb(0, 255, value)
        else:
            r, g, b = colours.grayscale_rgb(0, 255, value)

        self.color = colours.rgb_to_hex(r, g, b)
        self.config(textvariable=self.value,
                    width=config.cellWidth,
                    relief="flat",
                    font=font,
                    bg=self.color,
                    fg="#000000000",
                    justify='center')
        self.grid(column=y,
                  row=x)
        self.value.set("{0:.2f}".format(value / 255.0))

class ButtonGrid(Tkinter.Tk):

    """ Dialog box with Entry widgets arranged in columns and rows."""
    def __init__(self, data_matrix, title):

        # Set some data points
        self.matrix = data_matrix
        (self.no_rows, self.no_cols) = data_matrix.shape

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
                    return self.grid_button_handler(col, row)

                w.bind(sequence="<Button>", func=handler)
        self.mainloop()

    """
    | Shows the frame comparison GUI when a cell is clicked
    """
    def grid_button_handler(self, col, row):
        print "Clicked X: ", col, "Y: ", row

        inputFile = os.path.join(ROOT_DIR, config.inputPath)

        frame_1 = keyframes.get_frame(inputFile, col)
        frame_2 = keyframes.get_frame(inputFile, row)
        frame_compare.compare_frames(frame_1, frame_2)

    """
    | Shows the local maxima and magnitude plots when the labels are clicked
    """
    def label_handler(self, row):
        print "Clicked Row: " + str(row)
        matrix = self.matrix
        plot.plot_matrix_row(matrix, row)

    """
    | Generates the matrix row and column labels when initialising
    """
    def make_header(self):

        self.hdrDict = {}

        for i in range(0, self.no_cols + 1):
            w = Tkinter.Button(self.mainFrame,
                               text=i,
                               width=config.cellWidth,
                               relief="flat",
                               font=font,
                               bg="#000000",
                               fg="#ffffff",
                               justify='center')
            w.grid(row=0, column=i, sticky="W")
            self.hdrDict[(i, 0)] = w

        for i in range(1, self.no_cols + 1):
            w = Tkinter.Button(self.mainFrame,
                               text=i,
                               width=config.cellWidth,
                               relief="flat",
                               font=font,
                               bg="#000000",
                               fg="#ffffff",
                               justify='center')
            w.grid(row=i, column=0, sticky="W")
            self.hdrDict[(0, i + 1)] = w

            def handler(event, row=i):
                return self.label_handler(row)

            w.bind(sequence="<Button>", func=handler)

"""
| External callable function to generate the grid for the given matrix
"""
def create_matrix_visualization(matrix, title):
    demo_matrix = matrix
    app = ButtonGrid(demo_matrix, title)

