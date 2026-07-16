from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:8776@localhost:5432/postgres"


engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

class Punjab(Base):
    __tablename__ = "All_Districts"
    district_name = Column(String , primary_key=True)
    district_code = Column(Integer)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

district = Punjab (
    district_name = "Lahore",
    district_code = 7689
)

db.add(district)
db.commit()
db.refresh(district)
db.close()
