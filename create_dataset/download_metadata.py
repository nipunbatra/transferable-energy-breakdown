import psycopg2 as db
import pandas as pd
database_host = 'dataport.pecanstreet.org'
database_port = '5434'
database_name = 'postgres'
database_schema = 'university'
database_username='dqeRSAITtEVb'
database_password='GIr6e3WIXpI0'

conn = db.connect('host=' + database_host +
                          ' port=' + database_port +
                          ' dbname=' + database_name +
                          ' user=' + database_username +
                          ' password=' + database_password)

sql_query = """SELECT * from university.metadata"""
df = pd.read_sql(sql_query, conn)
df.to_csv("metadata/metadata.csv", index=False)
