from Tkinter import *
import Tkinter as tk
import subprocess as sub
import definitions as d

"""
|-------------------------------------------------------------------------------
| Start Dialog GUI Component
|-------------------------------------------------------------------------------
|
| The start component is the GUI which appears when the application is launched.
| For ease of use, it is best to launch using the start dialog, but each of
| the scripts have been designed to work independently.
|
"""

"""
| Gives a colour based on whether a button can be clicked or not
"""
def getColour(boolType):
    if boolType:
        return "#248f24"
    else:
        return "#800000"

"""
| Checks to see if the button can be interacted or not
"""
def getEnabled(boolType):
    if boolType:
        return NORMAL
    else:
        return DISABLED


class MainApplication(tk.Frame):

    def createWidgets(self):

        self.displayedTitle = Label(self,
            font="OpenSans 20",
            justify=LEFT,
            padx=10,
            text="Video Textures")

        self.createProcessSection()
        self.createGenerationSection()

        self.simButtons.pack(side=LEFT)
        self.dynButtons.pack(side=LEFT)
        self.futButtons.pack(side=LEFT)
        self.probButtons.pack(side=LEFT)
        self.pruneButtons.pack(side=LEFT)

        self.basicRandomButton.pack(side=LEFT)
        self.basicLoopButton.pack(side=LEFT)
        self.randomButton.pack(side=LEFT)
        self.videoLoopsButton.pack(side=LEFT)

    """
    | The buttons for the analysis stage
    """
    def createProcessSection(self):
        self.processTitle = LabelFrame(self,
            font="OpenSans 10",
            padx=10,
            text="Analysis and Synthesis")
        self.processTitle.grid(row=1, columnspan=7, sticky='WE',
                 padx=5, pady=5, ipadx=5, ipady=5)

        self.simButtons = Button(self.processTitle,
                                 text="Similarities",
                                 bg=getColour(self.similaritiesEnabled),
                                 font="OpenSans",
                                 fg="White",
                                 relief=FLAT,
                                 command=self.similaritiesClicked,
                                 state=getEnabled(self.similaritiesEnabled))

        self.dynButtons = Button(self.processTitle,
                                 text="Dynamics",
                                 bg=getColour(self.dynamicsEnabled),
                                 font="OpenSans",
                                 fg="White",
                                 relief=FLAT,
                                 command=self.dynamicsClicked,
                                 state=getEnabled(self.dynamicsEnabled))

        self.futButtons = Button(self.processTitle,
                                 text="Future Costs",
                                 bg=getColour(self.futureCostsEnabled),
                                 font="OpenSans",
                                 fg="White",
                                 relief=FLAT,
                                 command=self.futureClicked,
                                 state=getEnabled(self.futureCostsEnabled))

        self.probButtons = Button(self.processTitle,
                                  text="Probabilities",
                                  bg=getColour(self.probabilitiesEnabled),
                                  font="OpenSans",
                                  fg="White",
                                  relief=FLAT,
                                  command=self.probabilitiesClicked,
                                  state=getEnabled(self.probabilitiesEnabled))

        self.pruneButtons = Button(self.processTitle,
                                   text="Prune",
                                   bg=getColour(self.pruneEnabled),
                                   font="OpenSans",
                                   fg="White",
                                   relief=FLAT,
                                   command=self.pruneClicked,
                                   state=getEnabled(self.pruneEnabled))

    """
    | The buttons for the synthesis stage
    """
    def createGenerationSection(self):
        self.generateTitle = LabelFrame(self,
            font="OpenSans 10",
            padx=10,
            text="Video Generation")
        self.generateTitle.grid(row=2, columnspan=7, sticky='WE',
                 padx=5, pady=5, ipadx=5, ipady=5)

        self.basicLoopButton = Button(self.generateTitle,
                                      text="Basic Loop",
                                      bg=getColour(self.basicLoopEnabled),
                                      font="OpenSans",
                                      fg="White",
                                      relief=FLAT,
                                      command=self.basicLoopClicked,
                                      state=getEnabled(self.basicLoopEnabled))

        self.basicRandomButton = Button(self.generateTitle,
                                        text="Basic Random",
                                        bg=getColour(self.basicRandomEnabled),
                                        font="OpenSans",
                                        fg="White",
                                        relief=FLAT,
                                        command=self.basicRandomClicked,
                                        state=getEnabled(self.basicRandomEnabled))

        self.randomButton = Button(self.generateTitle,
                                   text="Informed Random",
                                   bg=getColour(self.informedRandomEnabled),
                                   font="OpenSans",
                                   fg="White",
                                   relief=FLAT,
                                   command=self.informedRandomClicked,
                                   state=getEnabled(self.informedRandomEnabled))

        self.videoLoopsButton = Button(self.generateTitle,
                                       text="Video Loops",
                                       bg=getColour(self.videoLoopsEnabled),
                                       font="OpenSans",
                                       fg="White",
                                       relief=FLAT,
                                       command=self.videoLoopsClicked,
                                       state=getEnabled(self.videoLoopsEnabled))

    """
    | All of the following are launchers for the various scripts
    """
    def similaritiesClicked(self):
        print d.similarities_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/analysis/a_determine_similarities.py', shell=True)
        self.process.wait()

        self.dynamicsEnabled = True
        self.dynButtons.config(bg=getColour(self.dynamicsEnabled), state=getEnabled(self.dynamicsEnabled))

    def dynamicsClicked(self):
        print d.dynamics_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/analysis/b_preserve_dynamics.py', shell=True)
        self.process.wait()

        self.futureCostsEnabled = True
        self.futButtons.config(bg=getColour(self.futureCostsEnabled), state=getEnabled(self.futureCostsEnabled))

    def futureClicked(self):
        print d.future_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/analysis/c_determine_future_costs.py', shell=True)
        self.process.wait()

        self.probabilitiesEnabled = True
        self.probButtons.config(bg=getColour(self.probabilitiesEnabled), state=getEnabled(self.probabilitiesEnabled))

    def probabilitiesClicked(self):
        print d.probabilities_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/analysis/d_determine_probabilities.py', shell=True)
        self.process.wait()

        self.pruneEnabled = True
        self.pruneButtons.config(bg=getColour(self.pruneEnabled), state=getEnabled(self.pruneEnabled))

    def pruneClicked(self):
        print d.prune_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/analysis/e_prune_transitions.py', shell=True)
        self.process.wait()

        self.informedRandomEnabled = True
        self.videoLoopsEnabled = True
        self.randomButton.config(bg=getColour(self.informedRandomEnabled), state=getEnabled(self.informedRandomEnabled))
        self.videoLoopsButton.config(bg=getColour(self.videoLoopsEnabled), state=getEnabled(self.videoLoopsEnabled))

    def basicRandomClicked(self):
        print d.basic_random_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/synthesis/basic_random_play.py', shell=True)
        self.process.wait()

    def basicLoopClicked(self):
        print d.basic_loop_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/synthesis/basic_loop.py', shell=True)
        self.process.wait()

    def informedRandomClicked(self):
        print d.informed_random_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/synthesis/random_play.py', shell=True)
        self.process.wait()

    def videoLoopsClicked(self):
        print d.video_loops_clicked

        self.process = sub.Popen('C:/Users/Struan/PycharmProjects/TestProject/synthesis/video_loops.py', shell=True)
        self.process.wait()

    """
    | Initialise the GUI
    """
    def __init__(self, master=None):
        self.master = master
        self.process = ""
        self.output = ""

        # Used for lighting up buttons
        self.similaritiesEnabled = True
        self.dynamicsEnabled = True
        self.futureCostsEnabled = True
        self.probabilitiesEnabled = True
        self.pruneEnabled = True

        self.basicRandomEnabled = True
        self.basicLoopEnabled = True
        self.informedRandomEnabled = True
        self.videoLoopsEnabled = True

        tk.Frame.__init__(self, master)

        master.title("Video Textures")

        self.pack()
        self.createWidgets()

