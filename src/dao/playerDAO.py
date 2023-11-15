from configparser import ConfigParser
from src.utils import get_Cursor
import urllib.parse as up
import psycopg2
from src.dao.Player import Player


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
class PlayerDAO:

    def __init__(self):
        pass

    def findByName(self, name):
        conn, crsr = get_Cursor()
        try:
            crsr.execute(f"SELECT * FROM players WHERE username='{name}'")
            result = crsr.fetchone()
            selected_player = Player(result[0], result[1], result[2], result[3], result[4], result[5])
            return selected_player


        except Exception as e:
            print(e)
        
        finally:
            crsr.close()
            conn.close()
        return None



crsr = conn.cursor()

crsr.execute("INSERT INTO players VALUES('Pyaire', 0, 0, 1000, 0, 0)")
crsr.execute("SELECT * FROM players")
print(crsr.fetchone())
crsr.close()
conn.close()