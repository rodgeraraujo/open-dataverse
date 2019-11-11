import configparser
import psycopg2

config = configparser.ConfigParser()
config.read('./config.ini')

def connect():
    try:
        # return psycopg2.connect(
        #     user = config['postgreSQL']['user'],
        #     password = config['postgreSQL']['password'],
        #     host = config['postgreSQL']['host'],
        #     port = config['postgreSQL']['port'],
        #     database = config['postgreSQL']['database']
        # )

        return psycopg2.connect(
            user = 'postgres',
            password = 'secret',
            host = '127.0.0.1',
            port = '5432',
            database = 'dataverse'
        )

    except (Exception, psycopg2.Error) as error :
        return None
        print ("Error while connecting to PostgreSQL", error)