from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    item_name = Column(String)
    price_cny = Column(Float)
    status = Column(String, default="processing")
    created_at = Column(DateTime, default=datetime.utcnow)
    tracking_number = Column(String)
    
    def save(self):
        engine = create_engine('sqlite:///storage/orders.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(self)
        session.commit()
        session.close()

def init_db():
    engine = create_engine('sqlite:///storage/orders.db')
    Base.metadata.create_all(engine)
