// Função definida

function verificaPar() {
    let entrada = parseInt(prompt('Digite um número: '))
    if (isNaN(entrada)) {
        alert('Número inválido! Por favor, digite um número válido.')
        return;
    }
    if (entrada % 2 === 0) {
        alert(`${entrada} é par.`);
    } else {
        alert(`${entrada} é impar.`);
    }
}
verificaPar();

let resultado = 0; // Se cplocar a variável como const, ela não vai funcionar, pois ela é um valor constante
let entrada1 = parseInt(prompt('Digite o primeiro valor: '))
let entrada2 = parseInt(prompt('Digite o segundo valor: '))
function somar(num1, num2) {
    resultado = num1 + num2;
}
function mostrar(msg) {
    alert(`O resultado da soma é: ${msg}`)
}
somar(entrada1, entrada2);
mostrar(resultado);

let valor1 = parseFloat(prompt('Digite o primeiro valor: '))
let valor2 = parseFloat(prompt('Digite o segundo valor: '))
let operacao = prompt('Digite a operação:\n+\n-\n*\n/')

function calculator(valor1, valor2, op) {
    if (operacao === '+') {
        return valor1 + valor2
    }

    else if (operacao === '-') {
        return valor1 - valor2
    }

    else if (operacao === '*') {
        return valor1 * valor2
    }

    else if (operacao === '/') {
        return valor1 / valor2
    }

    else {
        return 0;
    }
}
alert(calculator(valor1, valor2, operacao))

// Função anônima

// const soma = function (a, b) { return a + b }
// A function esta dentro da variavel

// Função arrow
// const soma = (a, b) => a + b; // Invisible, pois nao tem return

var exemplo = soma(1, 2);
alert(exemplo)
// estou chamando a varaivel invisible, do mesmo jeitinho.