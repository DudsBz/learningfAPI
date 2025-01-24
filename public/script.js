//Criar uma função assíncrona que carrega a lista de carros do backend e exibe na tela
async function carregarCarros(){
    //fazendo uma requisição get para o backend
    const response = await axios.get('http://127.0.0.1:8000/listar-carros')
    //o response é o que o backend respondeu
    const carros = response.data
    //ele da o erro de cors
    //o erro de cors é quando o front-end tenta acessar o back-end e o back-end não permite, pois é de outra origem, outra porta etc
    //então tem que configurar o cors no backend
    
    //pegando a lista de carros e adicionando na tela
    const lista = document.getElementById('lista_carros')
    //para cada carro, criar um item na lista
    carros.forEach(car => {
        const item = document.createElement('li')
        //adicionando o modelo do carro no item
        item.innerHTML = car.model
        //adicionando o item na lista
        lista.appendChild(item)
    });
}

async function formularioCarro() {
    const form_carro = document.getElementById('form_car')
    const model = document.getElementById('input_model_car')

    form_carro.onsubmit = async (event) => {
        event.preventDefault();
        const model_car = model.value;
        try {
            await axios.post('http://127.0.0.1:8000/c-cars', {
                model: model_car,
                year: 2022,
                price: 240000.00
            });
            alert(`${model_car} cadastrado com sucesso!`);
            // Recarregar a lista de carros após o cadastro
            carregarCarros();
        } catch (error) {
            console.error('Erro ao cadastrar carro:', error);
            alert('Erro ao cadastrar carro.');
        }
    };
}
function app(){
    console.log("app iniciado")
    carregarCarros()
    formularioCarro()
}
app()