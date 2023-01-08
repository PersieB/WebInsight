

"""
The methods below perform data model operations on the users table
"""

import sqlite3
connection = sqlite3.connect('../web_insights.db', check_same_thread=False)
cursor = connection.cursor()
from passlib.hash import sha256_crypt  # library for hashing password


"""
Signup first checks whether a username already exists by finding its password
If password is found, it returns false meaning that the user already exists
Otherwise, it inserts the new credentials and returns true indicating success
"""
def signup(username, email, password):
    hashed_password = sha256_crypt.hash(password)
    connection = sqlite3.connect('../web_insights.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT password FROM users WHERE username = '{username}';
        """.format(username=username)
    )
    exist = cursor.fetchone()
    if exist is None:
        cursor.execute("""
            INSERT INTO users(username, email, password)VALUES ('{username}', '{email}', '{password}');
            """.format(username=username, email=email, password=hashed_password)
        )
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return ('false')
    
    return ('true')


# Returns the password of an already existing user, and false otherwise
def check_pasword(username):
    connection = sqlite3.connect('../web_insights.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT password FROM users WHERE username = '{username}';
        """.format(username=username)
    )

    password = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    if password is None:
        return ('false')
    else:
        return password[0]

    
 # Returns user id based on its username   
def get_user_id(username):
    connection = sqlite3.connect('../web_insights.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT user_id FROM users WHERE username = '{username}';
        """.format(username=username)
    )

    userid = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return userid[0]


# need to fix table errorgi