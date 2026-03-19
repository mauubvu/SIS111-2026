import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

function calculadora(x: number){    
    const z = Number((15+(2*x/3))/(x**2+2))
    return `El valor de z es: ${z}`
}

console.log("Despejar Z");
console.log("*******************");

const num1 = Number(await rl.question("Introduzca el valor de x: "));
console.log(calculadora(num1));
rl.close();