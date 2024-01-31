from datetime import timezone

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, func, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
Base = declarative_base()


class TodoList(Base):
    __tablename__ = "todo_list"

    id = Column(UUID, primary_key=True)
    title = Column(String(50))
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))


class TodoItem(Base):
    __tablename__ = "todo_item"
    id = Column(UUID, primary_key=True)
    title = Column(String(50))
    list_id = Column(ForeignKey(TodoList.id), nullable=False)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(tz=timezone.utc))
