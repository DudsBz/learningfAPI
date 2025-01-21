#importação da API
from fastapi import FastAPI
#Importação do tipo de dados
from typing import List
#Importação para banco de dados
from pydantic import BaseModel

#roda a aplicação
app = FastAPI()

#Criação da classe Car, objeto que será utilizado para armazenar os dados de carros
#Possui o id, o modelo, o ano e o preço
class Car(BaseModel):
    id: int
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
    banc.append(car)
    return banc
        