from datetime import datetime

class Binding:
    def __init__(self, name, bind_from, bind_to, is_enabled=False):
        self.name = name
        self.bind_from = bind_from
        self.bind_to = bind_to
        self.is_enabled = is_enabled
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            "name": self.name,
            "bind_from": self.bind_from,
            "bind_to": self.bind_to,
            "is_enabled": self.is_enabled,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        binding = cls(
            name=data["name"],
            bind_from=data["bind_from"],
            bind_to=data["bind_to"],
            is_enabled=data["is_enabled"]
        )
        binding.created_at = data["created_at"]
        binding.updated_at = data["updated_at"]
        return binding

    def update_timestamp(self):
        self.updated_at = datetime.now().isoformat()