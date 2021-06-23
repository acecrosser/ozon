-- Database: shorturl

-- DROP DATABASE shorturl;

CREATE DATABASE shorturl
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Russian_Russia.1251'
    LC_CTYPE = 'Russian_Russia.1251'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

GRANT ALL ON DATABASE shorturl TO postgres;

GRANT TEMPORARY, CONNECT ON DATABASE shorturl TO PUBLIC;

GRANT ALL ON DATABASE shorturl TO admin_shorturl;

CREATE TABLE short(
	id serial primary key,
	token text UNIQUE,
	url text,
	date date,	
);

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO postgres;