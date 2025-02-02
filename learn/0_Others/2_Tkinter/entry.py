#==========================================================================================================================================================
# Contoh 1

# Import
from tkinter import *

root = Tk()

# Label
L1 = Label(root, text="User Name")
L1.pack( side = LEFT)

# Entry
E1 = Entry(root, bd =5)
E1.pack(side = RIGHT)

# End...
root.mainloop()

#==========================================================================================================================================================
"""
// Syntax //
// Here is the simple syntax to create this widget −

    w = Entry( master, option, ... )

// Parameters //
// master − This represents the parent window.
// options − Here is the list of most commonly used options for this widget. These options can be used as key-value pairs separated by commas.

// Option & Description //
1) bg
   The normal background color displayed behind the label and indicator.

2) bd
   The size of the border around the indicator. Default is 2 pixels.

3) command
   A procedure to be called every time the user changes the state of this checkbutton.

4) cursor
   If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the checkbutton.

5) font
   The font used for the text.

6) exportselection
   By default, if you select text within an Entry widget, it is automatically exported to the clipboard. To avoid this exportation, use exportselection=0.

7) fg
   The color used to render the text.

8) highlightcolor
   The color of the focus highlight when the checkbutton has the focus.

9) justify
   If the text contains multiple lines, this option controls how the text is justified: CENTER, LEFT, or RIGHT.

10) relief
    With the default value, relief=FLAT, the checkbutton does not stand out from its background. You may set this option to any of the other styles

11) selectbackground
    The background color to use displaying selected text.

12) selectborderwidth
    The width of the border to use around selected text. The default is one pixel.

13) selectforeground
    The foreground (text) color of selected text.

14) show
    Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show="*".

15) state
    The default is state=NORMAL, but you can use state=DISABLED to gray out the control and make it unresponsive. If the cursor is currently over the checkbutton, the state is ACTIVE.

16) textvariable
    In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.

17) width
    The default width of a checkbutton is determined by the size of the displayed image or text. You can set this option to a number of characters and the checkbutton will always have room for that many characters.

18) xscrollcommand
    If you expect that users will often enter more text than the onscreen size of the widget, you can link your entry widget to a scrollbar.


// Methods //
// Following are commonly used methods for this widget −

// Method & Description //
1) delete ( first, last=None )
   Deletes characters from the widget, starting with the one at index first, up to but not including the character at position last. If the second argument is omitted, only the single character at position first is deleted.

2) get()
   Returns the entry's current text as a string.

3) icursor ( index )
   Set the insertion cursor just before the character at the given index.

4) index ( index )
   Shift the contents of the entry so that the character at the given index is the leftmost visible character. Has no effect if the text fits entirely within the entry.

5) insert ( index, s )
   Inserts string s before the character at the given index.

6) select_adjust ( index )
   This method is used to make sure that the selection includes the character at the specified index.

7) select_clear()
   Clears the selection. If there isn't currently a selection, has no effect.

8) select_from ( index 
   Sets the ANCHOR index position to the character selected by index, and selects that character.

9) select_present()
   If there is a selection, returns true, else returns false.

10) select_range ( start, end )
    Sets the selection under program control. Selects the text starting at the start index, up to but not including the character at the end index. The start position must be before the end position.

11) select_to ( index )
    Selects all the text from the ANCHOR position up to but not including the character at the given index.

12) xview ( index )
    This method is useful in linking the Entry widget to a horizontal scrollbar.

13) vxview_scroll ( number, what )
    Used to scroll the entry horizontally. The what argument must be either UNITS, to scroll by character widths, or PAGES, to scroll by chunks the size of the entry widget. The number is positive to scroll left to right, negative to scroll right to left.
"""