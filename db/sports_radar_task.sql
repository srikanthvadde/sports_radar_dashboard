
1)​List all competitions along with their category name

   SELECT com.*, c.category_name FROM sports_radar_schema.competition  com 
   inner join sports_radar_schema.category c on c.category_id = com.category_id

2.Count the number of competitions in each category
    SELECT 
        com.category_id,
        COUNT(DISTINCT com.competition_id) AS competition_count
    FROM 
        sports_radar_schema.competition com
    GROUP BY 
        com.category_id
    ORDER BY 
        competition_count DESC;

3.Find all competitions of type 'doubles'
    select * from sports_radar_schema.competition where type = 'doubles';

4.Get competitions that belong to a specific category (e.g., ITF Men)
    select com.*,c.category_name from sports_radar_schema.competition com
    inner join sports_radar_schema.category c on c.category_id = com.category_id
    where c.category_name = 'ITF Men';

6.Analyze the distribution of competition types by category 
    SELECT 
        category_id,
        type,
        COUNT(*) AS competition_count
    FROM 
        sports_radar_schema.competition
    GROUP BY 
        category_id, type
    ORDER BY 
        category_id, competition_count DESC;

5.Identify parent competitions and their sub-competitions 
    SELECT 
        parent.competition_id AS parent_id,
        parent.competition_name AS parent_name,
        child.competition_id AS sub_id,
        child.competition_name AS sub_name
    FROM sports_radar_schema.competition child
    JOIN sports_radar_schema.competition parent
        ON child.parent_id = parent.competition_id
    ORDER BY parent.competition_name, child.competition_name;

7.List all competitions with no parent (top-level competitions) 
    SELECT 
    c.*
    FROM sports_radar_schema.competition c where c.parent_id is NULL

-------------------------------------------------------------------


1.List all venues along with their associated complex name
    select v.*,c.complex_name from sports_radar_schema.venues v
    inner join sports_radar_schema.complexes c on v.complex_id = c.complex_id

2)​Count the number of venues in each complex 
    select count(venue_id) as venue_count,v.complex_id from sports_radar_schema.venues v
    group by v.complex_id order by venue_count desc;

3)​Get details of venues in a specific country (e.g., Chile)
    select * from sports_radar_schema.venues v 
    where v.country_name = 'Chile';

4)​Identify all venues and their timezones 
    select distinct(v.venue_name),v.country_name,v.timezone  from sports_radar_schema.venues v;

5)​Find complexes that have more than one venue 
    select c.* from sports_radar_schema.complexes c
    inner join sports_radar_schema.venues v on v.complex_id = c.complex_id
    group by c.complex_id, c.complex_name
    having count(v.venue_id) > 1;

6)​List venues grouped by country 
    SELECT v.country_name, COUNT(*) AS venue_count
    FROM sports_radar_schema.venues v
    GROUP BY v.country_name
    ORDER BY venue_count DESC;

7)​Find all venues for a specific complex (e.g., Nacional) 
    select v.*,c.complex_name from sports_radar_schema.venues v
    inner join sports_radar_schema.complexes c on v.complex_id = c.complex_id
    where c.complex_name='Nacional';

---------------------------------------------------------------------

1.Get all competitors with their rank and points.
    select c.competitor_id,c.name,cr.rank,cr.points from sports_radar_schema.competitors c
    inner join sports_radar_schema.competitor_rankings cr on cr.competitor_id = c.competitor_id

2)​Find competitors ranked in the top 5 
    SELECT 
        c.rank,
        comp.competitor_id,
        comp.name,
        comp.country,
        comp.country_code,
        comp.abbreviation
    FROM 
        sports_radar_schema.competitor_rankings c
    JOIN 
        sports_radar_schema.competitors comp
    ON 
        c.competitor_id = comp.competitor_id
    WHERE 
        c.rank <= 5
    ORDER BY 
        c.rank ASC;


3)​List competitors with no rank movement (stable rank) 
    SELECT 
        comp.competitor_id,
        comp.name,
        comp.country,
        comp.country_code,
        comp.abbreviation,
        cr.rank,
        cr.movement
    FROM 
        sports_radar_schema.competitor_rankings cr
    JOIN 
        sports_radar_schema.competitors comp
    ON 
        cr.competitor_id = comp.competitor_id
    WHERE 
        cr.movement = 0
    ORDER BY 
        cr.rank ASC;

4)​Get the total points of competitors from a specific country (e.g., Croatia) 
    select sum(cr.points) as total_points ,c.country 
    from sports_radar_schema.competitor_rankings cr
    inner join sports_radar_schema.competitors c on c.competitor_id = cr.competitor_id
    where c.country = 'Australia' group by c.country;

5)​Count the number of competitors per country 
    select COUNT(c.competitor_id) as competitor_count,c.country
    from sports_radar_schema.competitors c group by  c.country
















	
	
