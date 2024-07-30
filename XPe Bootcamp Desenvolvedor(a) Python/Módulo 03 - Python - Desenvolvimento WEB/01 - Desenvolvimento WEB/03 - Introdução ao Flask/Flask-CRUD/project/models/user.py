from typing import Dict

from project.app import database


class User(database.Model):

    __tablename__ = "tab_users"

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(30))
    age = database.Column(database.String(30))
    address = database.Column(database.String(120))

    def serialize(self) -> Dict[str, str]:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "address": self.address,
        }
