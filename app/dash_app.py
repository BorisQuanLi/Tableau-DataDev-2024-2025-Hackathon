import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from backend.utils.db_utils import fetch_data

# Initialize the Dash app
app = dash.Dash(__name__)

# Fetch data from PostgreSQL
try:
    df = fetch_data("SELECT * FROM payroll_data")
except Exception as e:
    df = pd.DataFrame(columns=["base_salary", "total_pay", "employee_name"])
    print(f"Error fetching data: {e}")

# Create a Plotly figure
fig = px.scatter(df, x="base_salary", y="total_pay", color="employee_name", title="Citywide Payroll Data")

# Define the layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Citywide Payroll Data Visualization'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
