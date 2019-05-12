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


def validate_data(x_vals, y_vals):
    """ Validate entered data """
    pass


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

    run_btn = ttk.Button(main_frame, text='RUN!',
                         command=lambda: process(validate_data(x_vals, y_vals))).grid(column=7, row=0, rowspan=2)

    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    x_entry.focus()

    logging.info('GUI init finished')
    root.mainloop()
    logging.info('Finished running')
