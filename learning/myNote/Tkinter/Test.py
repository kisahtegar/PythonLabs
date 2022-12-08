import tkinter as tk

def show_entry_fields():
    print("First Name : {}\nLast Name : {}". format(E1.get(), E2.get()))

root = tk.Tk()
# Label First Name
tk.Label(
    root,
    text = "First Name"
).grid(
    row = 0
)

# Label Last Name
tk.Label(
    root,
    text = "Last Name"
).grid(
    row = 1
)

# Entry
E1 = tk.Entry(root)
E2 = tk.Entry(root)
#Entry Grid
E1.grid(row = 0, column = 1)
E2.grid(row = 1, column = 1)

# Button Quit
tk.Button(
    root,
    text = 'Quit',
    command = root.quit
).grid(
    row = 3,
    column = 0,
    sticky = tk.W,
    pady = 4
)

# Button Show
tk.Button(
    root,
    text = 'Show',
    command = show_entry_fields
).grid(
    row = 3,
    column = 1,
    sticky = tk.W,
    pady = 4
)

tk.mainloop()