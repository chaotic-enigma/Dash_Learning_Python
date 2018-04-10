import pandas_datareader.data as web
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output

start = datetime.datetime(2015,1,1) # starting time
end = datetime.datetime.now() # ending time till now

stock = 'TSLA'
df = web.DataReader(stock,'morningstar',start,end)

df.reset_index(inplace=True)
df.set_index("Date",inplace=True) # set 'Date' as the starting index
df = df.drop('Symbol',axis=1) # drops the column at axis 1
#print df.head()

app = dash.Dash(__name__)

app.layout = html.Div(children=[
		html.H1("Plotting finance data"),
		dcc.Graph(id = 'example_plot',
					 figure = {
					 	'data' : [
					 		{'x' : df.index,'y' : df.Close,'type' : 'line','name' : 'Close'
					 		}],
					 	'layout' : {'title' : 'DV of ' + str(stock)}
					 }
					)
	])

if __name__ == '__main__':
	app.run_server(debug=True)