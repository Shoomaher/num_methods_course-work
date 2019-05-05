import logging
import math
from collections import namedtuple
from sympy.abc import x
from sympy.utilities.lambdify import lambdify

Params = namedtuple('Params', ['expression', 'left_edge', 'right_edge'])
ACCURACY = 0.00001


""" Half-division method calculating
"""


def calc(setup: Params):
    """ Make calculations in a loop
    return DataFrame with processing
    """
    data = []
    left = setup.left_edge
    right = setup.right_edge
    middle = left + (right-left)/2
    fun = lambdify(x, setup.expression)

    tmp = {
        'left': left,
        'left_val': fun(left),
        'middle': middle,
        'middle_val': fun(middle),
        'right': right,
        'right_val': fun(right),
    }

    logging.info('Started processing...')

    i = 0
    curr_acc = 0  # Current accuracy

    while True:
        i += 1
        curr_acc = round(
            math.fabs(tmp['left'] - tmp['right']), 4)

        if curr_acc <= ACCURACY:
            break

        if tmp['middle_val'] < 0:
            tmp['left'] = tmp['middle']
        else:
            tmp['right'] = tmp['middle']

        tmp['middle'] = tmp['left'] + (tmp['right']-tmp['left'])/2
        tmp['middle_val'] = fun(tmp['middle'])

        data.append(tmp)

        if i > 1000:
            logging.error('Iteration error')
            return None

    logging.info('Result: {}'.format(tmp['middle']))
    return data
