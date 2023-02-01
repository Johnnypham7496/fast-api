from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from .config import settings


# if you are using sqlalchemy most of it can be copy and pasted, main this that will change is the url 
# format of the connection string that we use to pass into sqlalchemy
# we're still hardcoding our password and username into the code which is bad practice because we do not want this infomation to get checked into github
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# creating an engine and this is what sqlalchemy uses to connect with postgres
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""# this code is an example of how to run raw sql instead of using sqlalchemy
while True:

    try:  # keep in mind this is VERY BAD way of coding because everything of the database has been hardcoded. Since it is hardcoded here, once this get pushed to git, the information of the server will be public
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', 
                                password = 'Blackbird1195', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was sucessful!')
        break

    except Exception as error:
        print('Connecting to database failed')
        print('Error: ', error)
        time.sleep(2)"""