for (let i = 0; i < 10; i++) {
    console.log(i)
}

// Laço de repetetição
let num = parseInt(prompt('Número: '))

for (let i = 1; i <= 10; i++) {
    let resultado = num * i;
    console.log(`${num} x ${i} = ${resultado}`)
}

// // Laço de repetição com variável
// let repetir = true
// while (repetir) {
//     console.log('Ao infinito... e além')
// }

// Switch case + laço while
let entrada = prompt('Insira um nome: ')

while (entrada != 'sair') {
    switch (entrada) {
        case 'Ana':
            alert('Olá, Ana!');
            break;
        case 'João':
            alert('Olá, João!');
            break;
        default:
            alert('Quem é você?')
            break
    }

    entrada = prompt('Insira um nome: ')
}