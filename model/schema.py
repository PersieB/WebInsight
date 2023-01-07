import db_connect

conn, c = db_connect.database_connection()

# create tables

c.executescript(
    """
    CREATE TABLE users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20),
    email VARCHAR(100),
    password VARCHAR(225)
    );

    CREATE TABLE authors(
        author_id INTEGER PRIMARY KEY AUTOINCREMENT,
        auth_name VARCHAR(100)
    );

    CREATE TABLE publications(
        pub_id INTEGER PRIMARY KEY AUTOINCREMENT,
        pub_name VARCHAR(100)
    );

    CREATE TABLE media(
        media_id INTEGER PRIMARY KEY AUTOINCREMENT,
        media_name VARCHAR(100)
    );

    CREATE TABLE news(
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

    CREATE TABLE author_pub(
    authpub_id INTEGER PRIMARY KEY AUTOINCREMENT,
    pub_id INTEGER,
    author_id INTEGER,
    FOREIGN KEY (pub_id) REFERENCES publications(pub_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );

    CREATE TABLE sentiments(
    sent_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Positive DECIMAL(2,2),
    Neutral DECIMAL(2,2),
    Negative DECIMAL(2,2)
    );

    CREATE TABLE keywords(
        key_id INTEGER PRIMARY KEY AUTOINCREMENT,
        Keywords VARCHAR(225)
    );


    """
)
conn.commit()
c.close()
c.close()