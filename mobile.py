import plotly.figure_factory as ff
import pandas as pd 
#pandas is used for modifications
df = pd.read_csv("data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Rating"], show_hist=False )
fig.show()