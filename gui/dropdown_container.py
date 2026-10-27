import tkinter as tk

import constants
import settings

user_settings = settings.Settings()

class DropdownContainer(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.column_count = 0
        self.row_count = 0
        self.configure(bg=getattr(user_settings, constants.BACKGROUND_COLOR))

    def add_column_item(self, widget):
        widget.grid(column=self.column_count, row=self.row_count)
        self.column_count += 1

    def add_row_item(self, widget):
        self.column_count = 0
        self.row_count += 1
        widget.grid(column=self.column_count, row=self.row_count)
