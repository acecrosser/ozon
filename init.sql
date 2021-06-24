-- Database: shorturl

-- DROP DATABASE shorturl;

CREATE DATABASE shorturl
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'ru_RU.UTF-8'
    LC_CTYPE = 'ru_RU.UTF-8'
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