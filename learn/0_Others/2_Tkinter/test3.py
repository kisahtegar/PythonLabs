# Multi-frame tkinter application v2.3
import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        #self.master = master
        self.master.resizable(width="False", height="False")
        self.master.geometry("500x200")
        labels = self.labels()
        labels


    def labels(self):
        label1 = tk.Label(self.master, text="This is the start page")
        #label1.pack()
        label1.place(x=10, y=10)

        label2 = tk.Button(self.master, text="Open page one", command=lambda: self.master.switch_frame(PageOne))
        #label2.pack()
        label2.place(x=10, y= 30)

        label3 = tk.Button(self.master, text="Open page two", command=lambda: self.master.switch_frame(PageTwo))
        #label3.pack()
        label3.place(x=10, y= 60)

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master = master
        self.master.resizable(width="True", height="True")
        self.master.geometry("200x100")
        self.one()

    def one(self):
        label1 = tk.Label(self.master, text="This is page one").pack(side="top", fill="x", pady=10)
        label1.place(x=20,y=30)
        
        label2 = tk.Button(self.master, text="Return to start page", command=lambda: self.master.switch_frame(StartPage))
        label2.place(x=20,y=30)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self)
        self.master.resizable(width="True", height="True")
        self.master.geometry("200x100")
        self.two()

    def two(self):
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", command=lambda: self.master.switch_frame(StartPage)).pack()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.master = master
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()