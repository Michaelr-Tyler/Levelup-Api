SELECT * FROM levelupapi_gametype;
SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;
SELECT * FROM levelupapi_game;
SELECT * FROM levelupapi_event;
SELECT * FROM levelupapi_eventgamer;

SELECT
    g.id,
    g.title,
    g.gametype_id,
    g.number_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name,
    
FROM
    levelupapi_game g
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id;

SELECT
    e.id,
    e.day,
    e.time,
    e.location,
    e.game_id,
    e.gamer_id,
    u.first_name || ' ' || u.last_name AS full_name,
    g.title,
    eg.id event_gamer_id
    
FROM levelupapi_event e
JOIN levelupapi_game g ON g.id = e.game_id
JOIN levelupapi_gamer gr ON gr.id = e.gamer_id
JOIN levelupapi_eventgamer eg ON eg.gamer_id = g.id
JOIN auth_user u ON gr.user_id = u.id;

SELECT
    eg.id,
    eg.gamer_id,
    u.first_name || ' ' || u.last_name AS full_name,
    eg.event_id,
    e.location,
    e.time,
    e.day,
    g.title
    
FROM levelupapi_eventgamer eg
JOIN levelupapi_event e ON e.id = eg.event_id
JOIN levelupapi_gamer gr ON gr.id = eg.gamer_id
JOIN levelupapi_game g ON g.id = e.game_id
JOIN auth_user u ON u.id = gr.user_id;
