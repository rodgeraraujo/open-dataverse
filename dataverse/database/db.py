import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('./config.ini')

def connect():
    try:
        return psycopg2.connect(
            user = config['postgreSQL']['user'],
            password = config['postgreSQL']['password'],
            host = config['postgreSQL']['host'],
            port = config['postgreSQL']['port'],
            database = config['postgreSQL']['database']
        )
    except (Exception, psycopg2.Error) as error :
        return None
        print ("Error while connecting to PostgreSQL", error)