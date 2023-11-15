import urllib.parse as up
import psycopg2
from configparser import ConfigParser 

def get_Cursor():

    conf = ConfigParser()
    conf.read('.\\res\\data.ini')
    up.uses_netloc.append("postgres")
    url = up.urlparse(conf['PostgreSQL']['URL'])
    conn = psycopg2.connect(database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )
    crsr = conn.cursor()
    return conn, crsr 