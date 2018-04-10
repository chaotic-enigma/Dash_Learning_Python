import random
import time
from collections import deque
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Event, Output, Input
import plotly.graph_objs as go

app = dash.Dash(__name__)

# data lists
max_lenth = 50
times = deque(maxlen=max_lenth)
oil_temps = deque(maxlen=max_lenth)
intake_temps = deque(maxlen=max_lenth)
coolant_temps = deque(maxlen=max_lenth)
rpms = deque(maxlen=max_lenth)
speeds = deque(maxlen=max_lenth)
throttle_pos = deque(maxlen=max_lenth)

data_dict = {'Oil Temperature' : oil_temps,
				 'Intake Temperature' : intake_temps,
				 'Coolant Temperature' : coolant_temps,
				 'RPM' : rpms,
				 'Speed' : speeds,
				 'Throttle Position' : throttle_pos}

def obd_data_values(times,oil_temps,intake_temps,coolant_temps,rpms,speeds,throttle_pos):
	times.append(time.time()) # enter the current time

	# take entirely random data
	if len(times) == 1:
		oil_temps.append(random.randrange(180,230))
		intake_temps.append(random.randrange(95,115))
		coolant_temps.append(random.randrange(170,220))
		rpms.append(random.randrange(1000,9500))
		speeds.append(random.randrange(30,140))
		throttle_pos.append(random.randrange(10,90))
	else:
		for any_data in [oil_temps,intake_temps,coolant_temps,rpms,speeds,throttle_pos]:
			any_data.append(any_data[-1]+any_data[-1]*random.uniform(-0.0001,0.0001))

	return times,oil_temps,intake_temps,coolant_temps,rpms,speeds,throttle_pos

times,oil_temps,intake_temps,coolant_temps,rpms,speeds,throttle_pos = obd_data_values(times,oil_temps,intake_temps,coolant_temps,rpms,speeds,throttle_pos)

app.layout = html.Div([
		html.Div([
				html.H2('Vehicle Sensors',style = {'float' : 'left'})
			]),
		dcc.Dropdown(id = 'data_names',
						 options = [{'label' : s,'value' : s} for s in data_dict.keys()],
						 value = ['Coolant Temperature','Oil Temperature','Intake Temperature'],
						 multi = True
						),
		html.Div(children=html.Div(id='graphs'),className='row'),
		dcc.Interval(id='graph_update',interval=1000)
	],
	# laying out the content
	className = 'container',style = {'width' : '98%','margin-left' : 10,'margin-right' : 10,'max_width' : 50000})

@app.callback(
		Output('graphs','children'),
		[Input('data_names','value')],
		events = [Event('graph_update','interval')]
	)

def update_live_stream(data_names): # id value of Dropdown
	graphs = []
	obd_data_values(times,oil_temps,intake_temps,coolant_temps,rpms,speeds,throttle_pos)

	# grid materialisation
	if len(data_names) > 2:
		class_choice = 'col s12 m6 l4'
	elif len(data_names) == 2:
		class_choice = 'col s12 m6 l6'
	else:
		class_choice = 'col s12 m6 l12'

	for particular_data in data_names:
		data = go.Scatter(
				x = list(times),
				y = list(data_dict[particular_data]),
				name = str(particular_data),
				fill = 'tozeroy',
				fillcolor = '#82e0aa'
			)
		graphs.append(html.Div(dcc.Graph(
				id = str(particular_data),
				animate = True,
				figure = {'data' : [data],'layout' : go.Layout(xaxis=dict(range=[min(times),max(times)]),
							yaxis=dict(range=[min(data_dict[particular_data]),max(data_dict[particular_data])]),
							margin = {'l' : 50,'r' : 1,'t' : 45,'b' : 1},
							title = '{}'.format(str(particular_data)))
						}
			),className = class_choice))

	return graphs

# external scripts
external_css = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css']
for css in external_css:
	app.css.append_css({'external_url' : css})

external_js = ['https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js']
for js in external_js:
	app.scripts.append_script({'external_url' : js})


if __name__ == '__main__':
	app.run_server(debug=True)