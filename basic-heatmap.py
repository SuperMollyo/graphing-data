import plotly as py
import plotly.graph_objs as go

data = [
    go.Heatmap(
        z=[[1, 20, 30],
           [20, 1, 60],
           [30, 60, 1]]
    )
]
py.offline.plot(data, filename='basic-heatmap')
