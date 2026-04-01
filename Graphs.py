import pandas as pd
import plotly.express as px

df = pd.read_csv('countries.csv')

#Easy way to clean the data, remove commas and convert to numeric, then fill NaN with 0 and convert to int(Important so remember this)
df["Population"] = pd.to_numeric(df["Population"].astype(str).str.replace(",", ""), errors="coerce")
df["Area"] = pd.to_numeric(df["Area"].astype(str).str.replace(",", ""), errors="coerce")


df["Population"] = df["Population"].fillna(0).astype(int)
df["Area"] = df["Area"].fillna(0).astype(int)

top_pop = df.sort_values("Population", ascending=False).head(15)

fig = px.bar(
    top_pop,
    x="Name",
    y="Population",
    text="Population",
    title="Top 15 Most Populated Countries",
    labels={"Population": "Population", "Name": "Country"},
)

fig.update_layout(xaxis_tickangle=-45)
fig.show()