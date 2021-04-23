# vim: expandtab tabstop=4 shiftwidth=4

from .exceptions import DSPFTWPlottingException

import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact
import ipywidgets as widgets

def plot_func_slider(*args, **kwargs) -> plt.Figure:
    '''
    Plot the input function, displaying one plot per input sets.

    Parameters
    ----------
    func: function which takes N inputs
    iargs: tuple with 1D slider values, one for each inpu in the function
    str: (optional) string is for plotting parameters such as "r*-" which means
        plot it with a red line, marking the points with stars and connecting
        the stars.
    kwargs: dict
        Parameters passed through to plt.Figure.plot()
    '''

    if len(args) not in [2,3]:
        raise DSPFTWPlottingException("Input args should be 2 or 3 arguments but {} was provided".format(args))

    f = args[0]
    t = args[1]
    frmt_str = '-'
    if len(args) == 3:
        frmt_str = args[2]

    sliders_dict = {}
    sliders_keys = []    # must be in same order as defined so I'm saving the keys without using .keys()
    for i in range(len(t)):
        sliders_key = "in{}_idx".format(i)
        sliders_dict[sliders_key] = widgets.IntSlider(value=0, min=0, max=len(t[i])-1, step=1)
        sliders_keys.append(sliders_key)

    def plot_funct(*args1, **kwargs1):
        fig = plt.gcf()
        args1 = [t[i][sliders_dict[sliders_keys[i]].value] for i in range(len(t))]
        kwargs1 = f(*args1)
        data = kwargs1

        if np.isrealobj(data):
            y = data
            x = np.arange(len(y))
        else:
            x = data.real
            y = data.imag
        if len(fig.get_axes()) == 0:
            ax, = plt.plot(x, y, frmt_str, **kwargs)
        else:
            ax = fig.gca()
            ln = ax.get_lines()
            ln[0].set_data(x, y)
            ax.relim()
            ax.autoscale_view(True, True, True)
        fig.canvas.draw()

    interact(plot_funct, **sliders_dict)


def plotfs(*args, **kwargs) -> plt.Figure:
    '''
    An alias of plot_func_slider().
    '''
    return plot_func_slider(*args, **kwargs)
