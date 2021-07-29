import sqlite3
from datetime import date


rssUrl = [
    'https://g1.globo.com/rss/g1/tecnologia/'
]

con = sqlite3.connect('oldNewNews.db')
cur = con.cursor()

cur.execute(
    f'''CREATE TABLE IF NOT EXISTS "news" (
            "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
            "title"	TEXT,
            "data"	TEXT,
            "text"	TEXT,
            "collected_at" TEXT
        );
    '''
)


for url in rssUrl:
    pass


con.commit()
con.close()
