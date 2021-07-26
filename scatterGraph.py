import pandas as pd
import plotly.express as pe

df = pd.read_csv('Copy+of+data+-+data.csv')
graph = pe.scatter(df, x = 'date', y = 'cases', title = 'Corona Cases', color = 'country')
graph.show()