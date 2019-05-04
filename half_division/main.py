from tkinter import *
from tkinter import ttk
import logging
import pandas
import matplotlib
import sympy

""" Main script for half-division method implementation
Gonna store data in pandas DataFrame
Process the function calculation using sympy
"""


def process():
    """ Process the method """
    pass


if __name__ == "__main__":
    root = Tk()
    root.title('Half-division method')
    main_frame = ttk.Frame(root, padding='3 3 12 12')
    main_frame.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # init vars
    expr = StringVar()  # 'E'xpression to evaluate
    a_edge = StringVar()
    b_edge = StringVar()

    ttk.Label(main_frame, text='Enter expression:').grid(
        column=1, row=1, sticky='W', columnspan=2)

    ttk.Label(main_frame, text='Enter edges:').grid(
        column=3, row=1, sticky='W', columnspan=2)

    ttk.Label(main_frame, text='f(x) =').grid(
        column=1, row=2, sticky='W')

    ttk.Label(main_frame, text='Left:').grid(
        column=3, row=2, sticky='W')

    ttk.Label(main_frame, text='Right:').grid(
        column=5, row=2, sticky='W')

    a_edge_entry = ttk.Entry(main_frame, width=4, textvariable=a_edge)
    a_edge_entry.grid(column=4, row=2, sticky='E')

    b_edge_entry = ttk.Entry(main_frame, width=4, textvariable=b_edge)
    b_edge_entry.grid(column=6, row=2, sticky='E')

    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    expr_entry = ttk.Entry(main_frame, width=18, textvariable=expr)
    expr_entry.grid(column=2, row=2, sticky='E')

    expr_entry.focus()

    root.bind('<Return>', process)
    root.mainloop()
