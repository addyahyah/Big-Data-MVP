"""
***************************************************************************************
*    Title: nbrun.py
*    Author: Antonino Ingargiola
*    Date: Copyright (c) 2015
*    License: MIT
*    Availability:
*      https://github.com/tritemio/nbrun/tree/91e050931c347ae48a4f5a6b8995b04e397230a2
*    Modified for this project by Anna Scott with code by Benjamin RK
***************************************************************************************

Run an Jupyter/IPython notebook, optionally passing arguments.

USAGE
-----

Copy this file in the folder containing the master notebook used to
execute the other notebooks.
"""

import os
import io
import nbformat
from IPython import get_ipython
from nbconvert.preprocessors import ExecutePreprocessor


def dict_to_code(mapping):
    """Convert input dict `mapping` to a string containing python code.

    Each key is the name of a variable and each value is
    the variable content. Each variable assignment is separated by
    a newline.

    Keys must be strings, and cannot start with a number (i.e. must be
    valid python identifiers). Values must be strings or objects with a string
    representation (change to repr(value)) which is valid python code for
    re-creating the object.
    For example: numbers, strings or list/tuple/dict
    of numbers and strings are allowed.

    Returns:
        A string containing the python code.
    """
    lines = ("{} = {}".format(key, value)
             for key, value in mapping.items())
    return '\n'.join(lines)

def run_notebook(notebook_name, nb_kwargs=None,
                 insert_pos=5, timeout=120, execute_kwargs=None):
    """Runs a notebook and displays the output in the master notebook.

    Executes a notebook, optionally passing "arguments" in a way roughly
    similar to passing arguments to a function.
    Notebook arguments are passed in a dictionary (`nb_kwargs`) which is
    converted to a string containing python code, then inserted in the notebook
    as a code cell. The code contains only assignments of variables which
    can be used to control the execution of a suitably written notebook. When
    calling a notebook, you need to know which arguments (variables) to pass.
    Differently from functions, no check on the input arguments is performed.

    Arguments:
        notebook_name (string): name of the notebook to be executed.
        nb_kwargs (dict or None): If not None, this dict is converted to a
            string of python assignments with keys representing variables
            names and values variables content. This string is inserted as
            code-cell in the notebook to be executed.
        insert_pos (int): position of insertion of the code-cell containing
            the input arguments. Default is 5 (i.e. sixth cell). With this
            default, the input notebook can define, in the first cell, default
            values of input arguments (used when the notebook is executed
            with no arguments or through the Notebook GUI).
        timeout (int): timeout in seconds after which the execution is aborted.
        execute_kwargs (dict): additional arguments passed to
            `ExecutePreprocessor`.
    """
    if nb_kwargs is not None:
        header = '# Cell inserted during automated execution.'
        code = dict_to_code(nb_kwargs)
        code_cell = '\n'.join((header, code))

    if execute_kwargs is None:
        execute_kwargs = {}
    ep = ExecutePreprocessor(timeout=timeout, **execute_kwargs)
    nb = nbformat.read(notebook_name, as_version=4)
    if len(nb_kwargs) > 0:
        nb['cells'].insert(insert_pos, nbformat.v4.new_code_cell(code_cell))

    try:
        # Execute the notebook
        ep.preprocess(nb, {'metadata': {'path': './'}})
#*****************************************
#    Title: analysis.ipynb
#    Author: Benjamin RK
#    Date: April 2013
#    Availability: https://gist.github.com/minrk/5491090

        ip = get_ipython()
        for cell in nb.cells:
            if cell.cell_type != 'code':
                continue
            ip.run_cell(cell.source)
#*****************************************
    except:
        # Execution failed, print a message then raise.
        msg = 'Error executing the notebook "%s".\n\n' % notebook_name
        print(msg)
        raise
