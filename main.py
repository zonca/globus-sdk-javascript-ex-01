from pyscript import display
import pandas as pd
from js import createObject
from pyodide import create_proxy, to_js

def pandas_plot():
    from js import data
    df = pd.DataFrame(data)
    df = df.set_index("year")
    display(df.plot(kind="bar"), target="chart")

createObject(create_proxy(pandas_plot), "pandas_plot_js")
