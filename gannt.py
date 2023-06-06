import plotly.express as px
import pandas as pd

# Define the project phases
phases = ['Requirements Gathering and Analysis', 'System Design and Architecture', 'Development and Implementation',
          'Data Visualization and Reporting', 'Deployment and User Training', 'Evaluation and Maintenance']

# Define the start and end dates for each phase
start_dates = ['2023-06-01', '2023-07-01', '2023-09-01', '2023-11-01', '2023-12-16', '2023-12-16']
end_dates = ['2023-06-30', '2023-08-31', '2023-10-31', '2023-12-15', '2023-12-31', '2023-12-31']

# Create a DataFrame with the phase, start date, and end date
df = pd.DataFrame({'Phase': phases, 'Start Date': start_dates, 'End Date': end_dates})

# Convert the date columns to datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'])
df['End Date'] = pd.to_datetime(df['End Date'])

# Create the Gantt chart
fig = px.timeline(df, x_start="Start Date", x_end="End Date", y="Phase")

# Customize the appearance of the chart
fig.update_layout(
    title="Project Timeline",
    xaxis_title="Date",
    yaxis_title="Phases",
    yaxis=dict(autorange="reversed")
)

# Show the chart
fig.show()
