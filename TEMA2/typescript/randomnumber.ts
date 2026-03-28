import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";
const rl = readline.createInterface({ input, output });
const {floor,random}=Math;

function rand(n: number,odd: string="", even: string = ""): string {
    for (let i=0;i<n;i++){
        const r = floor(random()*100)+1;
        if (r % 2 === 0) {
            even += `${r} `;
        } else {
            odd += `${r} `;
        }
    }
    return `Pares: ${even}\nImpares: ${odd}`;
}

const n = Number(await rl.question("Introduzca el limite: "));
console.log(rand(n));
rl.close();