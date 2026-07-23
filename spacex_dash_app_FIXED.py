# Import required libraries
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Read the SpaceX launch data
spacex_df = pd.read_csv("spacex_launch_dash.csv")

max_payload = spacex_df["Payload Mass (kg)"].max()
min_payload = spacex_df["Payload Mass (kg)"].min()

# Create the Dash application
app = Dash(__name__)

# Create the application layout
app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={
                "textAlign": "center",
                "color": "#503D36",
                "fontSize": 40,
            },
        ),

        # TASK 1: Launch-site dropdown
        dcc.Dropdown(
            id="site-dropdown",
            options=[
                {"label": "All Sites", "value": "ALL"},
                *[
                    {"label": site, "value": site}
                    for site in sorted(spacex_df["Launch Site"].unique())
                ],
            ],
            value="ALL",
            placeholder="Select a launch site",
            searchable=True,
            clearable=False,
            style={"width": "80%", "margin": "0 auto"},
        ),

        html.Br(),

        # TASK 2: Pie chart
        html.Div(dcc.Graph(id="success-pie-chart")),

        html.Br(),
        html.P("Payload range (kg):"),

        # TASK 3: Payload-range slider
        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            marks={i: f"{i}" for i in range(0, 10001, 1000)},
            value=[min_payload, max_payload],
            tooltip={"placement": "bottom", "always_visible": False},
        ),

        # TASK 4: Scatter chart
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ]
)


# TASK 2: Update the pie chart
@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value"),
)
def get_pie_chart(entered_site):
    if entered_site == "ALL":
        success_counts = (
            spacex_df.groupby("Launch Site", as_index=False)["class"]
            .sum()
            .rename(columns={"class": "Successful Launches"})
        )

        return px.pie(
            success_counts,
            values="Successful Launches",
            names="Launch Site",
            title="Total Successful Launches by Site",
        )

    filtered_df = spacex_df[spacex_df["Launch Site"] == entered_site]

    outcome_counts = (
        filtered_df["class"]
        .value_counts()
        .reindex([0, 1], fill_value=0)
        .rename(index={0: "Failed", 1: "Successful"})
        .reset_index()
    )
    outcome_counts.columns = ["Outcome", "Count"]

    return px.pie(
        outcome_counts,
        values="Count",
        names="Outcome",
        title=f"Launch Outcomes for {entered_site}",
    )


# TASK 4: Update the payload scatter chart
@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [
        Input("site-dropdown", "value"),
        Input("payload-slider", "value"),
    ],
)
def get_scatter_plot(entered_site, payload_range):
    low, high = payload_range

    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low)
        & (spacex_df["Payload Mass (kg)"] <= high)
    ]

    if entered_site != "ALL":
        filtered_df = filtered_df[
            filtered_df["Launch Site"] == entered_site
        ]

    title = (
        "Payload Mass versus Launch Outcome for All Sites"
        if entered_site == "ALL"
        else f"Payload Mass versus Launch Outcome for {entered_site}"
    )

    return px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title=title,
        labels={"class": "Launch outcome (0 = failed, 1 = successful)"},
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
