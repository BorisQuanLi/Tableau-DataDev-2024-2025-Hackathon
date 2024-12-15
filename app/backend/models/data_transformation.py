from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class PayrollData(Base):
    __tablename__ = 'payroll_data'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    employee_name = Column(String)
    payroll_year = Column(Integer)
    base_salary = Column(Float)
    total_ot_pay = Column(Float)
    total_other_pay = Column(Float)
    total_pay = Column(Float)

def transform_data(raw_data):
    # Implement transformation logic here
    transformed_data = raw_data  # Placeholder for actual transformation logic
    return transformed_data

# Database setup
DATABASE_URL = "postgresql://your_username:your_password@localhost/tableau_data_dev"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
