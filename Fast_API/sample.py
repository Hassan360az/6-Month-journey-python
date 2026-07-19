from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

# Database Connection
DATABASE_URL = "postgresql://postgres:8776@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)


# Company Table
class Company(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)

    company_name = Column(String)


# Mobile Table
class Mobile(Base):

    __tablename__ = "mobiles"

    id = Column(Integer, primary_key=True)

    mobile_name = Column(String)

    company_id = Column(
        Integer,
        ForeignKey("companies.id")
    )


# Create Tables
Base.metadata.create_all(bind=engine)

print("Tables Created Successfully")


# Open Database Session
db = SessionLocal()


# Create Company Object
new_company = Company(
    company_name="Apple"
)

# Save Company
db.add(new_company)
db.commit()
db.refresh(new_company)

print("Company Added")


# Create Mobile Object
new_mobile = Mobile(
    mobile_name="iPhone 16",
    company_id=new_company.id
)

# Save Mobile
db.add(new_mobile)
db.commit()
db.refresh(new_mobile)

print("Mobile Added")


# Close Session
db.close()