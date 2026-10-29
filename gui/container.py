import tkinter as tk

import constants
import settings

user_settings = settings.Settings()

class Container(tk.Frame):

    def __init__(self, master, bg=getattr(user_settings, constants.BACKGROUND_COLOR), *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.column_count = 0
        self.row_count = 0
        self.configure(bg=bg, *args, **kwargs)

    def add_column_item(self, widget, padx=(10,10), pady=(5,5), *args, **kwargs):
        widget.grid(column=self.column_count, row=self.row_count, padx=padx, pady=pady, *args, **kwargs)
        self.column_count += 1

    def add_row_item(self, widget, padx=(10,10), pady=(5,5), *args, **kwargs):
        self.column_count = 0
        self.row_count += 1
        widget.grid(column=self.column_count, row=self.row_count, padx=padx, pady=pady, *args, **kwargs)
