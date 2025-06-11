# competitor_filter.py
import streamlit as st
import pandas as pd
import psycopg2

def get_filtered_competitors():
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="sports_radar",
        user="postgres",
        password="your_password"  # Replace with your actual password
    )
    cur = conn.cursor()

    # Fetch all competitors and their ranks
    query = """
    SELECT c.competitor_id, c.name, c.country, c.country_code, c.abbreviation,
           r.rank, r.movement, r.points, r.competitions_played
    FROM sports_radar_schema.competitors c
    JOIN sports_radar_schema.competitor_rankings r
    ON c.competitor_id = r.competitor_id
    """
    cur.execute(query)
    data = cur.fetchall()

    columns = ["ID", "Name", "Country", "Country Code", "Abbreviation", "Rank", "Movement", "Points", "Competitions Played"]
    df = pd.DataFrame(data, columns=columns)

    cur.close()
    conn.close()

    st.subheader("🔍 Search and Filter Competitors")

    # --- Search ---
    search_name = st.text_input("Search by Name")
    if search_name:
        df = df[df["Name"].str.contains(search_name, case=False)]

    # --- Filter ---
    rank_range = st.slider("Rank Range", int(df["Rank"].min()), int(df["Rank"].max()), (1, 100))
    df = df[(df["Rank"] >= rank_range[0]) & (df["Rank"] <= rank_range[1])]

    countries = df["Country"].dropna().unique()
    selected_country = st.selectbox("Filter by Country", options=["All"] + list(sorted(countries)))
    if selected_country != "All":
        df = df[df["Country"] == selected_country]

    points_threshold = st.slider("Minimum Points", 0, int(df["Points"].max()), 0)
    df = df[df["Points"] >= points_threshold]

    st.write(f"### Filtered Results ({len(df)} records)")
    st.dataframe(df, use_container_width=True)
