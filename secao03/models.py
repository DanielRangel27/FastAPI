from typing import Optional
from pydantic import BaseModel
from pydantic import validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def validar_titulo(cls, value):
        palavras  = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('o titulo deve ter pelo menos 3 palavras')

        return value

cursos = [
    Curso(id=1, titulo='a b Leigos', aulas=42, horas=56),
    Curso(id=2, titulo='a b Logica', aulas=52, horas=66),
]