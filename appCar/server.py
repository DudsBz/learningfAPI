from fastapi import FastAPI
#Importação do tipo de dados
from typing import List, Optional
#Importação para banco de dados
from pydantic import BaseModel
#Importação para o ID
from uuid import uuid4 

#roda a aplicação
app = FastAPI()
#Criação da classe Car, objeto que será utilizado para armazenar os dados de carros
#Possui o id, o modelo, o ano e o preço
class Car(BaseModel):
    id: Optional[str]
    model: str
    year: int
    price: float
#Criação de uma lista de carros
#"banc" é uma lista de objetos do tipo Car
#"List" é um tipo de dado que armazena uma lista
#A lista "banc" é inicializada com um objeto do tipo Car
#"Car" é o objeto que será armazenado na lista
banc: List[Car] = []
#Criação de uma rota para listar os carros
@app.get('/listar-carros')
def list_cars():
    return banc
#Criação de uma rota para adicionar carros
@app.post('/c-cars')
#Função que recebe um objeto do tipo Car e adiciona na lista "banc"
def input_cars(car: Car):
    car.id = str(uuid4())
    banc.append(car)
    return banc

@app.get('/obter-carros/{car_id}')
def get_cars(car_id: str):
   #Percorre a lista "banc" e verifica se o ID do carro é igual ao ID passado
    for car in banc:
        #Se o ID for igual, retorna o carro
        if car.id == car_id:
            #Retorna o carro
            return car
    #Se não encontrar o carro, retorna uma mensagem
    return {'message': 'Carro não encontrado'}

@app.delete('/obter-carros/{car_id}')
def del_cars(car_id: str):
    posicion = -1
    for index, car in enumerate(banc):
        if car.id == car_id:
            posicion = index
            break
    if posicion != -1:
        banc.pop(posicion)
        return {'message': 'Carro deletado com sucesso'}
    else:
        return {'message': 'Carro não encontrado'}