import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });

let n = 1;
let pares = ""
let impares = ""
const limite = Number(await rl.question('Ingresa el limite: '))
for(;n<=limite;n++){
    if(n%2==0) pares = `${pares} ${n},`
    else impares = `${impares} ${n},`
}
console.log(`Lista pares: ${pares}`)
console.log(`Lista impares: ${impares}`)
rl.close();