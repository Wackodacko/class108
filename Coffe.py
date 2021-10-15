import random
import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd

df=pd.read_csv("cups of coffee vs hours of sleep.csv")
dg=pd.read_csv("data.csv")
fig=ff.create_distplot([df["Coffee in ml"].tolist()],["Coffee"],show_hist=False)
fig1=ff.create_distplot([dg["Height(Inches)"].tolist()],["Height"],show_hist=False)
fig.show()
fig1.show()

#bell curve