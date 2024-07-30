from typing import Dict

from project.app import database


class User(database.Model):
    
    # Nome da tabela
    __tablename__: str = "tab_users"

    # Colunas
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    telefone = database.Column(database.String(14), nullable=False)
    endereco = database.Column(database.String(200), nullable=False)
    cpf = database.Column(database.String(11), unique=True, nullable=False)


    def serialize(self) -> Dict[str, str]:
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'endereco': self.endereco,
            'cpf': self.cpf
        }
    