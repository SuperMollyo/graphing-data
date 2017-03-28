import plotly as py
import plotly.graph_objs as go


data_file = open("spectrogram_0_log_domain.data", "r")

# read in and parse data file, and create a 2D array
list_of_data = []
for line in data_file.readlines():
		list_of_data.append(line.split(','))

#use a heatmap to plot data and make a spectrogram
data = [
    go.Heatmap(
        z= list_of_data,
        colorscale= 'Greys'
    )
]
py.offline.plot(data, filename='spectrogram-heatmap.html')
