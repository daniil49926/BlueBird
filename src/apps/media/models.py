from sqlalchemy import Column, ForeignKey, Integer, String

from core.db.database import Base


class Media(Base):
    __tablename__ = "Media"
    media_id: int = Column(Integer, primary_key=True, index=True)
    media_path: str = Column(String, nullable=False)
    media_name: str = Column(String, nullable=False)
    owner_id: int = Column(
        ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"),
        index=True,
        nullable=False,
    )
