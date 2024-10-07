from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from persistence.base import Base

class Binding(Base):
    __tablename__ = 'bindings'
    __binding_separator__ = '->'

    name = Column(String, primary_key=True)
    bind_from = Column(String)
    bind_to = Column(String)
    is_enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self, name: str, bind_from: list[str], bind_to: list[str], is_enabled: bool = True):
        self.name = name
        self.bind_from = self.__binding_separator__.join(bind_from)
        self.bind_to = self.__binding_separator__.join(bind_to)
        self.is_enabled = is_enabled
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, bind_from: list[str], bind_to: list[str]) -> None:
        self.bind_from = self.__binding_separator__.join(bind_from)
        self.bind_to = self.__binding_separator__.join(bind_to)
        self.updated_at = datetime.now()

    def toggle_enable_state(self) -> None:
        self.is_enabled = not self.is_enabled
        self.updated_at = datetime.now()

    def get_bind_to(self) -> list[str]:
        return self.bind_to.split(self.__binding_separator__)