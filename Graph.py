import pandas as pd
from plotly.subplots import make_subplots
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
import plotly.express as px



#Reading the file

df = pd.read_csv("C:\\Users\Ruth's PC\OneDrive\Documents\Essex\Second Year\CE201-5-FY Team Project\Individual Project\ExamResults1.csv")



fig = px.scatter(df, x="Average", y="CSE101",trendline="ols")
fig.update_layout(height=600, width=800,)

fig.show()
