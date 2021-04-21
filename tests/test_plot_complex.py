# vim: expandtab tabstop=4 shiftwidth=4

import unittest

import numpy as np
import dspftwplot

class PlottingTests(unittest.TestCase):
    def test_plot_complex(self):
        num_plots = 7
        num_points = 100
        complex_data_raw = np.random.randn(num_points, num_plots) + 1J*np.random.randn(num_points, num_plots)
        offsets = 8*np.exp(1J*2*np.pi*np.arange(num_plots)/num_plots).reshape((1,-1))
        complex_data = complex_data_raw + offsets
        dspftwplot.plot_complex(complex_data, '*-')
