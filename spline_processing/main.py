import logging
import os
import tkinter as tk
from pathlib import PureWindowsPath
from tkinter import *
from tkinter import messagebox, ttk
from collections import namedtuple

import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as intp


Vals = namedtuple('Vals', ['x', 'y'])


def get_interpolator(x: np.array, y: np.array):
    """ Get the interpolator  object """
    return intp.PchipInterpolator(x, y)


def process(vals: Vals):
    """ Process the interpolation """
    process_window = Toplevel()
    process_window.title('Process the interpolation')
    main_frame = ttk.Frame(process_window, padding='10 10 10 10')
    main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    x_arr = np.array(vals.x)
    y_arr = np.array(vals.y)

    try:
        interpolator = get_interpolator(x_arr, y_arr)
    except ValueError as e:
        logging.error('Unable to get interpolator')
        logging.error(e)

    x_range = np.arange(x_arr[0], x_arr[-1], 0.001)
    y_range = interpolator(x_range)

    ttk.Label(main_frame, text='x and y values:').grid(
        column=0, row=0, sticky=tk.W)

    scroll = ttk.Scrollbar(
        main_frame, orient=tk.VERTICAL)
    col = tk.Listbox(main_frame, yscrollcommand=scroll.set)
    col.insert(tk.END, 'X                 Y')
    for x, y in dict(zip(x_range, y_range)).items():
        col.insert(tk.END, '{:.3f}        {:.3f}'.format(
            round(x, 4), round(y, 4)))
    scroll.config(command=col.yview)
    col.grid(column=0, row=1)
    scroll.grid(column=1, row=1, sticky=tk.E+tk.N+tk.S)

    # for child in main_frame.winfo_children():
    #     child.grid_configure(padx=5, pady=5)


def validate_data(x_var, y_var):
    """ Validate entered data """
    x_raw_data = x_var.get().replace(',', ' ').replace('\t', ' ')
    y_raw_data = y_var.get().replace(',', ' ').replace('\t', ' ')

    x_vals = [float(x) for x in x_raw_data.split(' ') if x != ' ']
    y_vals = [float(y) for y in y_raw_data.split(' ') if y != ' ']

    if len(x_vals) != len(y_vals):
        logging.error('Different data arrays length')
        messagebox.showerror('Different data arrays length',
                             'x len: {}\ny len: {}'.format(len(x_vals), len(y_vals)))

    return Vals(x=x_vals, y=y_vals)


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
