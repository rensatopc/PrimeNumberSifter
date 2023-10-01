import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import simpledialog
import math
import ctypes
from lang import Lang
import json
import sys
import os

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

if not(os.path.isfile("settings.json")):
    settings = {"lang": "en"}
    with open("settings.json", "w") as f:
        json.dump(settings, f, ensure_ascii=False, indent=4)

settings = None
with open("settings.json", "r") as f:
    settings = json.load(f)

if "lang" in settings:
    if settings["lang"] == "ja":
        translateList = Lang().ja()
    elif settings["lang"] == "en":
        translateList = Lang().en()
else:
    msgbox.showerror("Error! (Error Code 1)", "not writed \"lang\" key in settings.json!")
    sys.exit(1)

class Sifter:
    def __init__(self):
        pass

    def createSifter(self, siftlen):
        self.sifterPanel = tk.Frame(self.root)
        self.sifterPanel.pack(expand=True)

        self.sifter = [True] * (siftlen + 1)
        self.sifter[0], self.sifter[1] = False, False

        sifterdivide = math.sqrt(len(self.sifter))

        self.sifterUI = []

        sifternum = [i for i in range(siftlen + 1)]
        i = 0
        for r in range(math.ceil(sifterdivide)):
            for c in range(math.floor(sifterdivide)):
                itemlist = [None] * 2
                item = tk.Label(self.sifterPanel, text=i, width=5, height=2, borderwidth=1, relief=tk.SOLID)
                item.grid(column=c, row=r)
                if i not in sifternum or i <= 1:
                    item.configure(text="")
                    itemlist[1] = False
                else:
                    itemlist[1] = True
                i += 1
                itemlist[0] = item
                self.sifterUI.append(itemlist)
    
    def createTkinter(self):
        self.root = tk.Tk()
        self.root.title(translateList["root_title"])

        menuBar = tk.Menu(self.root)

        menuFile = tk.Menu(menuBar, tearoff=False)
        menuBar.add_cascade(label=translateList["menubar_file"], menu=menuFile)

        menuFile.add_command(label=translateList["menubar_file_newsifter"], command=lambda: self.newSifter())

        menuFile.add_command(label=translateList["menubar_file_quit"], command=lambda: sys.exit(0))

        self.root.configure(menu=menuBar)
    
    def newSifter(self):
        self.siftlen = simpledialog.askinteger("", translateList["ask_sifterlength"], minvalue=3)

        if self.siftlen != None:
            self.sifterPanel.destroy()

            self.createSifter(self.siftlen)

    def init(self):
        self.createTkinter()

        self.NothingLabel = tk.Label(self.root, text=translateList["nothinglabel"])
        self.NothingLabel.pack(expand=True)

        self.siftlen = simpledialog.askinteger("", translateList["ask_sifterlength"], minvalue=3)

        if self.siftlen != None:
            self.NothingLabel.pack_forget()
            self.root.focus_force()

            self.createSifter(self.siftlen)

            self.root.mainloop()

if __name__ == "__main__":
    Sifter().init()