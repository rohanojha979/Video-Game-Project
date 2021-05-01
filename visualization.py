import plotly.graph_objects as go

def plot():
    fig = go.Figure()

    fig.add_trace( go.Line( x = [i for i in range(10)] , y = [ i*i for i in range(10) ] ) )

    return fig

def plotBar(datapoints, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    for template in ["plotly_dark"]:
        fig.update_layout(template=template)
    fig.add_trace( go.Bar(x = datapoints.index,y= datapoints.values.flatten()))
    return fig

def plotLine(datapoints, title, xlabel, ylabel):
    
    layout = go.Layout(title= title,
                    xaxis=dict(title=xlabel),
                    yaxis=dict(title=ylabel))
    fig = go.Figure(layout = layout)
    for template in ["plotly_dark"]:
        fig.update_layout(template=template)
    fig.add_trace( go.Line(x = datapoints.index,y= datapoints.values.flatten()))
    return fig

