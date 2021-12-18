import csv
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('class107.csv')
student_df = df.loc[df['student_id'] == 'TRL_imb']

print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    y = student_df.groupby("level")["attempt"].mean(),
    x = ["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation = 'v'
))

fig.show()