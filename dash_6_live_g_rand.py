import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Event, Output
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
Y = deque(maxlen=20)

X.append(1)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div([
		dcc.Graph(id='live_graph',animate=True),
		dcc.Interval(id='graph_update',interval=1000) # time span to update (milliseconds)
	])

@app.callback(
		Output('live_graph','figure'), # data.figure
		events = [Event('graph_update','interval')]
	)

def live_plotting():
	X.append(X[-1]+1)
	Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1,0.1)))

	data = go.Scatter(
			x=list(X),
			y=list(Y),
			name='Scatter',
			mode='lines+markers'
		)

	return {'data' : [data],'layout' : go.Layout(
		xaxis=dict(range=[min(X),max(X)]),
		yaxis=dict(range=[min(Y),max(Y)]))}

if __name__ == '__main__':
	app.run_server(debug=True)

'''
dcc.Graph(id = 'example',
         figure = {
            'data' : [
              {'x' : [1,2,3,4,5],'y' : [5,6,7,8,9],'type' : 'line','name' : 'boats'},
              {'x' : [6,7,8,9,10],'y' : [3,5,2,6,3],'type' : 'bar','name' : 'dogs'}
            'layout' : {'title' : 'Dash Basic Plotting'}
         }
    )
'''