"""
| Prints a message into the console when the application is loaded
"""
def display_welcome_message():
    print d.SPACER + " __     ___     _              _____         _                       "
    print d.SPACER + " \ \   / (_) __| | ___  ___   |_   _|____  _| |_ _   _ _ __ ___  ___ "
    print d.SPACER + "  \ \ / /| |/ _` |/ _ \/ _ \    | |/ _ \ \/ / __| | | | '__/ _ \/ __|"
    print d.SPACER + "   \ V / | | (_| |  __/ (_) |   | |  __/>  <| |_| |_| | | |  __/\__ \\"
    print d.SPACER + "    \_/  |_|\__,_|\___|\___/    |_|\___/_/\_\\\\__|\__,_|_|  \___||___/"
    print d.SPACER + "                                                                     "
    print d.SPACER + "                     --  STRUAN MCDONOUGH 2017  --                   "
    print d.SPACER + "http://cpl.cc.gatech.edu/projects/videotexture/SIGGRAPH2000/index.htm"
    print d.SPACER + "                                 -- --                               "
    print ""

"""
| Entry point for the program
"""
if __name__ == "__main__":
    display_welcome_message()
    sub.Popen("C:/Program Files (x86)/Notepad++/notepad++.exe")
    root = Tk()
    app = MainApplication(root)
    app.mainloop()

