import streamlit as st
from db import get_db_connection
from queries import get_summary_stats, get_top_competitors,get_highest_point_competitors,get_competitor_details,get_country_analysis, get_filtered_competitors_from_db

st.title("Sports Radar Dashboard")

conn = get_db_connection()

st.header("📊 Homepage Dashboard")
summary_df = get_summary_stats(conn)
st.metric("Total Competitors", int(summary_df['total_competitors'][0]))
st.metric("Countries Represented", int(summary_df['num_countries'][0]))
st.metric("Highest Points", int(summary_df['max_points'][0]))

st.subheader("🔍 Search and Filter Competitors")
with st.sidebar:
        st.header("Filters")
        name_filter = st.text_input("Search by Name")
        rank_min, rank_max = st.slider("Rank Range", 1, 500, (1, 100))
        country_filter = st.text_input("Filter by Country (Leave blank for all)")
        points_filter = st.slider("Minimum Points", 0, 10000, 0)

country_filter = country_filter if country_filter.strip() != '' else None

df = get_filtered_competitors_from_db(
        conn,
        name_filter=name_filter,
        rank_range=(rank_min, rank_max),
        country_filter=country_filter,
        min_points=points_filter
    )

st.write(f"### Filtered Results ({len(df)} records)")
st.dataframe(df, use_container_width=True)

if not df.empty:
        selected = st.selectbox("Select Competitor to View Details", df['name'].unique())
        if selected:
            selected_id = df[df['name'] == selected]['competitor_id'].iloc[0]
            details_df = get_competitor_details(conn, selected_id)
            st.subheader(f"📋 Competitor Details: {selected}")
            st.table(details_df)
st.subheader("🌍 Country-Wise Analysis")
country_df = get_country_analysis(conn)
st.dataframe(country_df, use_container_width=True)

st.subheader("🏆 Leaderboards")
st.markdown("**Top Ranked Competitors**")
st.dataframe(get_top_competitors(conn), use_container_width=True)

st.markdown("**Competitors with Highest Points**")
st.dataframe(get_highest_point_competitors(conn), use_container_width=True)

conn.close()