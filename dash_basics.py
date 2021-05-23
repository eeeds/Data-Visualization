# Import required packages
"""
Let's start with

Importing necessary libraries
Reading and sampling 500 random data points
Get the chart ready
Copy the below code to the dash_basics.py script and review the code.

"""
import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')
"""
Next, we create a skeleton for our dash application. Our dashboard application has three components as seen before:

Title of the application
Description of the application
Chart conveying the proportion of distance group by month
Mapping to the respective Dash HTML tags:

Title added using html.H1() tag
Description added using html.P() tag
Chart added using dcc.Graph() tag
Copy the below code to the dash_basics.py script and review the structure.

NOTE: Copy below the current code

"""

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1('Airline Dashboard',
                                style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
                           dcc.Graph(figure=fig),
                                               
                    ])

# Run the application                   
if __name__ == '__main__':
    app.run_server()

#Update the html.H1() tag to hold the application title.

#Application title is Airline Dashboard
#Use style parameter provided below to make the title center aligned, with color code #503D36, and font-size as 40

"""
Update the html.P() tag to hold the description of the application.

Description is Proportion of distance group (250 mile distance interval group) by flights.
Use style parameter to make the description center aligned and with color #F57241.
html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
After updating the html.H1() with the application title, the app.layout will look like:

"""

