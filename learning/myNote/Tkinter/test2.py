import tkinter as tk


# Creates the main window
class A(tk.Frame):
    """The class A frame is the main page of the application,
     when running the program, it will be the first thing shown to the user."""
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.bt_identities_a = []  # this list will be used to save the identities of each button created in class A

        # Creates multiple buttons
        for i in range(10):
            self.bt_a = tk.Button(self, text=f"Player  A{i}", command=lambda x=i: self.open_window_of_class_b(x))
            self.bt_a.grid()

            self.bt_identities_a.append(self.bt_a)  # adds the button identity to the list

    def open_window_of_class_b(self, n):
        """This is the method responsible for executing class B
            and for recognizing which button was clicked in class A

           All actions to be performed by the buttons in class B
            from now on must be associated with exactly that one
            button that was clicked in class A.
        """
        # Run class B
        B()

        # get the button id that was clicked
        bt_id = self.bt_identities_a[n]
        ...


# Creates the secondary window
class B(tk.Toplevel):
    """The class B frame is a secondary page that will only be opened if one of the Class A buttons is clicked."""
    def __init__(self):
        tk.Toplevel.__init__(self)

        self.bt_identities_b = []  # this list will be used to save the identities of each button created in class B

        # Creates multiple buttons
        for j in range(10):
            self.bt_b = tk.Button(self, text=f"Character B{j}",
                                  command=lambda x=j: self.changes_the_text_of_a_button_in_class_a(x))
            self.bt_b.grid()

            self.bt_identities_b.append(self.bt_b)  # adds the button identity to the list

    def changes_the_text_of_a_button_in_class_a(self, n):
        """This method should recognize which of the Class B buttons that was clicked,
           take the text from this exact button and pass the text to the Class A button
           that was clicked just before."""

        # get the button id that was clicked
        bt_id = self.bt_identities_b[n]
        ...


root = tk.Tk()
root.geometry("300x300")

app = A(root)
app.pack(fill="both", expand=True)
app.mainloop()