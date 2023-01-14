import pandas as pd
import db_connect

conn, c = db_connect.database_connection()

# load the data into a Pandas DataFrame
df = pd.read_excel(r'../data/news.xlsx', engine='openpyxl')
# replace empty author names with Unknown
df['Author'] = df['Author'].replace(['.', '-'], 'Unknown')

#rename column names to match schema names

df.rename(columns = {'Author':'auth_name'}, inplace = True)
df.rename(columns = {'Publication Name':'pub_name'}, inplace = True)
df.rename(columns = {'Media':'media_name'}, inplace = True)
df.rename(columns = {'Publication Date':'date_pub'}, inplace = True)


# write the authors data to sqlite table
df['auth_name'].to_sql('authors', conn, if_exists='append', index = False)
c.execute('''SELECT * FROM authors''')
auth=c.fetchall()

# write the publication names to sqlite table
pubdf = df['pub_name'].unique()
pubdf = pd.DataFrame(pubdf, columns=['pub_name'])
pubdf.to_sql('publications', conn, if_exists='append', index = False)

c.execute('''SELECT * FROM publications''')
pubs = c.fetchall()




# write the media data to sqlite table
media = df['media_name'].unique()
media = pd.DataFrame(media, columns=['media_name'])
media.to_sql('media', conn, if_exists='append', index = False)

c.execute('''SELECT * FROM media''')
med = c.fetchall()

# write the sentiments data to sqlite table
sentiments = df.filter(['Positive', 'Neutral', 'Negative'], axis=1)
sentiments.to_sql('sentiments', conn, if_exists='append', index = False)
"""
c.execute('''SELECT * FROM sentiments''')
sents=c.fetchall()"""

# write the keywords data to sqlite table
df['Keywords'].to_sql('keywords', conn, if_exists='append', index = False)

c.execute('''SELECT * FROM keywords''')
keys=c.fetchall()


#replace publication names with their ids
def replace_pub(x):
    for i in pubs:
        if i[1] == x:
            x = i[0]
    return x

def replace_media(x):
    for i in med:
        if i[1] == x:
            x = i[0]
    return x

def replace_authors(x):
    for i in auth:
        if i[1] == x:
            x = i[0]
    return x

def replace_keywords(x):
    for i in keys:
        if i[1] == x:
            x = i[0]
    return x


#write news data to sqlite table
#newsdf = df.filter(['Title', 'date_pub'], axis=1)
df['pub_id'] =df['pub_name'].apply(replace_pub)
del df['pub_name']
df['media_id'] = df['media_name'].apply(replace_media)
del df['media_name']
df['author_id'] = df['auth_name'].apply(replace_authors)
del df['auth_name']
df['key_id']=df['Keywords'].apply(replace_keywords)
del df['Keywords']

#write to auth:pub table
aupub = pd.DataFrame(df, columns=['pub_id', 'author_id'])
aupub.to_sql('author_pub', conn, if_exists='append', index = False)
"""
c.execute('''SELECT * FROM author_pub''')
aupubs = c.fetchall()"""

# write to news table
newsdf = df.filter(['Title', 'date_pub', 'pub_id', 'media_id', 'author_id', 'Summary', 'key_id'], axis=1)
newsdf.to_sql('news', conn, if_exists='append', index = False)
"""
c.execute('''SELECT * FROM news''')
news = c.fetchall()
#print(news[0])"""

# write to sentiments table


