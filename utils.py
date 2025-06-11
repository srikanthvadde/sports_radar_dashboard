import plotly.express as px

def plot_leaderboard(df):
    return px.bar(df, x="name", y="points", color="country", title="Top Competitors")