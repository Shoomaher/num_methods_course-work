from tkinter import *
from tkinter import ttk, messagebox
import logging
import pandas
import matplotlib
import sympy
from sympy.abc import x
import os
from collections import namedtuple
from pathlib import PureWindowsPath

""" Main script for half-division method implementation
Gonna store data in pandas DataFrame
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

    if (not a_edge.get()) or (not b_edge.get()):
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
    return None


if __name__ == "__main__":
    logging.basicConfig(filename=PureWindowsPath(os.path.realpath(__file__)).parent / 'last_run.log',
                        filemode='w', level=logging.DEBUG)

    root = Tk()
    root.title('Half-division method')
    main_frame = ttk.Frame(root, padding='3 3 12 12')
    main_frame.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # init vars
    expr = StringVar()  # Expression to evaluate
    a = StringVar()
    b = StringVar()

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

    a_entry = ttk.Entry(main_frame, width=4, textvariable=a)
    a_entry.grid(column=4, row=2, sticky='E')

    b_edge_entry = ttk.Entry(main_frame, width=4, textvariable=b)
    b_edge_entry.grid(column=6, row=2, sticky='E')

    run_btn = ttk.Button(main_frame, text='RUN',
                         command=lambda: process(validate_data(expr, a, b))).grid(column=7, row=2)

    expr_entry = ttk.Entry(main_frame, width=18, textvariable=expr)
    expr_entry.grid(column=2, row=2, sticky='E')

    for child in main_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    expr_entry.focus()

    root.bind('<Return>', process(validate_data(expr, a, b)))
    logging.info('GUI init finished')
    root.mainloop()
    logging.info('Finished running')
