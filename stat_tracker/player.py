from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from stat_tracker.db import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)

    matches = relationship("Match", back_populates="player", cascade="all, delete-orphan")
    ranks = relationship("Rank", back_populates="player", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Player(id={self.id}, username={self.username}, email={self.email})>"
