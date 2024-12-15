import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import psycopg2

# Initialize the Dash app
app = dash.Dash(__name__)

# Connect to PostgreSQL and fetch data
def fetch_data():
    conn = psycopg2.connect(
        dbname="tableau_data_dev",
        user="your_username",
        password="your_password",
        host="localhost"
    )
    df = pd.read_sql("SELECT * FROM payroll_data", conn)
    conn.close()
    return df

# Fetch data from PostgreSQL
df = fetch_data()

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
