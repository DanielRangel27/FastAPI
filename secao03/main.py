from ast import Dict
from re import T
from tkinter import N
from typing import Optional, Any, List
from fastapi import FastAPI, HTTPException, status, Response, Path, Query, Header, Depends
from models import Curso, cursos
from fastapi.responses import JSONResponse
from time import sleep

def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dado...')
        sleep(1)

app = FastAPI(title='API de cursos', version='0.0.1', description='Uma api para estudo do  fastAPI')



@app.get('/cursos', description='Retorna todos os cursos ou uma lista vazia', summary='Retorna todos os cursos', response_model=List[Curso], response_description='Cursos encontrado com sucesso')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos(curso_id: int= Path(default=None, title="ID do curso", description="Deve ser entre 1 e 2", gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso nao encontrado')

@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)

    return curso
    
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o ID {curso_id}')

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
        #return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o ID {curso_id}')

@app.get('/calculadora')
async def calcular(a: int =Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None) ,c : Optional[int]= None):
    soma = a + b
    if c:
        soma = soma + c
    print(f'X-GEEk:{x_geek}')
    
    return{"resultado": soma}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)