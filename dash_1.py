import dash
import dash_core_components as dcc # for graphs
import dash_html_components as html # tags and divs

app = dash.Dash() # start an application

# html of the entire project 
#app.layout = html.Div('Dash vizualisations')

# hreader 1 tag
app.layout = html.Div(children = [
  html.H1('Dash 1'), # header 1
  dcc.Graph(id = 'example',
         figure = {
            'data' : [
              {'x' : [1,2,3,4,5],'y' : [5,6,7,8,9],'type' : 'line','name' : 'boats'},
              {'x' : [6,7,8,9,10],'y' : [3,5,2,6,3],'type' : 'bar','name' : 'dogs'},
              {'x' : [11,12,13,14,15],'y' : [2,4,5,2,5],'type' : 'line','name' : 'messing'},
              {'x' : [11,12,13,14,15],'y' : [2,4,5,2,5],'type' : 'bar','name' : 'ricksy'}
            ],
            'layout' : {'title' : 'Dash Basic Plotting'}
         }
    )
  ])

# run the application
if __name__ == '__main__':
    app.run_server(debug=True)

