import dash
import dash_core_components as dcc # for graphs
import dash_html_components as html # tags and divs

import random

random_points_x = [random.randrange(-10,10) for i in range(10)]
random_points_y = [random.randrange(-10,10) for i in range(10)]

app = dash.Dash()

app.layout = html.Div(children = [
	html.H1('Dash 2'),
	dcc.Graph(id = 'example',
				 figure = {
				 		'data' : [
				 			{'x' : random_points_x,'y' : random_points_y,'type' : 'line','name' : 'boats'},
				 			{'x' : random_points_x,'y' : random_points_y,'type' : 'bar','name' : 'dogs'},
				 			{'x' : random_points_x,'y' : random_points_y,'type' : 'line','name' : 'messing'},
				 			{'x' : random_points_x,'y' : random_points_y,'type' : 'bar','name' : 'ricksy'}
				 		],
				 		'layout' : {'title' : 'Dash Basic Plotting'}
				}
		),
	dcc.Graph(id = 'example_1',
				 figure = {
				 		'data' : [
				 			{'x' : [2,4,1,5,6],'y' : [4,1,2,4,6],'type' : 'line','name' : 'cactus'},
				 			{'x' : random_points_x,'y' : random_points_y,'type' : 'bar','name' : 'morty'}
				 		],
				 		'layout' : {'title' : 'Dash Basic Plotting'}
				}
		)
	])

if __name__ == '__main__':
	app.run_server(debug=True)

# need to update the current file