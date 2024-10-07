from sqlalchemy.orm import Session
from persistence.bindings.binding import Binding
from typing import List, Optional

class BindingRepository:
    def __init__(self, session: Session):
        self.session = session
        self._cached_bindings = self._get_all()

    def get_bindings(self) -> list[Binding]:
        return self._cached_bindings
    
    def get_by_name(self, name: str) -> Binding | None:
        for binding in self._cached_bindings:
            if binding.name == name:
                return binding
        return None
    
    def get_by_bind_from(self, bind_from: str) -> Optional[Binding]:
        for binding in self._cached_bindings:
            if binding.bind_from == bind_from:
                return binding
        return None

    def add(self, binding: Binding) -> None:
        self.session.add(binding)
        self.session.commit()
        self._cached_bindings = self._get_all()

    def toggle_enable_by_name(self, name: str) -> None:
        binding = self.get_by_name(name)
        if binding:
            binding.toggle_enable_state()
            self.session.merge(binding)
            self.session.commit()
            self._cached_bindings = self._get_all()

    def delete_by_name(self, name: str) -> None:
        binding = self.get_by_name(name)
        if binding:
            self.session.delete(binding)
            self.session.commit()
            self._cached_bindings = self._get_all()

    def _get_all(self) -> list[Binding]:
        return self.session.query(Binding).all()
    
    


    