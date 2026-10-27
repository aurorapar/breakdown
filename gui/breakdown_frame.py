import tkinter as tk


class BreakdownFrame(tk.Frame):

    def __init__(self, master=None):
        self.master = master
        super().__init__(master)

        self.current_frame = None
        self.next_frame = None
        self.previous_frame = None