from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from stat_tracker.db import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False)
    game_mode = Column(String, nullable=False)
    kills = Column(Integer, default=0)
    deaths = Column(Integer, default=0)
    score = Column(Integer, default=0)
    date_played = Column(DateTime, default=lambda: datetime.utcnow().replace(microsecond=0))

    player = relationship("Player", back_populates="matches")

    def __repr__(self):
        return (f"<Match(id={self.id}, player_id={self.player_id}, game_mode={self.game_mode}, "
                f"kills={self.kills}, deaths={self.deaths}, score={self.score}, "
                f"date_played={self.date_played.strftime('%Y-%m-%d %H:%M:%S')})>")
