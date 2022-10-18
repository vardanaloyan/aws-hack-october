from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME="database-1-instance-1.cyreumlnhmm6.eu-west-1.rds.amazonaws.com"
USERNAME="postgres"
PASSWORD="jacaranda"
SQLALCHEMY_DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOSTNAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
