from sqlalchemy import column, Integer, string, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:8776@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)


Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

#Model

class City_Names(Base):
    __tablename__ = "Names_of_Cities"
    name = column(string)
    id = column(Integer)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

Punjab = City_Names(
    name = "Lahore",
    id = 9823
)

db.add(Punjab)
db.commit()
db.refresh(Punjab)

student = db.query(Punjab).filter(Punjab.id == 1).first()

student.name = "Ali"

db.commit()

db.refresh(student)

print(student.name)

db.close()



