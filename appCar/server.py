from fastapi import FastAPI
#Importação do tipo de dados
from typing import List, Optional
#Importação para banco de dados
from pydantic import BaseModel
#Importação para o ID
from uuid import uuid4 
#Importação para portas
from fastapi.middleware.cors import CORSMiddleware

#roda a aplicação
app = FastAPI()
#Configuração para aceitar requisições de qualquer origem
origins = ['http://127.0.0.1:5500']

#Parâmetros para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    # Uma lista de origens que devem ter permissão para fazer solicitações de origem cruzada
    allow_origins=origins,
    #Indica que os cookies devem ser suportados para solicitações de origem cruzada
    allow_credentials=True,
    # Uma lista de métodos HTTP que devem ser permitidos para solicitações de origem cruzada
    allow_methods=["*"],
    # Uma lista de cabeçalhos de solicitação HTTP que devem ser suportados para solicitações de origem cruzada
    allow_headers=["*"],
)

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
    #Percorre a lista "banc" e verifica se o ID do carro é igual ao ID passado
    for index, car in enumerate(banc):
        #Se o ID for igual, deleta o carro
        if car.id == car_id:
            #Retorna a posição do carro
            posicion = index
            break
    #Se encontrar o carro, deleta o carro
    if posicion != -1:
        banc.pop(posicion)
        return {'message': 'Carro deletado com sucesso'}
    else:
        return {'message': 'Carro não encontrado'}