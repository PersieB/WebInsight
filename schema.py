
import sqlite3
conn = sqlite3.connect('web_insights.db', check_same_thread=False)
c = conn.cursor()

# create tables

c.executescript(
    """
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20),
    email VARCHAR(100),
    password VARCHAR(225)
    );

    CREATE TABLE IF NOT EXISTS authors(
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        auth_name VARCHAR(100)
    );

    CREATE TABLE IF NOT EXISTS publications(
        pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pub_name VARCHAR(100)
    );

    CREATE TABLE IF NOT EXISTS media(
        media_id INTEGER PRIMARY KEY AUTOINCREMENT,
        media_name VARCHAR(100)
    );

    CREATE TABLE IF NOT EXISTS news(
    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title VARCHAR(225),
    date_pub DATE,
    pub_id INTEGER,
    media_id INTEGER,
    author_id INTEGER,
    Summary VARCHAR (225),
    key_id INTEGER,
    FOREIGN KEY (pub_id) REFERENCES publications(pub_id),
    FOREIGN KEY (media_id) REFERENCES media(media_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (key_id) REFERENCES keywords(key_id)
    );

    CREATE TABLE IF NOT EXISTS author_pub(
    authpub_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pub_id INTEGER,
    author_id INTEGER,
    FOREIGN KEY (pub_id) REFERENCES publications(pub_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );

    CREATE TABLE IF NOT EXISTS sentiments(
    sent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Positive DECIMAL(2,2),
    Neutral DECIMAL(2,2),
    Negative DECIMAL(2,2),
    );

    CREATE TABLE IF NOT EXISTS keywords(
        key_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Keywords VARCHAR(225)
    );


    """
)
conn.commit()
c.close()
c.close()