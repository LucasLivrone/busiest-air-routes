from app.db.database import Base
from sqlalchemy import Column, Integer, String


class Routes(Base):
    __tablename__ = "Routes"
    route = Column(String, primary_key=True)
    flights = Column(Integer)
