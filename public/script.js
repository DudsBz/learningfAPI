async function carregar_Carros(){
    const response = await axios.get('http://127.0.0.1:8000/listar-carros')

    console.log(response.data)
    //ele da o erro de cors
    //o erro de cors é quando o front-end tenta acessar o back-end e o back-end não permite, pois é de outra origem, outra porta etc
    //então tem que configurar o cors no backend

}

function app(){
    carregar_Carros()
    console.log("app iniciado")
}

app()