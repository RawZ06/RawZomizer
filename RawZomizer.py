from tkinter import *
import random
import os
from v_30 import v_30
from v_31 import v_31

def execute():
    ver = version.get()
    main.destroy()
    if ver == "Version 2.23.x - 3.x":
        v_30()
    else:
        v_31()

main=Tk()

main.geometry("450x100+500+300")

main.title("RawZomizer V3.6 : Setting String Randomizer for OoTR")

version = StringVar(main)
version.set("Version 2.23.x - 3.x")

Label(main, text="Choice your version of OoTR").grid(row=1, column=1)
w1 = OptionMenu(main, version, "Version 2.23.x - 3.x", "Version 3.1.x")
w1.grid(row=1, column=2)

Button(main, text="Execute", command=execute).grid(row=2, column=1)

main.mainloop()
