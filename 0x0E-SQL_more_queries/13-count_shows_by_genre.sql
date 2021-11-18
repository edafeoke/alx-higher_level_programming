-- a script that lists all genres from hbtn_0d_tvshows and displays the number
-- of shows linked to each.
SELECT tv_genres.name, COUNT(*) AS number_of_shows FROM tv_genres GROUP BY tv_shows.name;
