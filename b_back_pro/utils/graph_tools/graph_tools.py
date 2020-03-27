import numpy as np
from matplotlib import pyplot as plt


def plot_data(data ):
    p = np.array(data)
    v = np.arange(len(data))
    print(v)
    plt.plot(v, p, color='blue')

    plt.show()
