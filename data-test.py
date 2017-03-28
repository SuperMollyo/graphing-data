import plotly as py
import plotly.graph_objs as go


data_file = open("spectrogram_0_log_domain.data", "r")
# lines = data_file.read().strip().split(',')
# print lines
# print len(lines)

list_of_data = []
for line in data_file.readlines():
		list_of_data.append(line.split(','))


data = [
    go.Heatmap(
        z= list_of_data,
        colorscale= 'Greys'
    )
]
py.offline.plot(data, filename='basic-heatmap')
