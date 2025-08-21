from pydantic import BaseModel


class Relacao(BaseModel):
    text: str


class InputDataStr(BaseModel):
    elemento_tecnologico: str
    descricao: str
    desafio: str
    metodologia: str
    complemento: str