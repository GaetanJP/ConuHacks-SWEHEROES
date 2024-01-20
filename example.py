import plotly.graph_objects as go
import pandas as pd
import json
import random


# Sample data (replace this with your actual data)
def load_data(json_file):
    with open(json_file, "r") as file:
        return json.load(file)


data = load_data("./dataset/Exchange_1.json")
all_stocks = set()

for message in data:
    all_stocks.add(message["Symbol"])

number_of_colors = len(all_stocks)

color = [
    "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])
    for i in range(number_of_colors)
]

symbol_to_color = {}
all_stocks = list(all_stocks)

for i in range(len(all_stocks)):
    symbol_to_color[all_stocks[i]] = color[i]

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Create a Plotly figure
fig = go.Figure()

# Initialize a dictionary to store tree data
trees = {}

# Iterate over each row in the DataFrame
for _, row in df.iterrows():
    exchange = row["Exchange"]
    symbol = row["Symbol"]
    order_price = row["OrderPrice"]

    # Check if the tree exists, if not, create it
    if exchange not in trees:
        trees[exchange] = {"symbol": [], "order_price": []}

    # Add the order as a leaf to the tree
    trees[exchange]["symbol"].append(symbol)
    trees[exchange]["order_price"].append(order_price)

# Create a scatter plot for each tree
for exchange, tree_data in trees.items():
    fig.add_trace(
        go.Scatter(
            x=[exchange] * len(tree_data["order_price"]),
            y=tree_data["order_price"],
            mode="markers",
            marker=dict(
                size=10,
                color=list(
                    symbol_to_color.values()
                ),  # Use color to represent different symbols
                colorscale="Viridis",
                opacity=0.8,
            ),
            name=exchange,
        )
    )

# Update layout for better visualization
fig.update_layout(
    title="Seeing the Forest for the Trees",
    xaxis=dict(title="Exchange"),
    yaxis=dict(title="Order Price"),
    showlegend=True,
)

# Show the animated plot
fig.show()
