from src.models.base import Base

import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Service(Base):
    __tablename__ = "services"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    parent_id = Column(
        UUID(as_uuid=True), ForeignKey(f"{__tablename__}.id"), nullable=True
    )

    parent = relationship("Service", remote_side=[id], backref="children")

    def __repr__(self):
        return f"<Service(id={self.id}, name={self.name}, parent_id={self.parent_id})>"
