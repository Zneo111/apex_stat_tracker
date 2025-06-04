from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from stat_tracker.db import Base

class Rank(Base):
    __tablename__ = "ranks"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    rank_name = Column(String, nullable=False)
    rank_points = Column(Integer, default=0)

    player = relationship("Player", back_populates="ranks")

    def __repr__(self):
        return f"<Rank(id={self.id}, player_id={self.player_id}, rank_name={self.rank_name}, rank_points={self.rank_points})>"
