from pyscript import display
import pandas as pd

def pandas_plot():
    # from js import data
    # df = pd.DataFrame(data)
    # df = df.set_index("year")
    # display(df.plot(kind="bar"), target="chart")
    from datetime import datetime
    now = datetime.now()
    display(now.strftime("%m/%d/%Y, %H:%M:%S"), target="chart")
