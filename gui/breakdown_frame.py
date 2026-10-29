import tkinter as tk

import constants
import settings

user_settings = settings.Settings()

class BreakdownFrame(tk.Frame):

    def __init__(self, master=None,
                 bg=getattr(user_settings, constants.BACKGROUND_COLOR),
                 *args,
                 **kwargs
             ):
        self.master = master
        super().__init__(master)

        self.configure(bg=bg, *args, **kwargs)


        self.current_frame = None
        self.next_frame = None
        self.previous_frame = None

    def pack(self, padx=(10,10), pady=(10,10), *args, **kwargs):
        super().pack(padx=padx, pady=pady, *args, **kwargs)