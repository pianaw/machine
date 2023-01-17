import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    data = pd.read_csv('Sunspots.csv', index_col='ID')
    data.columns = ['date', 'mean']

    fig = px.line(data, x='date', y="mean", title='Monthly Mean Total Sunspot Number')
    fig.show()
