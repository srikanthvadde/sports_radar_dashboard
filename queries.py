from db import run_query, run_query_params

def get_summary_stats(conn):
    query = """
    SELECT 
            (SELECT COUNT(*) FROM sports_radar_schema.competitors) AS total_competitors,
            (SELECT COUNT(DISTINCT country) FROM sports_radar_schema.competitors) AS num_countries,
            (SELECT MAX(points) FROM sports_radar_schema.competitor_rankings) AS max_points
    """
    return run_query(conn, query)

def get_top_competitors(conn, limit=10):
    query = f"""
    SELECT c.name, c.country, cr.rank, cr.points
    FROM sports_radar_schema.competitors c
    JOIN sports_radar_schema.competitor_rankings cr ON c.competitor_id = cr.competitor_id
    ORDER BY cr.points DESC
    LIMIT {limit}
    """
    return run_query(conn, query)

def get_filtered_competitors_from_db(conn, name_filter='', rank_range=(1, 100), country_filter=None, min_points=0):
    query = """
        SELECT c.competitor_id, c.name, c.country, c.country_code, c.abbreviation,
               r.rank, r.movement, r.points, r.competitions_played
        FROM sports_radar_schema.competitors c
        JOIN sports_radar_schema.competitor_rankings r
        ON c.competitor_id = r.competitor_id
        WHERE (%s = '' OR LOWER(c.name) LIKE LOWER(%s))
          AND r.rank BETWEEN %s AND %s
          AND (%s IS NULL OR c.country = %s)
          AND r.points >= %s
    """
    name_search = f"%{name_filter}%"
    params = (name_filter, name_search, rank_range[0], rank_range[1], country_filter, country_filter, min_points)
    return run_query_params(conn, query, params=params)


def get_competitor_details(conn, competitor_id):
    query = """
        SELECT c.competitor_id, c.name, c.country, c.country_code, c.abbreviation,
               r.rank, r.movement, r.points, r.competitions_played
        FROM sports_radar_schema.competitors c
        JOIN sports_radar_schema.competitor_rankings r
        ON c.competitor_id = r.competitor_id
        WHERE c.competitor_id = %s
    """
    return run_query_params(conn, query, (competitor_id,))

def get_country_analysis(conn):
    query = """
        SELECT c.country, COUNT(*) as num_competitors, AVG(r.points) as avg_points
        FROM sports_radar_schema.competitors c
        JOIN sports_radar_schema.competitor_rankings r
        ON c.competitor_id = r.competitor_id
        GROUP BY c.country
        ORDER BY avg_points DESC
    """
    return run_query(conn, query)


def get_highest_point_competitors(conn, limit=10):
    query = f"""
        SELECT c.name, r.rank, r.points
        FROM sports_radar_schema.competitors c
        JOIN sports_radar_schema.competitor_rankings r
        ON c.competitor_id = r.competitor_id
        ORDER BY r.points DESC
        LIMIT {limit}
    """
    return run_query(conn, query)
