import tkinter as tk

from .breakdown_root import BdRoot

root = BdRoot()

main_frame = tk.Frame(root)
main_frame.configure(bg="#292929")
main_frame.pack(expand=True, fill="both")