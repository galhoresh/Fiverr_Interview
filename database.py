import os
from dotenv import load_dotenv
from psycopg2 import OperationalError
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

load_dotenv()

# Retrieve the password safely
db_pass = os.getenv("DB_PASSWORD")

DATABASE_URL = f"postgresql://postgres:{db_pass}@localhost:5432/freelancers_db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

def check_connection():
    try:
        # Connect and execute a simple query
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ SUCCESS: Database connection established.")
    except OperationalError as e:
        print(f"❌ ERROR: Could not connect to the database. \nDetails: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
