from tkinter import *
import random
import os
from v_30 import v_30
from v_31 import v_31
import version

WARNING = "Warning ! The OoTR " + version.DEV + " is developing ! May be incompatible"

label = None

def execute():
    ver = version.get()
    main.destroy()
    if ver == "Release":
        v_30()
    else:
        v_31()

def warning(element):
    global label
    if element != "Release":
        if label == None:
            label = Label(main, text=WARNING)
            label.pack(side=TOP)
    else:
        if label != None:
            label.destroy()
            label = None

main=Tk()

main.geometry("450x150+500+300")

main.title("RawZomizer "+ str(version.VERSION) +" : Settings String Randomizer for OoTR")

l = LabelFrame(main, text="Choose version", padx=20, pady=20)
l.pack(fill="both", expand="yes", side=BOTTOM)

Label(l, text="Last release supported : " + version.RELEASE).grid(row=0, column=1)
Label(l, text="Last dev supported: " + version.DEV).grid(row=0, column=2)

version = StringVar(main)
version.set("Release")

Label(l, text="Choose your version of OoTR").grid(row=1, column=1)
w1 = OptionMenu(l, version, "Release", "Dev", command=warning)
w1.grid(row=1, column=2)

Button(l, text="Execute", command=execute).grid(row=2, column=1)

main.mainloop()
