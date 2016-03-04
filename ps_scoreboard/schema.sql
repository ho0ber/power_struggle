create table if not exists scores(
  id integer primary key,
  post_id integer,
  steam_id integer,
  name text,
  score integer,
  timestamp datetime default current_timestamp
);

create table if not exists rosters(
  steam_id integer,
  clan_id integer,
  clan_name text
  timestamp datetime default current_timestamp
);

create table if not exists current_scores(
  steam_id text,
  score integer,
  timestamp datetime default current_timestamp
);

create table if not exists hall_of_fame(
  id integer primary key,
  start_date date,
  end_date date,
  name text,
  members text,
  score integer,
  timestamp datetime default current_timestamp
);

