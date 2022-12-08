#==========================================================================================================================================================
# Contoh 1

# Import
import tkinter
import tkinter.messagebox as msgboxx

root = tkinter.Tk()

# Code to add widgets will go here...
def messageboxx():
    msgboxx.showerror("Error","hello kisah, this program error")

B = tkinter.Button(font = 10,  text = "Hello", command = messageboxx)

# End...
if __name__ == "__main__":
    B.pack()
    root.mainloop()

#==========================================================================================================================================================
# Contoh 2

# Import
from tkinter import *
import tkinter

root = tkinter.Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()

def checkbutton():

    C1 = Checkbutton(
        root,
        text     = "Music",
        variable = CheckVar1,
        onvalue  = 1,
        offvalue = 0,
        height   = 5,
        width    = 20
    )
    
    C2 = Checkbutton(
        root,
        text     = "Music",
        variable = CheckVar2,
        onvalue  = 1,
        offvalue = 0,
        height   = 5,
        width    = 20
    )
    C1.pack()
    C2.pack()

def button():
    B = tkinter.Button(
        root,
        font = 5,
        text = "Hello",
        command = clear
    )
    B.pack()

def clear():
    CheckVar1.set(0)
    CheckVar2.set(0)

if __name__ == "__main__":
    checkbutton()
    button()
    root.mainloop()

#==========================================================================================================================================================
"""
// Syntax //
// Here is the simple syntax to create this widget −

    w = Button ( master, option=value, ... )

// Parameters //
// master − This represents the parent window.
// options − Here is the list of most commonly used options for this widget. 
             These options can be used as key-value pairs separated by commas.

// Option & Description //
1) activebackground
   Background color when the button is under the cursor.

2) activeforeground
   Foreground color when the button is under the cursor.

3) bd
   Border width in pixels. Default is 2.

4) bg
   Normal background color.

5) command
   Function or method to be called when the button is clicked.

6) fg
   Normal foreground (text) color.

7) font
   Text font to be used for the button's label.

8) height
   Height of the button in text lines (for textual buttons) or pixels (for images).

9) highlightcolor
   The color of the focus highlight when the widget has focus.

10) image
    Image to be displayed on the button (instead of text).

11) justify 
    How to show multiple text lines: LEFT to left-justify each line; CENTER to center them; or RIGHT to right-justify.

12) padx
    Additional padding left and right of the text.

13) pady 
    Additional padding above and below the text.

14) relief
    Relief specifies the type of the border. Some of the values are SUNKEN, RAISED, GROOVE, and RIDGE.

15) state
    Set this option to DISABLED to gray out the button and make it unresponsive. Has the value ACTIVE when the mouse is over it. Default is NORMAL.

16) underline
    Default is -1, meaning that no character of the text on the button will be underlined. If nonnegative, the corresponding text character will be underlined.

17) width
    Width of the button in letters (if displaying text) or pixels (if displaying an image).

18) wraplength
    If this value is set to a positive number, the text lines will be wrapped to fit within this length.
"""