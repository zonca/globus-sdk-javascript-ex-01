from pyscript import display
from js import console
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

def pandas_plot(*args):
    from js import data
    console.log(data)
    df = pd.read_json(StringIO(data))
    df = df.set_index("year")
    fig, ax = plt.subplots()
    df.plot(kind="bar", ax=ax)
    display(fig, target="chart")
