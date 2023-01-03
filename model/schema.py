import sqlite3
conn = sqlite3.connect('web_insights.db', check_same_thread=False)
c = conn.cursor()

# create tables

c.executescript(
    """
    CREATE TABLE app_users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname VARCHAR(50),
    lname VARCHAR(50),
    username VARCHAR(20),
    email VARCHAR(100),
    password VARCHAR(225)
    );

    CREATE TABLE authors(
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname VARCHAR(50),
        lname VARCHAR(50)
    );

    CREATE TABLE publications(
        pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100)
    );

    CREATE TABLE media(
        media_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100)
    );

    CREATE TABLE news(
    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(225),
    date_pub DATE,
    pub_id INTEGER,
    media_id INTEGER,
    author_id INTEGER,
    FOREIGN KEY (pub_id) REFERENCES publications(pub_id),
    FOREIGN KEY (media_id) REFERENCES media(media_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );

    CREATE TABLE author_pub(
    authpub_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pub_id INTEGER,
    author_id INTEGER,
    FOREIGN KEY (pub_id) REFERENCES publications(pub_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );

    CREATE TABLE sentiments(
    sent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    positive DECIMAL(2,2),
    neutral DECIMAL(2,2),
    negative DECIMAL(2,2)
    );

    """
)
conn.commit()
c.close()
c.close()