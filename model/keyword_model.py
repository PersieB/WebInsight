"""
The methods below perform data model operations on the keywords table
"""
import sys

sys.path.append( r'C:/Users/percy/Documents/Projects/GPS/WebInsight/functions' )
import cloudwords
import sqlite3
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 


# stopwords is a collection of words that dont convey meaning. mostly pronouns such as he she etc.

# Show all todos of a particular user
def select_keywords():
    connection = sqlite3.connect('../web_insights.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT Keywords FROM keywords;
        """
    )
    all_keys = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    keyword_list = []
    for i in all_keys:
        keyword_list.append(i[0])
    str_keys = ""
    str_keys = str_keys.join(keyword_list)
    return str_keys
    cloudwords.show_keywords(str_keys)


select_keywords()

