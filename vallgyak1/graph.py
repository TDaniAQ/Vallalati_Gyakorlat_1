import tkinter as tk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def draw_graph(raktar, eladott, btname):
    data = {'Raktárkészlet': raktar, 'Eladott': eladott}
    valname = list(data.keys())
    val = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(valname, val, color='green',
            width=0.6)

    plt.ylabel("darabszám")
    plt.title("A(z) " + btname + " nevű termék adatai")
    plt.show()
