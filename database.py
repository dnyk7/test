# database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an engine
# For SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # For simplicity & quick setup, start w SQLite. Can switch to PostgreSQL later if needed.#
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the database model
Base = declarative_base()

# new class for the database, from git copilor
class UserTable(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, index=True)


# Create all tables
Base.metadata.create_all(bind=engine)

# Create a session
db = SessionLocal()

# Query for all data in the table
data = db.query(UserTable).all()

# Iterate and print data
for row in data:
    print(row.id, row.data)

# Close the session
db.close()