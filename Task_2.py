# Task 1 : Loading Data

import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import pandas as pd
import numpy as np

'''
The code below has some errors.
You need to find them and correct them
Of Course, I will help you.
'''


from plotly.figure_factory
import plotly.express as px

gapminder = px.data.gapminder()

table = create_table(gapminder.head(10))
py.iplot(table)