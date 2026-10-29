// Objetos
// Representação de um objeto real
// O objeto carro, é de uma categoria, mas com características específicas como cor, pneu, etc (são chamadas de chaves)

// chave e valor
let produto = {
    //  chave  valor
    nome: 'Mouse Gamer',
    preco: 89.90,
    categoria: 'Informática,'
}
console.log(produto);

// Desestruturação:
console.log(produto.nome);
console.log(`R$ ${produto.preco.toFixed(2)}`); // Como finalizou o valor, eu posso passar um método.

// JSON é uma lista de objetos em formato de texto

// Array ou listas
// Forma de guardar múltiplos valores dentro de uma mesma variável
// texto, numeros inteiros ou flutuantes, booleano, chamar funcao, variavel, lista e objetos
// let nomes = ['texto', 1, 7.8, true, App(), produto, [], {} ]

let nomes = ['Ana', 'João', 'Pedro', 'Lucas'];
console.log(nomes);
console.log(nomes[0]);

// Lista de objetos
let produtos = [
    {
        nome: 'Teclado Mecânico',
        preco: 199.90,
        categoria: 'Informática',
    },
    {
        nome: 'Cadeira Gamer',
        preco: 899.90,
        categoria: 'Móveis',
    },
    {
        nome: 'Monitor 24',
        preco: 749.90,
        categoria: 'Informática',
    },
]

// Para invocar um método, tem que fazer em uma variável
// Simplifica a pesquisa 
produtos.forEach((produto) => {
    console.log(`${produto.nome} - R$ ${produto.preco.toFixed(2)}`)
});

// Classes

class Pessoa {
    // constructor constrói um modelo para criar objetos
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
    // Criação de um método próprio
    apresentar() {
        console.log(`Olá, nome é ${this.nome} e tenho ${this.idade} anos.`)
    }
};

// Sempre que for usar a classe chama o método new
let pessoa1 = new Pessoa('João', 30)
console.log(pessoa1)
let pessoa2 = new Pessoa('Augusto', 22)
console.log(pessoa2)
// A ideia da linguagem orientada a objteos é construir objetos (modelos) para que eu possa usá-los no decorrer do meu código

// Variável com método que eu criei
pessoa1.apresentar()
pessoa2.apresentar()

//DOM
//1º temos que 'pegar' o que vamos manipular
//2º manipular o que pegamos

let listaProdutos = document.getElementById('lista-produtos');

produtos.forEach((produto) => {
    // innerHTML seria uma espécie de injeção de conteúdo no html.
    // += soma e guarda o valor antigo
    listaProdutos.innerHTML += `
        <div>
            <h2>${produto.nome}</h2>
            <p>Preço: R$ ${produto.preco.toFixed(2)}</p>
            <p>Categoria: R$ ${produto.categoria}</p>
            <hr>
        </div>
    `
})