import logging
import os
import tkinter as tk
from collections import namedtuple
from pathlib import PureWindowsPath
from tkinter import *
from tkinter import messagebox, ttk

import sympy
from matplotlib.pyplot import annotate
from sympy.abc import x
from sympy.plotting import plot

from half_div import ACCURACY, calc
from table import Table

""" Main script for half-division method implementation
Process the function calculation using sympy
"""

Params = namedtuple('Params', ['expression', 'left_edge', 'right_edge'])


def validation_error(details):
    """ Show validation error message """
    logging.error(details)
    messagebox.showerror('Validation error', details)


def validate_data(raw_expr, a_edge, b_edge):
    """ Validate entered data"""
    left_edge = None
    right_edge = None
    expression = None

    if (not a_edge.get()) or (not b_edge.get()) or (not raw_expr.get()):
        validation_error('Not all data was entered')
        return None

    try:
        left_edge = float(a_edge.get().replace(',', '.'))
        right_edge = float(b_edge.get().replace(',', '.'))
    except ValueError:
        validation_error('Wrong values in edges')
        return None

    try:
        expression = sympy.sympify(raw_expr.get())
    except sympy.SympifyError as e:
        logging.error(e)
        return None

    if x not in expression.free_symbols:
        validation_error('Used wrong variable in expression')
        return None

    if len(expression.free_symbols) > 1:
        validation_error('Extra variables present')
        return None

    logging.info('Left edge: {}'.format(left_edge))
    logging.info('Right edge: {}'.format(right_edge))
    logging.info('Expression: {}'.format(expression))

    if right_edge < left_edge:
        right_edge, left_edge = left_edge, right_edge
        logging.info('Swapped edges')

    logging.info('Successful parsing!')
    return Params(expression=expression, left_edge=left_edge, right_edge=right_edge)


def process(params: Params):
    """ Process the method """
    if not params:
        logging.error('No params provided!')
        return

    proc_hist = calc(params)

    if not proc_hist:
        messagebox.showerror('Error!', 'Unable to process')
        return

    # last middle in the processing history:
    result = round(proc_hist[-1][2], 5)

    process_window = Toplevel()
    process_window.title('Process half-division method')
    main_frame = ttk.Frame(process_window, padding='10 10 10 10')
    main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    p = plot(params.expression, (x, params.left_edge, params.right_edge),
             show=False, title=str(params.expression))
    # p.append(plot(result, 0, (x, result, result+ACCURACY),
    #               line_color='red', linestyle='-', show=False)[0])

    show_plot_btn = ttk.Button(
        main_frame, text='Show plot', command=lambda: p.show()).grid(column=1, row=0)

    ttk.Label(main_frame, text='Result: {}'.format(
        result)).grid(column=0, row=0)
    ttk.Label(main_frame, text='Accuracy: {}'.format(
        ACCURACY)).grid(column=0, row=1)

    # to_show = reduce(lambda full_list, ind: full_list +
    #                  [list(ind.values()), ], proc_hist, [])

    table = Table(main_frame, headings=('left', 'left_va;', 'middle',
                                        'middle_val', 'right', 'right_val'), rows=tuple(proc_hist))

    table.grid(column=0, row=2, rowspan=12, sticky=tk.S)

    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)


if __name__ == "__main__":
    logging.basicConfig(filename=PureWindowsPath(os.path.realpath(__file__)).parent / 'last_run.log',
                        filemode='w', level=logging.INFO)

    root = Tk()
    root.title('Half-division method')
    main_frame = ttk.Frame(root, padding='3 3 12 12')
    main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # init vars
    expr = StringVar()  # Expression to evaluate
    a = StringVar()
    b = StringVar()

    ttk.Label(main_frame, text='Enter expression:').grid(
        column=1, row=1, sticky=tk.W, columnspan=2)

    ttk.Label(main_frame, text='Enter edges:').grid(
        column=3, row=1, sticky=tk.W, columnspan=2)

    ttk.Label(main_frame, text='f(x) =').grid(
        column=1, row=2, sticky=tk.W)

    ttk.Label(main_frame, text='Left:').grid(
        column=3, row=2, sticky=tk.W)

    ttk.Label(main_frame, text='Right:').grid(
        column=5, row=2, sticky=tk.W)

    a_entry = ttk.Entry(main_frame, width=4, textvariable=a)
    a_entry.grid(column=4, row=2, sticky=tk.E)

    b_edge_entry = ttk.Entry(main_frame, width=4, textvariable=b)
    b_edge_entry.grid(column=6, row=2, sticky=tk.E)

    run_btn = ttk.Button(main_frame, text='RUN!',
                         command=lambda: process(validate_data(expr, a, b))).grid(column=7, row=2)

    expr_entry = ttk.Entry(main_frame, width=18, textvariable=expr)
    expr_entry.grid(column=2, row=2, sticky=tk.E)

    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    expr_entry.focus()

    logging.info('GUI init finished')
    root.mainloop()
    logging.info('Finished running')
