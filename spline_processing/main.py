import logging
import os
import tkinter as tk
from pathlib import PureWindowsPath
from tkinter import *
from tkinter import messagebox, ttk

import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as intp


def process(x_arr, y_arr):
    """ Process the interpolation """
    pass


def validate_data(x_var, y_var):
    """ Validate entered data """
    x_raw_data = x_var.get().replace(',', ' ').replace('\t', ' ')
    y_raw_data = y_var.get().replace(',', ' ').replace('\t', ' ')

    x_vals = [x for x in x_raw_data.split(' ') if x != ' ']
    y_vals = [y for y in y_raw_data.split(' ') if y != ' ']

    if len(x_vals) != len(y_vals):
        logging.error('Different data arrays length')
        messagebox.showerror('Different data arrays length',
                             'x len: {}\ny len: {}'.format(len(x_vals), len(y_vals)))


def show_help():
    """ Show help about data entering """
    messagebox.showinfo('Data entering', """
    Enter equal arrays of x and y values
    Separate values with space < >, tab <   > or coma <,>
    Separate fraction using dot <.>
    """)


if __name__ == "__main__":
    logging.basicConfig(filename=PureWindowsPath(os.path.realpath(__file__)).parent / 'spline_last_run.log',
                        filemode='w', level=logging.INFO)

    root = Tk()
    root.title('Hermite-spline interpolating')
    main_frame = ttk.Frame(root, padding='3 3 12 12')
    main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # init vars
    x_vals = StringVar()
    y_vals = StringVar()

    ttk.Label(main_frame, text='Enter values on x axis:').grid(
        column=0, row=0, sticky=tk.W)

    ttk.Label(main_frame, text='Enter values on y axis:').grid(
        column=0, row=1, sticky=tk.W)

    x_entry = ttk.Entry(main_frame, width=40, textvariable=x_vals)
    x_entry.grid(column=1, row=0, sticky=tk.E)

    y_entry = ttk.Entry(main_frame, width=40, textvariable=y_vals)
    y_entry.grid(column=1, row=1, sticky=tk.E)

    help_btn = ttk.Button(main_frame, text='HELP',
                          command=lambda: show_help()).grid(column=7, row=0)

    run_btn = ttk.Button(main_frame, text='RUN!',
                         command=lambda: process(validate_data(x_vals, y_vals))).grid(column=7, row=1)

    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    x_entry.focus()

    logging.info('GUI init finished')
    root.mainloop()
    logging.info('Finished running')
