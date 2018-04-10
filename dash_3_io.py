import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output # to create user Input and Output

app = dash.Dash()
#print(dir(app))

app.layout = html.Div(children=[
		# Input not from dcc.dependencies
		dcc.Input(id='input',value='',type='text'), # creates a field
		html.Div(id='output') # output could be anything unlike the functionality of javascript, it takes the id of the dcc.dependencies.Output (referance from the @app.callback)
	])

# wrapping up (decorators)
@app.callback(
	# Output provided with list of inputs
	Output(component_id='output',component_property='children'),
	[Input(component_id='input',component_property='value')] # referance from the app.layout
	)

def update_value(input_data):
	try:
		return 'Output: {}'.format(str(float(input_data)**2))
	except:
		return 'Stack overflow'


if __name__ == '__main__':
	app.run_server(debug=True)