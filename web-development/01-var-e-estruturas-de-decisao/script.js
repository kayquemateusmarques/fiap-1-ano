var entradaUsuario = Number(prompt('Digite um número de 1 a 5'));
if (entradaUsuario >= 1 && entradaUsuario <= 5)
    if (entradaUsuario == 1) {
        alert('O número digitado foi um.');
    }
    else if (entradaUsuario == 2) {
        alert('O número digitado foi dois.');
    }
    else if (entradaUsuario == 3) {
        alert('O número digitado foi três.');
    }
    else if (entradaUsuario == 4) {
        alert('O número digitado foi quatro.');
    }
    else {
        alert('O número digitado foi cinco.');
    }
else {
    alert('Digite apenas um número de 1 a 5!');
};






var num = parseInt(prompt('Digite vosso número entre 1 e 50'));
if (num <= 10) {
    console.log('O número digitado é:', num)
    alert('O número digitado está entre 1 e 10: ' + num);
}
else if (num <= 20) {
    console.log('O número digitado é:', num)
    alert('O número digitado está entre 11 e 20: ' + num);
}
else if (num <= 30) {
    console.log('O número digitado é:', num)
    alert('O número digitado está entre 21 e 30: ' + num);
}
else if (num <= 40) {
    console.log('O número digitado é:', num)
    alert('O número digitado está entre 31 e 40: ' + num);
}
else if (num <= 50) {
    console.log('O número digitado é:', num)
    alert('O número digitado está entre 41 e 50: ' + num);
}
else {
    alert('O número digitado não está entre o intervalo');
}

// || -> operador logico OU
// && -> operador lógico E
// -> Ao usar estes operadores, é preciso isolar as comparações.

var idade = parseInt(prompt('Digite tua idade'));
if(idade < 18){
    alert('Você é criança.')
}
else if ((idade >=18) && (idade <60)) {
    alert('Você é adulto')
}