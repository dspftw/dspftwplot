import numpy as np
from matplotlib import pyplot as plt

from dspftw import decimal_convert_to_base, vector_power

def constellation_plot(constellation: np.array, binary_mode: int=0, scale: int=100):
    """
    Plots symbol numbers at corresponding constellation points

    Parameters
    ----------
    constellation:
       QAM constellation as a row numpy array vector of complex numbers
    binary_mode:
       Mode for printing symbols: 0 = decimals (default), 1 = binary
    scale:
       Size of characters on plot (default 100)

    Returns power normalized constellation as a numpy array
    """

    # Ensure constellation is a 1-dimensional complex array
    con = constellation.flatten().astype(complex)

    # Constellation size
    con_size = len(con)

    # Check Parameters
    # Constellations must contain at least 1 element
    if con_size < 1:
        raise ValueError("constellation_plot constellation size must be at least 1")

    # If user provided mode, then it must be 0 or 1
    if binary_mode not in (0, 1):
        raise ValueError("constellation_plot binary_mode must be 0 or 1")

    # If user provided sceale, then it must be nonnegative
    if scale < 0:
        raise ValueError("constellation_plot scale must be nonnegative")

    # Number of bits per symbol
    bps = np.ceil(np.log2(con_size)).astype(int)

    # Plotting logic
    plt.suptitle(f"Scatterplot of {con_size}-point constellation")
    size = 1

    for k in np.arange(0, con_size):
        # Determine plot scale

        # Decimal Mode
        if binary_mode == 0:
            # Number of decimal digits in k
            if k == 0:
                ndigit = 1
            else:
                ndigit = np.floor(np.log10(k))+1
            size = scale * ndigit
            txt = f"${k}$"

        # Binary Mode
        elif binary_mode == 1:
            size = scale * bps
            tmp = decimal_convert_to_base(k, 2, bps).flatten()
            # Convert binary array to string
            txt = "$"

            for idx in np.arange(0, bps):
                txt = f"{txt}{tmp[idx]}"

            txt = f"{txt}$"

        plt.scatter(con[k].real, con[k].imag, s=size, marker=txt, c='k')

    plt.show()

    # Return power normalized constellation
    return (con/np.sqrt(vector_power(con))).flatten()

def conplot(*args, **kwargs) -> np.array:
    '''
    Alias for constellation_plot.
    '''
    return constellation_plot(*args, **kwargs)
