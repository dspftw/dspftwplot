from ipywidgets import interact
from ipywidgets.widgets import IntSlider

import matplotlib.pyplot as plt
import numpy as np

from .exceptions import DSPFTWPlottingException

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

    if len(args) not in (2, 3):
        raise DSPFTWPlottingException(f"Input args should be 2 or 3 arguments but {args} was provided")

    f = args[0]
    t = args[1]
    frmt_str = '-'

    if len(args) == 3:
        frmt_str = args[2]

    sliders_dict = {}
    sliders_keys = []    # must be in same order as defined so I'm saving the keys without using .keys()

    for i, tval in enumerate(t):
        sliders_key = f"in{i}_idx"
        sliders_dict[sliders_key] = IntSlider(value=0, min=0, max=len(tval)-1, step=1)
        sliders_keys.append(sliders_key)

    def plot_funct(*args1, **kwargs1):
        fig = plt.gcf()
        args1 = [tval[sliders_dict[sliders_keys[i]].value] for i, tval in enumerate(t)]
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
