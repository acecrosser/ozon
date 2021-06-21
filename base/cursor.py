import os
from py_dotenv import read_dotenv
import psycopg2 as sql


path = os.path.abspath('../.env')
read_dotenv(path)

connect = sql.connect(
        dbname=str(os.getenv('DB_NAME')),
        user=str(os.getenv('DB_USER')),
        password=str(os.getenv('PASSWORD')),
        host=str(os.getenv('HOST')),
        port=str(os.getenv('PORT'))
    )

cursor = connect.cursor()
connect.autocommit = True


# CREATE TABLE public.short
# (
#     id serial,
#     token text,
#     url text,
#     date date,
#     PRIMARY KEY (id)
# );

# ALTER TABLE public.short
#     OWNER to postgres;