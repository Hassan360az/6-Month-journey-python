from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:8776@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(bind=engine)

db = SessionLocal()

user = User(
    name="Hassan",
    is_active=True
)

db.add(user) 
db.commit()
db.refresh(user)
print(user.name)
db.close()
