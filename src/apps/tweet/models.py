import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from core.db.database import Base


class Tweet(Base):
    __tablename__ = "Tweet"
    id: int = Column(Integer, primary_key=True)
    content: str = Column(String, nullable=False)
    author: int = Column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    _datetime: datetime.datetime = Column(DateTime)


class TweetMediaReferences(Base):
    __tablename__ = "TweetMediaReferences"
    id: int = Column(Integer, primary_key=True)
    tweet_id: int = Column(
        ForeignKey("Tweet.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    media_id: int = Column(
        ForeignKey("Media.media_id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )


class TweetLikes(Base):
    __tablename__ = "TweetLikes"
    id: int = Column(Integer, primary_key=True)
    tweet_id: int = Column(
        ForeignKey("Tweet.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    user_id: int = Column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
