import json
import dash
from dash import html
from dash import dcc
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from flask import Flask
from flask_restful import Resource, Api
import sys
sys.path.append(r'C:\Users\AVIGNAN NAG\OneDrive\Desktop\Python_Files\PycharmProjects\dashboard_project\backend_scripts\db_scripts')
from connect_2_db import get_db_data
sys.path.append(r'C:\Users\AVIGNAN NAG\OneDrive\Desktop\Python_Files\PycharmProjects\dashboard_project\backend_scripts')
from backend_request import make_charts


# Creating a flash server
server = Flask(__name__)
app = dash.Dash(server=server, external_stylesheets=[dbc.themes.DARKLY])
app.title = "AVANTEL DASHBOARD"

# Graphs = html.Div(children = [
# html.Div(children = ["Graph 1", dcc.Graph(id="pie_chart_id", figure=pie_chart)], #dash graph element
# style = {'width': '45%', "position": "fixed", "left": "2%",
#          'display': 'inline-block', 'text-align': 'center',
#          'top': '12%', 'border': '2px solid red', 'height':'61.5%'}
# ),
# html.Div(children = ["Graph 2", dcc.Graph(id="bar_chart_id", figure=bar_chart)], #dash graph element
# style = {'width': '45%', 'position': 'fixed', 'left': '53%',
#          'display': 'inline-block', 'text-align': 'center',
#          'top': '20%', 'border': '2px solid red', 'height':'61.5%'}
# )
# ])


app.layout = html.Div([

html.Div(
className = "row",children =[
    html.Div(className='six columns', children=[
        dcc.Dropdown(
            id='dropdown_job_title',
            placeholder="Select a Job Title",
                    options=[
                        {'label': 'Data Scientist', 'value': 'Data Scientist'},
                        {'label': 'Machine Learning Engineer', 'value': 'Machine Learning Engineer'},
                        {'label': 'Data Analyst', 'value': 'Data Analyst'}
                    ],
                    value='Data Scientist',
                    multi=False,
                    clearable=False,
                    searchable=False,
        )], style={'cursor': 'pointer', 'color': 'black', 'border': '2px solid cyan'})
    ,html.Div(className='six columns', children=[
        dcc.Dropdown(
        id='dropdown_time_period',
        placeholder="Select a Year",
        options=[
            {'label': '2020', 'value': '2020'},
            {'label': '2021', 'value': '2021'},
            {'label': '2022', 'value': '2022'}
        ],
        value='2020',
        clearable=True,
        multi=False,
        searchable=False,
    )], style={'background-color': 'dimgrey', 'cursor': 'pointer', 'color': 'black'})
  ]),

html.Div(id ="main_div",                           # , children=[Graphs]
         style={'padding':'0',
                'width':'100%', 'height':'100%', 'border': '2px solid cyan',
                'height':'100%'}
             )
])


@app.callback(
    dash.dependencies.Output("main_div", "children"),
    [
        dash.dependencies.Input("dropdown_job_title", "value"),
        dash.dependencies.Input("dropdown_time_period", "value"),
    ],  # dropdown_chart_type
)

