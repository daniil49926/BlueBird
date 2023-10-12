import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from core.db.database import Base
from core.settings import settings


class User(Base):
    __tablename__ = "User"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    username: str = Column(String, nullable=False, unique=True)
    email: str = Column(String, nullable=False, unique=True)
    hashed_password: str = Column(String, nullable=False)
    created_at: datetime.datetime = Column(DateTime, default=datetime.datetime.now())
    is_active: int = Column(
        Integer, nullable=False, default=0 if not settings.TESTING else 1
    )


class FollowersReferences(Base):
    __tablename__ = "FollowersReferences"
    id: int = Column(Integer, primary_key=True)
    user_id: int = Column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
    follow: int = Column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
