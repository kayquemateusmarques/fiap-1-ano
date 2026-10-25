// Escopo global (exemplo)
let resultado = 0

function somar(num1, num2){
    resultado = num1 + num2
}
alert(resultado(5, 5))

// Hosting EVITAR!!!!
// Eu posso escrever na linha errada, e a leitura do js muda para ALTURA correta. O ideal é na altura correta.

// this - escopo global

alert(this.resultado)

// O termo 'new' serve para usar o termo da variavel global, ainda que localmente ela seja reatribuida