import plotly.graph_objects as go

def plot():
    fig = go.Figure()

    fig.add_trace( go.Line( x = [i for i in range(10)] , y = [ i*i for i in range(10) ] ) )

    return fig

def plotBar(datapoint , title , xlabel , ylabel):
    fig = go.Figure()

    layout = go.Layout(title = title,
                        xaxis = dict(title = xlabel),
                        yaxis = dict(title = ylabel))

    fig = go.Figure(layout = layout)

    fig.add_trace( go.Bar( x = datapoint.index , y = datapoint.values ) )

    return fig

def PlotLine(x,y):
    fig = go.Figure()

    fig.add_trace(go.Line( x = x, y = y))

    return fig