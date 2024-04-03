from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = 'zalman'
DB_PASSWORD = 'hyperion'
DB_NAME = 'fastapi'

SQL_ALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# try:
#     conn = engine.connect()
# except Exception as e:
#     print("Connecting to database failed")
#     print("Errors goes", e)
