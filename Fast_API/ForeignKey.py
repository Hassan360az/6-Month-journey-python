from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql://postgres:8776@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Company(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)

    company_name = Column(String)

company_names = Company(
    id = 10,
    company_name = "Apple"
)

class Mobile(Base):

    __tablename__ = "mobiles"

    id = Column(Integer, primary_key=True)

    mobile_name = Column(String)

    company_id = Column(
        Integer,
        ForeignKey("companies.id")
    )

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully")