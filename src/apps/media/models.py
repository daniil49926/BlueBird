from sqlalchemy import Column, ForeignKey, Integer, String

from core.db.database import Base


class Media(Base):
    __tablename__ = "Media"
    media_id = Column(Integer, primary_key=True, index=True)
    media_path = Column(String, nullable=False)
    media_name = Column(String, nullable=False)
    owner_id = Column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    # tweet_id = Column("Tweet.id", ...)
