from sqlalchemy import Column, ForeignKey, Integer, String

from core.db.database import Base


class User(Base):
    __tablename__ = "User"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String, nullable=False)
    api_key: str = Column(String, nullable=False)


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