def update_graph(selected_value_1,selected_value_2):
    html_children = []
    if selected_value_1 == "Data Scientist":
        if selected_value_2 == "2020":
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
            html.Div(
                children=[
                    'Chart-1',
                    dcc.Graph(
                        id='pie_chart',
                        figure=fig_pie.add_trace(
                            go.Pie(
                                labels=temp_df[0]["column_names"],
                                values=temp_df[0]["column_values"],
                            ),
                        ),
                    ),
                ],
                style={
                    "width": "45%",
                    "left": "2%",
                    "display": "inline-block",
                    "text-align": "center",
                    "top": "10%",
                    "border": "2px solid red",
                    "height": "41.5%",
                    "margin": "10px",
                    # "background-color": "dimgrey",
                    "cursor": "pointer",
                    # "color": "black",
                    # "overflow": "scroll",
                },
            )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
        elif selected_value_2 == "2021":
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
                html.Div(
                    children=[
                        'Chart-1',
                        dcc.Graph(
                            id='pie_chart',
                            figure=fig_pie.add_trace(
                                go.Pie(
                                    labels=temp_df[0]["column_names"],
                                    values=temp_df[0]["column_values"],
                                ),
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
        else:
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
                html.Div(
                    children=[
                        'Chart-1',
                        dcc.Graph(
                            id='pie_chart',
                            figure=fig_pie.add_trace(
                                go.Pie(
                                    labels=temp_df[0]["column_names"],
                                    values=temp_df[0]["column_values"],
                                ),
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
    elif selected_value_1 == "Data Analyst":
        if selected_value_2 == "2020":
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
            html.Div(
                children=[
                    'Chart-1',
                    dcc.Graph(
                        id='pie_chart',
                        figure=fig_pie.add_trace(
                            go.Pie(
                                labels=temp_df[0]["column_names"],
                                values=temp_df[0]["column_values"],
                            ),
                        ),
                    ),
                ],
                style={
                    "width": "45%",
                    "left": "2%",
                    "display": "inline-block",
                    "text-align": "center",
                    "top": "10%",
                    "border": "2px solid red",
                    "height": "41.5%",
                    "margin": "10px",
                    # "background-color": "dimgrey",
                    "cursor": "pointer",
                    # "color": "black",
                    # "overflow": "scroll",
                },
            )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
        elif selected_value_2 == "2021":
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
            html.Div(
                children=[
                    'Chart-1',
                    dcc.Graph(
                        id='pie_chart',
                        figure=fig_pie.add_trace(
                            go.Pie(
                                labels=temp_df[0]["column_names"],
                                values=temp_df[0]["column_values"],
                            ),
                        ),
                    ),
                ],
                style={
                    "width": "45%",
                    "left": "2%",
                    "display": "inline-block",
                    "text-align": "center",
                    "top": "10%",
                    "border": "2px solid red",
                    "height": "41.5%",
                    "margin": "10px",
                    # "background-color": "dimgrey",
                    "cursor": "pointer",
                    # "color": "black",
                    # "overflow": "scroll",
                },
            )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
        else:
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
            html.Div(
                children=[
                    'Chart-1',
                    dcc.Graph(
                        id='pie_chart',
                        figure=fig_pie.add_trace(
                            go.Pie(
                                labels=temp_df[0]["column_names"],
                                values=temp_df[0]["column_values"],
                            ),
                        ),
                    ),
                ],
                style={
                    "width": "45%",
                    "left": "2%",
                    "display": "inline-block",
                    "text-align": "center",
                    "top": "10%",
                    "border": "2px solid red",
                    "height": "41.5%",
                    "margin": "10px",
                    # "background-color": "dimgrey",
                    "cursor": "pointer",
                    # "color": "black",
                    # "overflow": "scroll",
                },
            )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
    else:
        if selected_value_2 == "2020":
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
            html.Div(
                children=[
                    'Chart-1',
                    dcc.Graph(
                        id='pie_chart',
                        figure=fig_pie.add_trace(
                            go.Pie(
                                labels=temp_df[0]["column_names"],
                                values=temp_df[0]["column_values"],
                            ),
                        ),
                    ),
                ],
                style={
                    "width": "45%",
                    "left": "2%",
                    "display": "inline-block",
                    "text-align": "center",
                    "top": "10%",
                    "border": "2px solid red",
                    "height": "41.5%",
                    "margin": "10px",
                    # "background-color": "dimgrey",
                    "cursor": "pointer",
                    # "color": "black",
                    # "overflow": "scroll",
                },
            )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
        elif selected_value_2 == "2021":
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
            html.Div(
                children=[
                    'Chart-1',
                    dcc.Graph(
                        id='pie_chart',
                        figure=fig_pie.add_trace(
                            go.Pie(
                                labels=temp_df[0]["column_names"],
                                values=temp_df[0]["column_values"],
                            ),
                        ),
                    ),
                ],
                style={
                    "width": "45%",
                    "left": "2%",
                    "display": "inline-block",
                    "text-align": "center",
                    "top": "10%",
                    "border": "2px solid red",
                    "height": "41.5%",
                    "margin": "10px",
                    # "background-color": "dimgrey",
                    "cursor": "pointer",
                    # "color": "black",
                    # "overflow": "scroll",
                },
            )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
        else:
            result_dict = get_db_data(selected_value_1, selected_value_2)
            temp_df = make_charts(result_dict)
            fig_pie = go.Figure()
            fig_bar = go.Figure()
            html_children.append(
            html.Div(
                children=[
                    'Chart-1',
                    dcc.Graph(
                        id='pie_chart',
                        figure=fig_pie.add_trace(
                            go.Pie(
                                labels=temp_df[0]["column_names"],
                                values=temp_df[0]["column_values"],
                            ),
                        ),
                    ),
                ],
                style={
                    "width": "45%",
                    "left": "2%",
                    "display": "inline-block",
                    "text-align": "center",
                    "top": "10%",
                    "border": "2px solid red",
                    "height": "41.5%",
                    "margin": "10px",
                    # "background-color": "dimgrey",
                    "cursor": "pointer",
                    # "color": "black",
                    # "overflow": "scroll",
                },
            )
            )
            html_children.append(
                html.Div(
                    children=[
                        "Chart_2",
                        dcc.Graph(
                            id="Bar_chart",
                            figure=fig_bar.add_trace(
                                go.Bar(
                                    x=temp_df[0]["column_names"],
                                    y=temp_df[0]["column_values"],
                                )
                            ),
                        ),
                    ],
                    style={
                        "width": "45%",
                        "left": "2%",
                        "display": "inline-block",
                        "text-align": "center",
                        "top": "10%",
                        "border": "2px solid red",
                        "height": "41.5%",
                        "margin": "10px",
                        # "background-color": "dimgrey",
                        "cursor": "pointer",
                        # "color": "black",
                        # "overflow": "scroll",
                    },
                )
            )
            Graphs = html.Div(children=html_children.copy())
            return Graphs
    



if __name__ == "__main__":
    app.run_server(debug=True, port='8080')